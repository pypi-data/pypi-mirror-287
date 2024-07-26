# coding: utf-8

"""
Application to create a default configuration file to be used by h52nx application.

.. code-block:: bash

    usage: nxtomomill h5-config [-h] [--from-title-names] [--from-scan-urls] output_file

    Create a default configuration file

    positional arguments:
      output_file         output .cfg file

    optional arguments:
      -h, --help          show this help message and exit
      --from-title-names  Provide minimalistic configuration to make a conversion from titles names. (FRAME TYPE section is ignored). Exclusive with `from-scan-urls` option
      --from-scan-urls    Provide minimalistic configuration to make a conversion from scan urls. (ENTRIES and TITLES section is ignored). Exclusive with `from-title-names` option

For a complete tutorial you can have a look at: :ref:`Tomoh52nx`
"""

import argparse
import logging

from nxtomomill.io import TomoHDF5Config, XRD3DHDF5Config, generate_default_h5_config

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)


def main(argv):
    """ """
    parser = argparse.ArgumentParser(description="Create a default configuration file")
    parser.add_argument("output_file", help="output .cfg file")
    parser.add_argument(
        "--from-title-names",
        help="Provide minimalistic configuration to make a conversion from "
        "titles names. (FRAME TYPE section is ignored). \n"
        "Exclusive with `from-scan-urls` option",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "--from-scan-urls",
        help="Provide minimalistic configuration to make a conversion from "
        "scan urls. (ENTRIES and TITLES section is ignored).\n"
        "Exclusive with `from-title-names` option",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "--config-3dxrd",
        help="Configuration file for 3dxrd dataset",
        action="store_true",
        default=False,
    )

    options = parser.parse_args(argv[1:])

    if options.config_3dxrd:
        configuration = generate_default_h5_config(config_3dxrd=True)
        XRD3DHDF5Config.dict_to_cfg(file_path=options.output_file, dict_=configuration)
    else:
        configuration = generate_default_h5_config(config_3dxrd=False)
        if options.from_title_names:
            if options.from_scan_urls:
                raise ValueError(
                    "`from-title-names` and `from-scan-urls` are " "exclusive options"
                )
            del configuration[TomoHDF5Config.FRAME_TYPE_SECTION_DK]
        elif options.from_scan_urls:
            del configuration[TomoHDF5Config.ENTRIES_AND_TITLES_SECTION_DK]
        TomoHDF5Config.dict_to_cfg(file_path=options.output_file, dict_=configuration)
