# encoding: utf-8
"""
gen_py_module - class GenPyModule

Usage:
	from dist_py_module import DistPyModule

	tool = DistPyModule()
	tool.process()

@date: Feb 25, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

import sys
from app.base import Base
from module.gen_module import GenModule
from os.path import dirname, realpath

class GenPyModule(Base, GenModule):
	"""
	Define class GenPyModule with atribute(s) and method(s).
	Load a settings, create a CL interface and run operation(s).
	It defines:
		attribute:
			__CONFIG - Configuration file path
			__OPS - Tool options (list)
		method:
			__init__ - Create and initial instance
			process - Process and run tool option(s)
	"""

	__CONFIG = "/../conf/gen_py_module.cfg"
	__OPS = ["-g", "--gen", "-h", "--version"]

	def __init__(self):
		"""
		@summary: Basic constructor
		"""
		cdir = dirname(realpath(__file__))
		base_config_file = "{0}{1}".format(cdir, GenPyModule.__CONFIG)
		Base.__init__(self, base_config_file)
		if self.get_tool_status():
			self.add_new_option(
				GenPyModule.__OPS[0], GenPyModule.__OPS[1], dest="mod",
				help="Generate python module"
			)
			GenModule.__init__(self)

	def process(self):
		"""
		@summary: Process and run tool option(s)
		"""
		if self.get_tool_status():
			if len(sys.argv) > 1:
				op = sys.argv[1]
				if op not in GenPyModule.__OPS:
					sys.argv = []
					sys.argv.append("-h")
			else:
				sys.argv.append("-h")
			opts, args = self.parse_args(sys.argv)
			if len(args) == 1 and opts.mod:
				status = self.gen_module("{0}".format(opts.mod))
				if status == True:
					print("Done!\n")
			else:
				print("Failed to process and run option!\n")
		else:
			print("Tool is not operational!\n")

