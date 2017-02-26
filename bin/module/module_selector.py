# encoding: utf-8
"""
module.module_selector - class ModuleSelector

Usage:
	from module.module_selector import ModuleSelector

	module = ModuleSelector.choose_module()
	# operate with module
	...

	file_name = ModuleSelector.format_name(module_name, module)
	# operate with file name

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
			__EXT - Extension python file
			__MODULES - List of options
		method:
			choose_module - Selecting type of module for generating process
	"""

	__EXT = ".py"

	__MODULES = {
		"1" : "Empty module",
		"2" : "Main module",
		"3" : "Class module",
		"4" : "Settings module",
		"5" : "Options module",
		"6" : "Abstract base module",
		"7" : "Abstract Google base module"
	}

	@classmethod
	def choose_module(cls):
		"""
		@summary: Selecting type of module for generating process
		@return: Range (1, 4)
		"""
		for key in sorted(ModuleSelector.__MODULES):
			print("{0}".format(key + " " + ModuleSelector.__MODULES[key]))
		while True:
			module = input("Select module: ")
			if module not in ModuleSelector.__MODULES.keys():
				print("Not an appropriate choice.")
			else:
				break
		return module

	@classmethod
	def format_name(cls, module_name, module):
		"""
		@summary: Format file name by module name and module type
		@param module_name: Module name (translate to lower case)
		@param module: Type of module (empty/class/main/settings/options)
		@return: File name with extension
		"""
		file_name = module_name.lower()
		if module == 0 or module == 2:
			pass
		elif module == 1:
			file_name = "{0}{1}".format(module_name, "_run")
		elif module == 3:
			file_name = "{0}".format("settings")
		elif module == 4:
			file_name = "{0}{1}".format("cli_options")
		return "{0}{1}".format(file_name, ModuleSelector.__EXT)

