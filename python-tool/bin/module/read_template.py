# -*- coding: UTF-8 -*-
# read_template.py
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
from os.path import dirname, realpath
from inspect import stack

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


class ReadTemplate(object):
    """
        Define class ReadTemplate with attribute(s) and method(s).
        Read a template file and return a string representation.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __TEMPLATE_DIR - Prefix path to templates
                __TEMPLATES - Modules (python templates)
                __template - Absolute template file path
            method:
                __init__ - Initial constructor
                read - Read a template and return a content or None
    """

    __slots__ = (
        'VERBOSE',
        '__TEMPLATE_DIR',
        '__TEMPLATES',
        '__template'
    )
    VERBOSE = 'MODULE::READ_TEMPLATE'
    __TEMPLATE_DIR = '/../../conf/template/'
    __TEMPLATES = {
        ModuleSelector.Empty: 'empty.template',
        ModuleSelector.Main: 'main.template',
        ModuleSelector.Class: 'class.template',
        ModuleSelector.NotImp: 'abstract_base_class.template',
        ModuleSelector.ABC: 'abstract_abc_class.template'
    }

    def __init__(self, verbose=False):
        """
            Initial constructor
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        current_dir = dirname(realpath(__file__))
        self.__template = "{0}{1}".format(
            current_dir, ReadTemplate.__TEMPLATE_DIR
        )

    def read(self, module_type):
        """
            Read a template and return a content or None
            :param module_type: File name
            :type module_type: <str>
            :return: Template module content | None
            :rtype: <str> | <NoneType>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func, module_content = stack()[0][3], None
        module_type_txt = 'Argument: expected module_type <str> object'
        module_type_msg = "{0} {1} {2}".format('def', func, module_type_txt)
        if module_type is None or not module_type:
            raise ATSBadCallError(module_type_msg)
        if not isinstance(module_type, str):
            raise ATSTypeError(module_type_msg)
        try:
            file_path = "{0}{1}".format(
                self.__template, ReadTemplate.__TEMPLATES[module_type]
            )
            template_file = open(file_path, 'r')
            module_content = template_file.read()
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
        else:
            if module_content:
                template_file.close()
        return module_content

