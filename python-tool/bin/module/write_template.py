# -*- coding: UTF-8 -*-
# write_template.py
# Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# gen_py_module is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gen_py_module is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys
from datetime import date
from os import getcwd, chmod
from string import Template

try:
    from module.module_selector import ModuleSelector
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ##################################

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
                write - Write a template content with parameters to a file
    """

    __slots__ = ('VERBOSE')
    VERBOSE = 'MODULE::WRITE_TEMPLATE'

    def __init__(self, verbose=False):
        """
            Initial constructor
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        pass

    def write(self, module_content, module_name, module_type):
        """
            Write a template content with parameters to a file
            :param module_content: Template content
            :type module_content: <str>
            :param module_name: File name
            :type module_name: <str>
            :param module_type: Type of module
            :type module_type: <str>
            :return: Boolean status
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func, status, current_dir = stack()[0][3], False, getcwd()
        module_content_txt = 'Argument: expected module_content <str> object'
        module_content_msg = "{0} {1} {2}".format(
            'def', func, module_content_txt
        )
        module_name_txt = 'Argument: expected module_name <str> object'
        module_name_msg = "{0} {1} {2}".format('def', func, module_name_txt)
        module_type_txt = 'Argument: expected module_type <str> object'
        module_type_msg = "{0} {1} {2}".format('def', func, module_type_txt)
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
        if not isinstance(module_type, str):
            raise ATSTypeError(module_type_msg)
        file_name = ModuleSelector.format_name(module_name, module_type)
        module_file_name = "{0}/{1}".format(current_dir, file_name)
        module = {
            "mod": "{0}".format(module_name),
            "modlc": "{0}".format(module_name.lower()),
            "date": "{0}".format(date.today()),
            "year": "{0}".format(date.today().year)
        }
        try:
            template = Template(module_content)
            module_file = open(module_file_name, 'w')
            module_file.write(template.substitute(module))
        except (IOError, KeyError) as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
        else:
            module_file.close()
            chmod(path=module_file_name, mode=0o666)
            status = True
        return True if status else False

