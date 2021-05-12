# -*- coding: UTF-8 -*-

'''
 Module
     module_selector.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Definedd class ModuleSelector with attribute(s) and method(s).
     Selecting python template module for generating process.
'''

import sys

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.error import error_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_py_module/blob/dev/LICENSE'
__version__ = '1.3.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ModuleSelector:
    '''
        Defined class ModuleSelector with attribute(s) and method(s).
        Selecting python template module for generating process.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | Empty  - 0 Empty module.
                | Main   - 1 Main module.
                | Class  - 2 Class module.
                | NotImp - 3 Not implemented (Abstract) class module.
                | ABC    - 4 ABC abstract module.
                | Cancel - 5 Cancel option.
                | MODULES - dictionary with option/description.
            :methods:
                | choose_module - selecting type of module.
                | format_name - formatting name for file module.
                | __str__ - dunder method for ModuleSelector.
    '''

    GEN_VERBOSE = 'GEN_PY_MODULE::MODULE::MODULE_SELECTOR'
    Empty, Main, Class, NotImp, ABC, Cancel = range(6)
    MODULES = {
        Empty : 'Empty module',
        Main : 'Main module',
        Class : 'Class module',
        NotImp : 'Abstract base module',
        ABC : 'Abstract ABC base module',
        Cancel : 'Cancel'
    }

    @classmethod
    def choose_module(cls):
        '''
            Selecting type of module for generating process.

            :return: Module type id.
            :rtype: <int>
            :exceptions: None
        '''
        print('\n module option list:')
        for key in sorted(ModuleSelector.MODULES):
            print('  {0} {1}'.format(key, ModuleSelector.MODULES[key]))
        while True:
            try:
                module_type = int(raw_input(' select module: '))
            except NameError:
                module_type = int(input(' select module: '))
            if module_type not in ModuleSelector.MODULES.keys():
                error_message(
                    ModuleSelector.GEN_VERBOSE, 'not an appropriate choice'
                )
            else:
                break
        return module_type

    @classmethod
    def format_name(cls, module_name, module_type):
        '''
            Formatting name for file module.

            :param module_name: module name (translate to lower case).
            :type module_name: <str>
            :param module_type: type of module (empty/class/main/NotImpl/ABC).
            :type module_type: <int>
            :return: file name with extension.
            :rtype: <str>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:module_name', module_name), ('int:module_type', module_type)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        if module_type == ModuleSelector.MODULES[ModuleSelector.Main]:
            return '{0}_run{1}'.format(module_name.lower(), '.py')
        return '{0}{1}'.format(module_name.lower(), '.py')

    def __str__(self):
        '''
            Dunder method for ModuleSelector.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ()'.format(self.__class__.__name__)
