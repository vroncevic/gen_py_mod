# -*- coding: UTF-8 -*-

"""
 Module
     module_selector.py
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
     Define class ModuleSelector with attribute(s) and method(s).
     Selecting python template module for generating process.
"""

import sys
from inspect import stack

try:
    from ats_utilities.console_io.error import error_message
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


class ModuleSelector(object):
    """
        Define class ModuleSelector with attribute(s) and method(s).
        Selecting python template module for generating process.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                Empty  - 0 Empty module
                Main   - 1 Main module
                Class  - 2 Class module
                NotImp - 3 Not implemented (Abstract) class module
                ABC    - 4 ABC abstract module
                Cancel - 5 Cancel option
                __MODULES - Dictionary with option/description
            method:
                choose_module - Selecting type of module for generating process
                format_name - Formatting name for file module
    """

    __slots__ = (
        'VERBOSE',
        'Empty',
        'Main',
        'Class',
        'NotImp',
        'ABC',
        'Cancel',
        '__MODULES'
    )
    VERBOSE = 'GEN_PY_MODULE::MODULE::MODULE_SELECTOR'
    Empty, Main, Class, NotImp, ABC, Cancel = range(6)
    __MODULES = {
        Empty : "Empty module",
        Main : "Main module",
        Class : "Class module",
        NotImp : "Abstract base module",
        ABC : "Abstract ABC base module",
        Cancel : "Cancel"
    }

    @classmethod
    def choose_module(cls):
        """
            Selecting type of module for generating process
            :return: Module type id
            :rtype: <int>
            :exceptions: None
        """
        print("\n Module option list:")
        for key in sorted(ModuleSelector.__MODULES):
            print("  {0} {1}".format(key, ModuleSelector.__MODULES[key]))
        while True:
            try:
                module_type = int(raw_input(" Select module: "))
            except NameError:
                module_type = int(input(" Select module: "))
            if module_type not in ModuleSelector.__MODULES.keys():
                error_message(
                    ModuleSelector.VERBOSE, 'Not an appropriate choice.'
                )
            else:
                break
        return module_type

    @classmethod
    def format_name(cls, module_name, module_type):
        """
            Formatting name for file module
            :param module_name: Module name (translate to lower case)
            :type module_name: <str>
            :param module_type: Type of module (empty/class/main/NotImpl/ABC)
            :type module_type: <str>
            :return: File name with extension
            :rtype: <str>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        module_name_txt = 'Argument: expected module_name <str> object'
        module_name_msg = "{0} {1} {2}".format('def', func, module_name_txt)
        module_type_txt = 'Argument: expected module_name <str> object'
        module_type_msg = "{0} {1} {2}".format('def', func, module_type_txt)
        if module_name is None or not module_name:
            raise ATSBadCallError(module_name_msg)
        if not isinstance(module_name, str):
            raise ATSTypeError(module_name_msg)
        if module_type is None or not module_type:
            raise ATSBadCallError(module_type_msg)
        if not isinstance(module_type, int):
            raise ATSTypeError(module_type_msg)
        if module_type == ModuleSelector.__MODULES[ModuleSelector.Main]:
            return "{0}_run{1}".format(module_name.lower(), ".py")
        return "{0}{1}".format(module_name.lower(), ".py")
