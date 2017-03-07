# encoding: utf-8
"""
module.gen_module - class GenModule

Usage:
	from module.gen_setup import GenModule

	generator = GenModule()
	status = generator.gen_module("configuration")
	if status:
		# operation done

@date: Feb 25, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from module.read_template import ReadTemplate
from module.write_template import WriteTemplate
from module.module_selector import ModuleSelector

class GenModule(ReadTemplate, WriteTemplate):
	"""
	Define class GenModule with atribute(s) and method(s).
	Generate python module by template and parameters.
	It defines:
		attribute:
			None
		method:
			__init__ - Create and initial instance
			gen_module - Generate file python module
			
	"""

	def __init__(self):
		"""
		@summary: Basic constructor
		"""
		ReadTemplate.__init__(self)
		WriteTemplate.__init__(self)

	def gen_module(self, module_name):
		"""
		@summary: Generate setup.py by template and parameters
		@param module_name: Parameter module name
		@return: Success return true, else return false
		"""
		status = False
		module = ModuleSelector.choose_module()
		content = self.read(module)
		if content != None:
			status = self.write(content, module_name, module)
		return status

