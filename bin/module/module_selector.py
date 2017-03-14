# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
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
			Empty - 0 Empty module
			Main - 1 Main module
			Class - 2 Class module
			NotImp - 3 Not implemented (Abstract) class module
			ABC - 4 ABC abstract module
			Cancel - 5 Cancel option
			__MODULES - Dictionary with option/description
		method:
			choose_module - Selecting type of module for generating process
			format_name - Formatting name for file module
	"""

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
		:return: Module type id
		:rtype: int
		"""
		print("\n Module option list:")
		for key in sorted(ModuleSelector.__MODULES):
			print("  {0} {1}".format(key, ModuleSelector.__MODULES[key]))
		while True:
			module_type = input(" Select module: ")
			if module_type not in ModuleSelector.__MODULES.keys():
				print(" Not an appropriate choice.")
			else:
				break
		return module_type

	@classmethod
	def format_name(cls, module_name, module_type):
		"""
		:param module_name: Module name (translate to lower case)
		:type: str
		:param module_type: Type of module (empty/class/main/NotImpl/ABC)
		:type: str
		:return: File name with extension
		:rtype: str
		"""
		if module_type == ModuleSelector.__MODULES[ModuleSelector.Main]:
			return "{0}_run{1}".format(module_name.lower(), ".py")
		return "{0}{1}".format(module_name.lower(), ".py")
