# coding: utf-8

"""
Base class for tomography acquisition (defined by Bliss)
"""

import os

import h5py

from nxtomo.application.nxtomo import NXtomo
from nxtomomill.utils.h5pyutils import from_data_url_to_virtual_source
from nxtomomill.utils.hdf5 import EntryReader
from nxtomomill.utils.utils import embed_url, get_file_name  # noqa F401

try:
    import hdf5plugin  # noqa F401
except ImportError:
    pass
import logging
import typing
from collections import OrderedDict

import numpy
from silx.io.url import DataUrl
from silx.io.utils import h5py_read_dataset
from pyunitsystem.metricsystem import MetricSystem

from nxtomomill.io.config import TomoHDF5Config

_logger = logging.getLogger(__name__)


def _ask_for_file_removal(file_path):
    res = input(f"Overwrite {file_path} ? (Y/n)")
    return res == "Y"


class BaseAcquisition:
    """
    Util class to group several hdf5 group together and to write the data
    Nexus / NXtomo compliant
    """

    _ENERGY_PATH = "technique/scan/energy"

    _DATASET_NAME_PATH = ("technique/scan/name",)

    _GRP_SIZE_PATH = ("technique/scan/nb_scans",)

    _SAMPLE_NAME_PATH = ("sample/name",)

    _TITLE_PATH = ("title",)

    _INSTRUMENT_NAME_PATH = (
        "technique/saving/beamline",
        "instrument/title",
    )

    _FOV_PATH = "technique/scan/field_of_view"

    _NB_LOOP_PATH = ("technique/scan/nb_loop", "technique/proj/nb_loop")

    _NB_TOMO_PATH = ("technique/scan/nb_tomo", "technique/proj/nb_tomo")

    _NB_TURNS_PATH = ("technique/proj/nb_turns",)

    _TOMO_N_PATH = "technique/proj/tomo_n", "technique/scan/tomo_n"

    _START_TIME_PATH = ("start_time",)

    _END_TIME_PATH = ("end_time",)

    _TECHNIQUE_MOTOR_PATHS = ("technique/scan/motor", "technique/proj/motor")

    _DETECTOR_ROI = ("technique/detector/roi",)

    _SOURCE_NAME = ("instrument/machine/name",)

    _SOURCE_TYPE = ("instrument/machine/type",)

    _FRAME_FLIP_PATHS = (
        "technique/detector/{detector_name}/flipping",
        "technique/detector/flipping",
    )

    def __init__(
        self,
        root_url: typing.Union[DataUrl, None],
        configuration: TomoHDF5Config,
        detector_sel_callback,
        start_index: int,
    ):
        self._root_url = root_url
        self._detector_sel_callback = detector_sel_callback
        self._registered_entries = OrderedDict()
        self._copy_frames = OrderedDict()
        # key is the entry, value his type
        self._entries_o_path = dict()
        # key is the entry, value his the entry path from the original file.
        # this value is different from `.name`. Don't know if this is a bug ?
        """user can have defined already some parameter values as energy.
        The idea is to avoid asking him if """
        self._configuration = configuration
        self._start_index = start_index

    @property
    def configuration(self):
        return self._configuration

    @property
    def start_index(self) -> int:
        return self._start_index

    def write_as_nxtomo(
        self,
        shift_entry: int,
        input_file_path: str,
        request_input: bool,
        divide_into_sub_files,
        input_callback=None,
    ) -> tuple:
        nx_tomos = self.to_NXtomos(
            request_input=request_input,
            input_callback=input_callback,
            check_tomo_n=True,
        )

        # preprocessing to define output file name
        possible_extensions = (".hdf5", ".h5", ".nx", ".nexus")
        output_file_basename = os.path.basename(self.configuration.output_file)
        file_extension_ = None
        for possible_extension in possible_extensions:
            if output_file_basename.endswith(possible_extension):
                output_file_basename.rstrip(possible_extension)
                file_extension_ = possible_extension

        def get_file_name_and_entry(index, divide_sub_files):
            entry = "entry" + str(index).zfill(4)

            if self.configuration.single_file or not divide_sub_files:
                en_output_file = self.configuration.output_file
            else:
                ext = file_extension_ or self.configuration.file_extension
                file_name = (
                    os.path.splitext(output_file_basename)[0]
                    + "_"
                    + str(index).zfill(4)
                    + ext
                )
                en_output_file = os.path.join(
                    os.path.dirname(self.configuration.output_file), file_name
                )

                if os.path.exists(en_output_file):
                    if self.configuration.overwrite is True:
                        _logger.warning(en_output_file + " will be removed")
                        _logger.info("remove " + en_output_file)
                        os.remove(en_output_file)
                    elif _ask_for_file_removal(en_output_file) is False:
                        raise OSError(f"unable to overwrite {en_output_file}, exit")
                    else:
                        os.remove(en_output_file)
            return en_output_file, entry

        result = []
        for i_nx_tomo, nx_tomo in enumerate(nx_tomos):
            output_file, data_path = get_file_name_and_entry(
                (shift_entry + i_nx_tomo), divide_sub_files=divide_into_sub_files
            )
            output_file = os.path.abspath(os.path.relpath(output_file, os.getcwd()))
            output_file = os.path.abspath(output_file)

            # For pcotomo for example the data path is modified in order to handle with the splitting
            # that does not fit at 100 % with the current API. for now there is
            # no convenient way to handle this in a better way
            assert isinstance(nx_tomo, NXtomo)
            # embed data if requested
            if len(nx_tomo.instrument.detector.data) == 0:
                _logger.warning(
                    f"No frame found for NXtomo number {i_nx_tomo}. Won't write any output for it"
                )
                continue
            vs_0 = nx_tomo.instrument.detector.data[0]
            if nx_tomo.detector_data_is_defined_by_url():
                new_urls = []
                for url in nx_tomo.instrument.detector.data:
                    if self._copy_frames[url.path()]:
                        created_url = embed_url(
                            url=url,
                            output_file=output_file,
                        )
                        new_urls.append(created_url)
                    else:
                        new_urls.append(url)
                nx_tomo.instrument.detector.data = new_urls
            elif nx_tomo.detector_data_is_defined_by_virtual_source():
                new_vs = []
                for vs in nx_tomo.instrument.detector.data:
                    assert isinstance(vs, h5py.VirtualSource)
                    assert isinstance(vs_0, h5py.VirtualSource)
                    url = DataUrl(file_path=vs.path, data_path=vs.name, scheme="silx")
                    if (
                        url.path() in self._copy_frames
                        and self._copy_frames[url.path()]
                    ):
                        new_url = embed_url(url, output_file=output_file)
                        n_vs, _, _ = from_data_url_to_virtual_source(new_url)
                        new_vs.append(n_vs)
                    else:
                        new_vs.append(vs)
                nx_tomo.instrument.detector.data = new_vs

            # provide some extra data like origin of the input_file
            if input_file_path is not None:
                nx_tomo.bliss_original_files = (os.path.abspath(input_file_path),)
            # save data
            nx_tomo.save(file_path=output_file, data_path=data_path)
            # check rotation angle
            if nx_tomo.sample.rotation_angle is not None:
                unique_angles = numpy.unique(nx_tomo.sample.rotation_angle)
                if len(unique_angles) == 1:
                    _logger.warning(
                        f"NXtomo {data_path}@{output_file} seems to have a single value ({unique_angles}) for rotation angle. Seems it fails to find correct path to the rotation angle dataset"
                    )

            result.append((output_file, data_path))
        return tuple(result)

    def to_NXtomos(self, request_input, input_callback, check_tomo_n=True) -> tuple:
        raise NotImplementedError("Base class")

    @property
    def raise_error_if_issue(self):
        """
        Should we raise an error if we encounter or an issue or should we
        just log an error message
        """
        return self.configuration.raises_error

    @property
    def is_xrd_ct(self):
        """Is this an XRD-CT acquisition"""
        raise NotImplementedError("Base class")

    @property
    def require_x_translation(self):
        """is `x_translation` expected"""
        raise NotImplementedError("Base class")

    @property
    def require_z_translation(self):
        """is `z_translation` expected"""
        raise NotImplementedError("Base class")

    @property
    def has_diode(self):
        """is the acquisition expect to have a diode (instead of an energy
        field)"""
        raise NotImplementedError("Base class")

    @property
    def root_url(self):
        return self._root_url

    def get_expected_nx_tomo(self):
        """
        Return the expected number of nxtomo created for this acquisition.
        This is required to get consistent entry and file name. At lest for automation
        """
        raise NotImplementedError("Base class")

    def read_entry(self):
        return EntryReader(self._root_url)

    def is_different_sequence(self, entry):
        """
        Can we have several entries 1.1, 1.2, 1.3... to consider.
        This is the case for XRD-CT where 1.1, 1.2, 1.3 should be consider as
        being part of the same sequence. Not for 'standard tomography'
        """
        raise ValueError("Base class")

    @staticmethod
    def _get_node_values_for_frame_array(
        node: h5py.Group,
        n_frame: int,
        keys: typing.Iterable,
        info_retrieve,
        expected_unit,
    ):
        def get_values():
            # this is a two step process: first step we parse all the
            # the keys until we found one with the expected length
            # if first iteration fails then we return the first existing key
            for respect_length in (True, False):
                for possible_key in keys:
                    if possible_key in node and isinstance(
                        node[possible_key], h5py.Dataset
                    ):
                        values_ = h5py_read_dataset(node[possible_key])
                        unit_ = BaseAcquisition._get_unit(
                            node[possible_key], default_unit=expected_unit
                        )
                        # skip values containing '*DIS*'
                        if isinstance(values_, str) and values_ == "*DIS*":
                            continue

                        if n_frame is not None and respect_length is True:
                            if numpy.isscalar(values_):
                                length = 1
                            else:
                                length = len(values_)
                            if length in (n_frame, n_frame + 1):
                                return values_, unit_
                        else:
                            return values_, unit_
            return None, None

        values, unit = get_values()
        if values is None:
            raise ValueError(
                f"Unable to retrieve {info_retrieve} for {node.name}. Was looking for {keys} datasets"
            )
        elif n_frame is None:
            return values, unit
        elif numpy.isscalar(values):
            return numpy.array([values] * n_frame), unit
        elif len(values) == n_frame:
            return values.tolist(), unit
        elif len(values) == (n_frame + 1):
            # for now we can have one extra position for rotation,
            # x_translation...
            # because saved after the last projection. It is recording the
            # motor position. For example in this case: 1 is the motor movement
            # (saved) and 2 is the acquisition
            #
            #  1     2    1    2     1
            #      -----     -----
            # -----     -----     -----
            #
            return values[:-1].tolist(), unit
        elif len(values) > n_frame:
            _logger.warning(
                f"Incoherent number of values found for {info_retrieve}. Can come from an acquisition canceled. Else please investigate."
            )
            # in this case only get the values which have a frame
            return values[0:n_frame], unit
        elif len(values) < n_frame:
            _logger.warning(
                f"Incoherent number of values found for {info_retrieve}. Can come from an acquisition canceled. Else please investigate."
            )
            # in this case append 0 to existing values. Maybe -1 would be better ?
            return list(values) + [0] * (n_frame - values), unit
        elif len(values) == 1:
            return numpy.array([values[0]] * n_frame), unit
        else:
            raise ValueError("incoherent number of angle position vs number of frame")

    def register_step(self, url: DataUrl, entry_type, copy_frames) -> None:
        """
        Add a bliss entry to the acquisition
        :param url:
        :param entry_type:
        """
        raise NotImplementedError("Base class")

    @staticmethod
    def _get_unit(node: h5py.Dataset, default_unit):
        """Simple process to retrieve unit from an attribute"""
        if "unit" in node.attrs:
            return node.attrs["unit"]
        elif "units" in node.attrs:
            return node.attrs["units"]
        else:
            _logger.info(
                f"no unit found for {node.name}, take default unit: {default_unit}"
            )
            return default_unit

    @staticmethod
    def _get_instrument_node(entry_node: h5py.Group) -> h5py.Group:
        if not isinstance(entry_node, h5py.Group):
            raise TypeError("entry_node: h5py.group expected")
        return entry_node["instrument"]

    @staticmethod
    def _get_positioners_node(entry_node):
        if not isinstance(entry_node, h5py.Group):
            raise TypeError("entry_node is expected to be a h5py.Group")
        parent_node = BaseAcquisition._get_instrument_node(entry_node)
        if "positioners" in parent_node:
            return parent_node["positioners"]
        else:
            return None

    @staticmethod
    def _get_measurement_node(entry_node):
        if not isinstance(entry_node, h5py.Group):
            raise TypeError("entry_node is expected to be a h5py.Group")
        if "measurement" in entry_node:
            return entry_node["measurement"]
        else:
            return None

    @staticmethod
    def _get_machine_node(entry_node):
        if not isinstance(entry_node, h5py.Group):
            raise TypeError("entry_node is expected to be a h5py.Group")
        if "instrument/machine" in entry_node:
            return entry_node["instrument/machine"]
        else:
            return None

    def _read_rotation_motor_name(self) -> typing.Union[str, None]:
        """read rotation motor from root_url/technique/scan/motor

        :return: name of the motor used for rotation. None if cannot find
        :rtype: Union[tuple, None]
        """
        if self._root_url is None:
            _logger.warning("no root url. Unable to read rotation motor")
            return None
        else:
            with EntryReader(self._root_url) as entry:
                for motor_path in self._TECHNIQUE_MOTOR_PATHS:
                    if motor_path in entry:
                        try:
                            rotation_motor = get_dataset_name_from_motor(
                                motors=h5py_read_dataset(
                                    numpy.asarray(entry[motor_path])
                                ),
                                motor_name="rotation",
                            )
                        except Exception as e:
                            _logger.error(e)
                        else:
                            return rotation_motor
                    else:
                        _logger.warning(
                            f"{motor_path} unable to find rotation motor from {self._root_url}"
                        )
                return None

    def _get_electric_current(self, root_node) -> list:
        """retrieve electric current provide a time stamp for each of them"""
        if root_node is None:
            _logger.warning("no root url. Unable to read electric current")
            return None, None
        else:
            grps = [
                root_node,
            ]

            measurement_node = self._get_measurement_node(root_node)
            if measurement_node is not None:
                grps.append(measurement_node)
            machine_node = self._get_machine_node(root_node)
            if machine_node is not None:
                grps.append(machine_node)

            for grp in grps:
                try:
                    elec_current, unit = self._get_node_values_for_frame_array(
                        node=grp,
                        keys=self.configuration.machine_electric_current_keys,
                        info_retrieve="machine electric current",
                        expected_unit="mA",
                        n_frame=None,
                    )
                except (ValueError, KeyError):
                    pass
                else:
                    # handle case where elec_current is a scalar. Cast it to list before return
                    if numpy.isscalar(elec_current):
                        elec_current = [
                            elec_current,
                        ]

                    return elec_current, unit
            else:
                _logger.warning(
                    f"Unable to retrieve machine electric current for {root_node.name}"
                )

            return None, None

    def _get_rotation_angle(self, root_node, n_frame) -> tuple:
        """return the list of rotation angle for each frame"""
        if not isinstance(root_node, h5py.Group):
            raise TypeError("root_node is expected to be a h5py.Group")

        for grp in (
            self._get_positioners_node(root_node),
            root_node,
            self._get_measurement_node(root_node),
        ):
            try:
                angles, unit = self._get_node_values_for_frame_array(
                    node=grp,
                    n_frame=n_frame,
                    keys=self.configuration.rotation_angle_keys,
                    info_retrieve="rotation angle",
                    expected_unit="degree",
                )
            except (ValueError, KeyError):
                pass
            else:
                return angles, unit

        mess = f"Unable to find rotation angle for {root_node.name}"
        if self.raise_error_if_issue:
            raise ValueError(mess)
        else:
            mess += "default value will be set. (0)"
            _logger.warning(mess)
            return [0] * n_frame, "degree"

    def _get_x_translation(self, root_node, n_frame) -> tuple:
        """return the list of translation for each frame"""
        for grp in self._get_positioners_node(root_node), root_node:
            try:
                x_tr, unit = self._get_node_values_for_frame_array(
                    node=grp,
                    n_frame=n_frame,
                    keys=self.configuration.x_trans_keys,
                    info_retrieve="x translation",
                    expected_unit="mm",
                )
                x_tr = numpy.asarray(x_tr) * MetricSystem.from_value(unit).value
            except (ValueError, KeyError):
                pass
            else:
                return x_tr, "m"

        mess = f"Unable to find x translation for {self.root_url.path()}"
        if self.raise_error_if_issue:
            raise ValueError(mess)
        else:
            mess += "default value will be set. (0)"
            _logger.warning(mess)
            return [0] * n_frame, "m"

    def _get_y_translation(self, root_node, n_frame) -> tuple:
        """return the list of translation for each frame"""
        for grp in self._get_positioners_node(root_node), root_node:
            try:
                y_tr, unit = self._get_node_values_for_frame_array(
                    node=grp,
                    n_frame=n_frame,
                    keys=self.configuration.y_trans_keys,
                    info_retrieve="y translation",
                    expected_unit="mm",
                )
                y_tr = numpy.asarray(y_tr) * MetricSystem.from_value(unit).value
            except (ValueError, KeyError):
                pass
            else:
                return y_tr, "m"

        mess = f"Unable to find y translation for {self.root_url.path()}"
        if self.raise_error_if_issue:
            raise ValueError(mess)
        else:
            mess += "default value will be set. (0)"
            _logger.warning(mess)
            return [0] * n_frame, "m"

    @staticmethod
    def get_z_translation_frm(root_node, n_frame: int, configuration: TomoHDF5Config):
        for grp in BaseAcquisition._get_positioners_node(root_node), root_node:
            try:
                z_tr, unit = BaseAcquisition._get_node_values_for_frame_array(
                    node=grp,
                    n_frame=n_frame,
                    keys=configuration.z_trans_keys,
                    info_retrieve="z translation",
                    expected_unit="mm",
                )
                z_tr = numpy.asarray(z_tr) * MetricSystem.from_value(unit).value
            except (ValueError, KeyError):
                pass
            else:
                return z_tr, "m"

        mess = f"Unable to find z translation on node {root_node.name}"
        if configuration.raises_error:
            raise ValueError(mess)
        else:
            mess += "default value will be set. (0)"
            _logger.warning(mess)
            return [0] * n_frame, "m"

    def _get_z_translation(self, root_node, n_frame) -> tuple:
        """return the list of translation for each frame"""
        return self.get_z_translation_frm(
            root_node=root_node,
            n_frame=n_frame,
            configuration=self.configuration,
        )

    def _get_expo_time(self, root_node, n_frame, detector_node) -> tuple:
        """return expo time for each frame"""
        for grp in detector_node["acq_parameters"], root_node:
            try:
                expo, unit = self._get_node_values_for_frame_array(
                    node=grp,
                    n_frame=n_frame,
                    keys=self.configuration.exposition_time_keys,
                    info_retrieve="exposure time",
                    expected_unit="s",
                )
            except (ValueError, KeyError):
                pass
            else:
                return expo, unit

        mess = f"Unable to find frame exposure time on entry {self.root_url.path()}"
        if self.raise_error_if_issue:
            raise ValueError(mess)
        else:
            mess += "default value will be set. (0)"
            _logger.warning(mess)
            return 0, "s"

    def get_axis_scale_types(self):
        """
        Return axis display for the detector data to be used by silx view
        """
        return ["linear", "linear"]

    def __str__(self):
        if self.root_url is None:
            return "NXTomo"
        else:
            return self.root_url.path()

    def get_detector_roi(self):
        if self._root_url is None:
            _logger.warning("no root url. Unable to read detector roi")
            return None
        else:
            with EntryReader(self._root_url) as entry:
                for roi_path in self._DETECTOR_ROI:
                    if roi_path in entry:
                        try:
                            roi = h5py_read_dataset(numpy.asarray(entry[roi_path]))
                        except Exception as e:
                            _logger.error(e)
                        else:
                            return roi
                    else:
                        _logger.warning(
                            f"{roi_path} unable to find detector roi from {self._root_url}"
                        )
                return None


def get_dataset_name_from_motor(motors, motor_name):
    motors = numpy.asarray(motors)
    indexes = numpy.where(motors == motor_name)[0]
    if len(indexes) == 0:
        return None
    elif len(indexes) == 1:
        index = indexes[0]
        index_dataset_id = index + 1
        if index_dataset_id < len(motors):
            return motors[index_dataset_id]
        else:
            raise ValueError(
                f"{motor_name} found but unable to find dataset name from {motors}"
            )
    else:
        raise ValueError(f"More than one instance of {motor_name} as been found.")
