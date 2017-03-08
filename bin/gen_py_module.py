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
from os.path import dirname, realpath, exists
from datetime import datetime

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
		tool = "[{0}]".format(self.get_name())
		ver = "version {0}".format(self.get_version())
		print("\n{0} {1} {2}".format(tool, ver, datetime.now().date()))
		if self.get_tool_status():
			if len(sys.argv) > 1:
				op = sys.argv[1]
				if op not in GenPyModule.__OPS:
					sys.argv = []
					sys.argv.append("-h")
			else:
				sys.argv.append("-h")
			opts, args = self.parse_args(sys.argv)
			pymod = "{0}.py".format(opts.mod)
			if len(args) == 1 and opts.mod and not exists(pymod.lower()):
				op_txt = "generating python module"
				print("{0} {1} [{2}]".format(tool, op_txt, opts.mod))
				status = self.gen_module("{0}".format(opts.mod))
				if status == True:
					print("\n{0} {1}".format(tool, "done!\n"))
				else:
					op_txt = "failed to process and run option!\n"
					print("{0} {1}".format(tool, op_txt))
			else:
				op_txt = "module name already exist in local folder!\n"
				print("{0} {1}".format(tool, op_txt))
		else:
			op_txt = "tool is not operational!\n"
			print("{0} {1}".format(tool, op_txt))

