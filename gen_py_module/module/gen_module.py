# -*- coding: UTF-8 -*-

"""
 Module
     gen_module.py
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
     Define class GenModule with attribute(s) and method(s).
     Generate python module by template and parameters.
"""

import sys
from inspect import stack

try:
    from gen_py_module.module.read_template import ReadTemplate
    from gen_py_module.module.write_template import WriteTemplate
    from gen_py_module.module.module_selector import ModuleSelector
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
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


class GenModule(object):
    """
        Define class GenModule with attribute(s) and method(s).
        Generate python module by template and parameters.
        It defines:

            :attributes:
                | __slots__ - Setting class slots
                | VERBOSE - Console text indicator for current process-phase
                | __reader - Reader API
                | __writer - Writer API
            :methods:
                | __init__ - Initial constructor
                | get_reader - Getter for reader object
                | get_writer - Getter for writer object
                | gen_module - Generate file python module
    """

    __slots__ = ('VERBOSE', '__reader', '__writer')
    VERBOSE = 'GEN_PY_MODULE::MODULE::GEN_MODULE'

    def __init__(self, verbose=False):
        """
            Initial constructor.

            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(GenModule.VERBOSE, verbose, 'Initial module')
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)

    def get_reader(self):
        """
            Getter for reader object.

            :return: Read template object
            :rtype: <ReadTemplate>
            :exceptions: None
        """
        return self.__reader

    def get_writer(self):
        """
            Getter for writer object.

            :return: Write template object
            :rtype: <WriteTemplate>
            :exceptions: None
        """
        return self.__writer

    def gen_module(self, module_name, verbose=False):
        """
            Generate file python module.

            :param module_name: Parameter module name
            :type module_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Boolean status True (success), else False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func, status = stack()[0][3], False
        module_name_txt = 'Argument: expected module_name <str> object'
        module_name_msg = "{0} {1} {2}".format('def', func, module_name_txt)
        if module_name is None or not module_name:
            raise ATSBadCallError(module_name_msg)
        if not isinstance(module_name, str):
            raise ATSTypeError(module_name_msg)
        verbose_message(
            GenModule.VERBOSE, verbose, 'Generating module', module_name
        )
        module_type = ModuleSelector.choose_module()
        if module_type != ModuleSelector.Cancel:
            module_content = self.__reader.read(module_type, verbose=verbose)
            if module_content:
                status = self.__writer.write(
                    module_content, module_name, module_type, verbose=verbose
                )
        return True if status else False
