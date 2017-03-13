# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from module.read_template import ReadTemplate
from module.write_template import WriteTemplate
from module.module_selector import ModuleSelector

class GenModule(ReadTemplate, WriteTemplate):
	"""
	Define class GenModule with attribute(s) and method(s).
	Generate python module by template and parameters.
	It defines:
		attribute:
			None
		method:
			__init__ - Initial constructor
			gen_module - Generate file python module
	"""

	def __init__(self):
		ReadTemplate.__init__(self)
		WriteTemplate.__init__(self)

	def gen_module(self, module_name):
		"""
		:arg: module_name - Parameter module name
		:type: str
		:return: Boolean status
		:rtype: bool
		"""
		status = True
		module_type = ModuleSelector.choose_module()
		if module_type != ModuleSelector.Cancel:
			module_content = self.read(module_type)
			if module_content:
				status = self.write(module_content, module_name, module_type)
			else:
				status = False
		return status
