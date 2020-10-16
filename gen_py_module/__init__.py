# -*- coding: UTF-8 -*-

"""
 Module
     gen_py_module.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
     gen_py_module is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     gen_py_module is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define class GenPyModule with attribute(s) and method(s).
     Load a settings, create a CL interface and run operation(s).
"""

import sys
from os import getcwd

try:
    from pathlib import Path
    from gen_py_module.module.gen_module import GenModule
    from ats_utilities.cfg_base import CfgBase
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.success import success_message
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2018, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"


class GenPyModule(CfgBase):
    """
        Define class GenPyModule with attribute(s) and method(s).
        Load a settings, create a CL interface and run operation(s).
        It defines:

            :attributes:
                | __slots__ - Setting class slots
                | VERBOSE - Console text indicator for current process-phase
                | __CONFIG - Configuration file path
                | __OPS - Tool options (list)
            :methods:
                | __init__ - Initial constructor
                | process - Process and run tool option(s)
    """

    __slots__ = ('VERBOSE', '__CONFIG', '__OPS')
    VERBOSE = 'GEN_PY_MODULE'
    __CONFIG = '/conf/gen_py_module.cfg'
    __OPS = ['-g', '--gen', '-h', '--version']

    def __init__(self, verbose=False):
        """
            Loading configuration and setting argument options.

            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        current_dir = Path(__file__).resolve().parent
        base_config_file = "{0}{1}".format(current_dir, GenPyModule.__CONFIG)
        CfgBase.__init__(self, base_config_file, verbose=verbose)
        if self.tool_status:
            self.add_new_option(
                GenPyModule.__OPS[0], GenPyModule.__OPS[1], dest="mod",
                help="Generate python module"
            )

    def process(self, verbose=False):
        """
            Process and run operation.

            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
            :exceptions: None
        """
        status = False
        if self.tool_status:
            num_of_args_sys = len(sys.argv)
            if num_of_args_sys > 1:
                operation = sys.argv[1]
                if operation not in GenPyModule.__OPS:
                    sys.argv = []
                    sys.argv.append('-h')
            else:
                sys.argv.append('-h')
            opts, args = self.parse_args(sys.argv)
            target_module = "{0}.py".format(opts.mod).lower()
            num_of_args, current_dir = len(args), getcwd()
            mod_path = "{0}/{1}".format(current_dir, target_module)
            mod_exists = Path(mod_path).exists()
            if num_of_args and opts.mod and not mod_exists:
                generator, gen_status = GenModule(verbose=verbose), False
                print(
                    "{0} {1} [{2}]".format(
                        "[{0}]".format(GenPyModule.VERBOSE),
                        'Generating python module', opts.mod
                    )
                )
                gen_status = generator.gen_module("{0}".format(opts.mod))
                if gen_status:
                    success_message(GenPyModule.VERBOSE, 'Done\n')
                    status = True
                else:
                    error_message(
                        GenPyModule.VERBOSE, 'Failed to generate module'
                    )
            else:
                error_message(GenPyModule.VERBOSE, 'module already exist !')
        else:
            error_message(GenPyModule.VERBOSE, 'Tool is not operational')
        return True if status else False
