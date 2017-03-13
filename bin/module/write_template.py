# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from datetime import date
from os import getcwd, chmod
from string import Template
from module.module_selector import ModuleSelector

class WriteTemplate(object):
	"""
	Define class WriteTemplate with atribute(s) and method(s).
	Write a template content with parameters to a file.
	It defines:
		attribute:
			None
		method:
			__init__ - Initial constructor
			write - Write a template content with parameters to a file
	"""

	def __init__(self):
		pass

	def write(self, module_content, module_name, module_type):
		"""
		:arg: module_content - Template content
		:type: str
		:arg: module_name - File name
		:type: str
		:return: Boolean status
		:rtype: bool
		"""
		current_dir = getcwd()
		file_name = ModuleSelector.format_name(module_name, module_type)
		module_file = "{0}/{1}".format(current_dir, file_name)
		module = {
			"mod" : "{0}".format(module_name),
			"modlc": "{0}".format(module_name.lower()),
			"date" : "{0}".format(date.today()),
			"year" : "{0}".format(date.today().year)
		}
		try:
			template = Template(module_content)
			module_file = open(module_file, "w")
			module_file.write(template.substitute(module))
		except (IOError, KeyError) as e:
			print("I/O error({0}): {1}".format(e.errno, e.strerror))
			module_file.close()
		else:
			chmod(module_file, 0o666)
			module_file.close()
			return True
		return False
