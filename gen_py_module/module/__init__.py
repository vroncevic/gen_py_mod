# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
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
     Defined class GenModule with attribute(s) and method(s).
     Generate python module by template and parameters.
'''

import sys

try:
    from gen_py_module.module.read_template import ReadTemplate
    from gen_py_module.module.write_template import WriteTemplate
    from gen_py_module.module.module_selector import ModuleSelector
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_py_module/blob/dev/LICENSE'
__version__ = '1.2.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenModule:
    '''
        Defined class GenModule with attribute(s) and method(s).
        Generate python module by template and parameters.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | __reader - reader API.
                | __writer - writer API.
            :methods:
                | __init__ - initial constructor.
                | get_reader - getter for reader object.
                | get_writer - getter for writer object.
                | gen_module - generate file python module.
                | __str__ - dunder method for GenModule.
    '''

    GEN_VERBOSE = 'GEN_PY_MODULE::MODULE::GEN_MODULE'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        verbose_message(GenModule.GEN_VERBOSE, verbose, 'init generator')
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)

    def get_reader(self):
        '''
            Getter for reader object.

            :return: read template object.
            :rtype: <ReadTemplate>
            :exceptions: None
        '''
        return self.__reader

    def get_writer(self):
        '''
            Getter for writer object.

            :return: write template object.
            :rtype: <WriteTemplate>
            :exceptions: None
        '''
        return self.__writer

    def gen_module(self, module_name, verbose=False):
        '''
            Generate file python module.

            :param module_name: parameter module name.
            :type module_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status True (success) | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:module_name', module_name)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        verbose_message(
            GenModule.GEN_VERBOSE, verbose, 'Generating module', module_name
        )
        module_type = ModuleSelector.choose_module()
        if module_type != ModuleSelector.Cancel:
            module_content = self.__reader.read(module_type, verbose=verbose)
            if module_content:
                status = self.__writer.write(
                    module_content, module_name, module_type, verbose=verbose
                )
        elif module_type == ModuleSelector.Cancel:
            status = True
        return status

    def __str__(self):
        '''
            Dunder method for GenModule.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, str(self.__reader), str(self.__writer)
        )
