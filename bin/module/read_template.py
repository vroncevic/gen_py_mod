# encoding: utf-8
"""
setup.read_template - class ReadTemplate

Usage:
	from setup.read_template import ReadTemplate
	# ...

	template_reader = ReadTemplate()
	module_content = template_reader.read(module_type)
	if module_content != None:
		# operate with content
		# ...

@date: Feb 24, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from os.path import dirname, realpath
from module.module_selector import ModuleSelector

class ReadTemplate(object):
	"""
	Define class ReadTemplate with atribute(s) and method(s).
	Read a template file (setup.template) and return a string representation.
	It defines:
		attribute:
			__TEMPLATE_DIR - Prefix path to templates
			__TEMPLATES - Modules (python templates)
			__template - Absolute template file path
		method:
			__init__ - Initial constructor
			read - Read a template and return a content or None
	"""

	__TEMPLATE_DIR = "/../../conf/template"

	__TEMPLATES = {
		ModuleSelector.Empty : "empty.template",
		ModuleSelector.Main : "main.template",
		ModuleSelector.Class : "class.template",
		ModuleSelector.NotImp : "abstract_base_class.template",
		ModuleSelector.ABC : "abstract_abc_class.template"
	}

	def __init__(self):
		"""
		@summary: Basic constructor
		"""
		cdir = dirname(realpath(__file__))
		self.__template = "{0}{1}".format(cdir, ReadTemplate.__TEMPLATE_DIR)

	def read(self, module_type):
		"""
		@summary: Read a template file and return a content
		@return: Template module content or None
		"""
		try:
			fpath = "{0}/{1}".format(
				self.__template, ReadTemplate.__TEMPLATES[module_type]
			)
			tfile = open(fpath, "r")
			module_content = tfile.read()
		except IOError as e:
			print("I/O error({0}): {1}".format(e.errno, e.strerror))
		else:
			if bool(module_content):
				tfile.close()
				return module_content
		return None

