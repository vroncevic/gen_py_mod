# Generate Python Module

gen_py_module is toolset for generation Py Module.

Developed in python code: 100%.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/gen_py_module/workflows/Python%20package/badge.svg?branch=master)

### INSTALLATION
Navigate to release [page](https://github.com/vroncevic/gen_py_module/releases/tag/v1.0) download and extract release archive.

To install this set of modules type the following:

```
tar xvzf gen_py_module-1.0.tar.gz
cd gen_py_module-1.0/python-tool
cp -R ~/bin/   /root/scripts/gen_py_module/
cp -R ~/conf/  /root/scripts/gen_py_module/
cp -R ~/log/   /root/scripts/gen_py_module/
```

### DEPENDENCIES

This module requires these other modules and libraries:

* ats_utilities https://vroncevic.github.io/ats_utilities

### GENERATION FLOW OF PY MODULE

Base flow of generation process:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_py_module/dev/python-tool-docs/gen_py_module_flow.png)

### TOOL STRUCTURE

gen_py_module is based on Template mechanism:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_py_module/dev/python-tool-docs/gen_py_module.png)

Generator structure:

```
.
├── bin
│   ├── gen_py_module.py
│   ├── gen_py_module_run.py
│   └── module
│       ├── gen_module.py
│       ├── __init__.py
│       ├── module_selector.py
│       ├── read_template.py
│       └── write_template.py
├── conf
│   ├── gen_py_module.cfg
│   ├── gen_py_module_util.cfg
│   └── template
│       ├── abstract_abc_class.template
│       ├── abstract_base_class.template
│       ├── class.template
│       ├── empty.template
│       └── main.template
└── log
    └── gen_py_module.log
```

### COPYRIGHT AND LICENCE

Copyright (C) 2018 by hhttps://vroncevic.github.io/gen_py_module

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.4.2 or,
at your option, any later version of Python 3 you may have available.

:sparkles:
