# -*- coding: UTF-8 -*-

"""
 Module
     write_template.py
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
     Define class WriteTemplate with atribute(s) and method(s).
     Write a template content with parameters to a file.
"""

import sys
from datetime import date
from os import getcwd, chmod
from string import Template
from inspect import stack

try:
    from module.module_selector import ModuleSelector

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


class WriteTemplate(object):
    """
        Define class WriteTemplate with atribute(s) and method(s).
        Write a template content with parameters to a file.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
            method:
                __init__ - Initial constructor
                get_check_setup - Getter for checking status
                write - Write a template content with parameters to a file
    """

    __slots__ = ('VERBOSE', '__check_setup')
    VERBOSE = 'GEN_PY_MODULE::MODULE::WRITE_TEMPLATE'

    def __init__(self, verbose=False):
        """
            Initial constructor
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(WriteTemplate.VERBOSE, verbose, 'Initial writer')
        self.__check_setup = False

    def get_check_setup(self):
        """
            Getter for checking status
            :return: Checked status
            :rtype: <bool>
            :exceptions: None
        """
        return self.__check_setup

    def write(self, module_content, module_name, module_type, verbose=False):
        """
            Write a template content with parameters to a file
            :param module_content: Template content
            :type module_content: <str>
            :param module_name: File name
            :type module_name: <str>
            :param module_type: Type of module
            :type module_type: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Boolean status
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        status = False
        verbose_message(WriteTemplate.VERBOSE, verbose, 'Write template')
        module_content_txt = 'Argument: expected module_content <str> object'
        module_content_msg = "{0} {1} {2}".format(
            'def', stack()[0][3], module_content_txt
        )
        module_name_txt = 'Argument: expected module_name <str> object'
        module_name_msg = "{0} {1} {2}".format(
            'def', stack()[0][3], module_name_txt
        )
        module_type_txt = 'Argument: expected module_type <str> object'
        module_type_msg = "{0} {1} {2}".format(
            'def', stack()[0][3], module_type_txt
        )
        if module_content is None or not module_content:
            raise ATSBadCallError(module_content_msg)
        if not isinstance(module_content, str):
            raise ATSTypeError(module_content_msg)
        if module_name is None or not module_name:
            raise ATSBadCallError(module_name_msg)
        if not isinstance(module_name, str):
            raise ATSTypeError(module_name_msg)
        if module_type is None or not module_type:
            raise ATSBadCallError(module_type_msg)
        if not isinstance(module_type, int):
            raise ATSTypeError(module_type_msg)
        self.__check_setup = True
        module_file_name = "{0}/{1}".format(
            getcwd(), ModuleSelector.format_name(module_name, module_type)
        )
        template = Template(module_content)
        if template:
            with open(module_file_name, 'w') as module_file:
                module_file.write(
                    template.substitute(
                        {
                            "mod": "{0}".format(module_name),
                            "modlc": "{0}".format(module_name.lower()),
                            "date": "{0}".format(date.today()),
                            "year": "{0}".format(date.today().year)
                        }
                    )
                )
                chmod(module_file_name, 0o666)
                status = True
        return True if status else False
