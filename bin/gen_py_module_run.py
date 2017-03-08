#!/usr/bin/env python
# encoding: utf-8
"""
gen_py_module_run - It defines main entry point.

@date: Feb 25, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from gen_py_module import GenPyModule

if __name__ == '__main__':

	tool = GenPyModule()
	tool.process()

