# encoding: utf-8
"""
module.module_selector - class ModuleSelector

Usage:
	from module.module_selector import ModuleSelector

	module = ModuleSelector.choose_module()
	# operate with module
	# ...

	file_name = ModuleSelector.format_name(module_name, module)
	# operate with file name
	# ...

@date: Feb 25, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

class ModuleSelector(object):
	"""
	Define class ModuleSelector with atribute(s) and method(s).
	Selecting python template module for generating process.
	It defines:
		attribute:
			Empty - 0 Empty modul3
			Main - 1 Main module
			Class - 2 Class module
			NotImp - 3 Not implemented (Abstract) class module
			ABC - 4 ABC abstract module
			Cancel - 5 Cancel option
			__MODULES - Dictionary with option/description
		method:
			choose_module - Selecting type of module for generating process
			format_name - Formating name for file module
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
		@summary: Selecting type of module for generating process
		@return: 0(Empty), 1(Main), 2(Class), 3(Not implem.), 4(ABC), 5(Cancel)
		"""
		print("\n Module option list:")
		for key in sorted(ModuleSelector.__MODULES):
			print("  {0} {1}".format(key, ModuleSelector.__MODULES[key]))
		while True:
			module = input(" Select module: ")
			if module not in ModuleSelector.__MODULES.keys():
				print(" Not an appropriate choice.")
			else:
				break
		return module

	@classmethod
	def format_name(cls, module_name, module_type):
		"""
		@summary: Format file name by module name and module type
		@param module_name: Module name (translate to lower case)
		@param module_type: Type of module (empty/class/main/NotImpl/ABC)
		@return: File name with extension
		"""
		if module_type == ModuleSelector.__MODULES[ModuleSelector.Main]:
			return "{0}_run{1}".format(module_name.lower(), ".py")
		return "{0}{1}".format(module_name.lower(), ".py")

