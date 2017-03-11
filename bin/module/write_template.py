# encoding: utf-8
"""
setup.write_template - class WriteTemplate

Usage:
	from setup.write_template import WriteTemplate

	template_writter = WriteTemplate()
	# ...
	status = template_writter.write(module_content, module_name)
	if status == True:
		# operation done
		# ...

@date: Feb 24, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

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
		"""
		@summary: Basic constructor
		"""
		pass

	def write(self, setup_content, module_name, module_type):
		"""
		@summary: Write a template content with parameters to a file
		@param module_content: Template content
		@param module_name: Parameter module name
		@return: Success return true, else return false
		"""
		cdir = getcwd()
		file_name = ModuleSelector.format_name(module_name, module_type)
		module_file = "{0}/{1}".format(cdir, file_name)
		module = {
			"mod" : "{0}".format(module_name),
			"modlc": "{0}".format(module_name.lower()),
			"date" : "{0}".format(date.today()),
			"year" : "{0}".format(date.today().year)
		}
		try:
			template = Template(setup_content)
			mfile = open(module_file, "w")
			mfile.write(template.substitute(module))
		except (IOError, KeyError) as e:
			print("I/O error({0}): {1}".format(e.errno, e.strerror))
			mfile.close()
		else:
			chmod(module_file, 0o666)
			mfile.close()
			return True
		return False

