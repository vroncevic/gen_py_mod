# Generate Python Module

**gen_py_module** is tool for generation PY Module.

Developed in **[python](https://www.python.org/)** code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/gen_py_module/workflows/Python%20package%20gen_py_module/badge.svg?branch=master) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_py_module.svg)](https://github.com/vroncevic/gen_py_module/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_py_module.svg)](https://github.com/vroncevic/gen_py_module/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
- [Dependencies](#dependencies)
- [Generation flow of py module](#generation-flow-of-py-module)
- [Library structure](#library-structure)
- [Docs](#docs)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

![Install Python2 Package](https://github.com/vroncevic/gen_py_module/workflows/Install%20Python2%20Package%20gen_py_module/badge.svg?branch=master) ![Install Python3 Package](https://github.com/vroncevic/gen_py_module/workflows/Install%20Python3%20Package%20gen_py_module/badge.svg?branch=master)

Navigate to **[release page](https://github.com/vroncevic/gen_py_module/releases)** download and extract release archive.

To install **gen_py_module** type the following:
```
tar xvzf gen_py_module-x.y.z.tar.gz
cd gen_py_module-x.y.z
pip install -r requirements.txt
```

Install lib process
```
python setup.py install_lib
running install_lib
running build_py
creating build
creating build/lib.linux-x86_64-2.7
creating build/lib.linux-x86_64-2.7/gen_py_module
copying gen_py_module/__init__.py -> build/lib.linux-x86_64-2.7/gen_py_module
creating build/lib.linux-x86_64-2.7/gen_py_module/module
copying gen_py_module/module/__init__.py -> build/lib.linux-x86_64-2.7/gen_py_module/module
copying gen_py_module/module/write_template.py -> build/lib.linux-x86_64-2.7/gen_py_module/module
copying gen_py_module/module/read_template.py -> build/lib.linux-x86_64-2.7/gen_py_module/module
copying gen_py_module/module/module_selector.py -> build/lib.linux-x86_64-2.7/gen_py_module/module
copying gen_py_module/module/gen_module.py -> build/lib.linux-x86_64-2.7/gen_py_module/module
creating /usr/local/lib/python2.7/dist-packages/gen_py_module
creating /usr/local/lib/python2.7/dist-packages/gen_py_module/module
copying build/lib.linux-x86_64-2.7/gen_py_module/module/__init__.py -> /usr/local/lib/python2.7/dist-packages/gen_py_module/module
copying build/lib.linux-x86_64-2.7/gen_py_module/module/write_template.py -> /usr/local/lib/python2.7/dist-packages/gen_py_module/module
copying build/lib.linux-x86_64-2.7/gen_py_module/module/read_template.py -> /usr/local/lib/python2.7/dist-packages/gen_py_module/module
copying build/lib.linux-x86_64-2.7/gen_py_module/module/module_selector.py -> /usr/local/lib/python2.7/dist-packages/gen_py_module/module
copying build/lib.linux-x86_64-2.7/gen_py_module/module/gen_module.py -> /usr/local/lib/python2.7/dist-packages/gen_py_module/module
copying build/lib.linux-x86_64-2.7/gen_py_module/__init__.py -> /usr/local/lib/python2.7/dist-packages/gen_py_module
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_py_module/module/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_py_module/module/write_template.py to write_template.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_py_module/module/read_template.py to read_template.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_py_module/module/module_selector.py to module_selector.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_py_module/module/gen_module.py to gen_module.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/gen_py_module/__init__.py to __init__.pyc
```

Install lib egg info
```
python setup.py install_egg_info
running install_egg_info
running egg_info
creating gen_py_module.egg-info
writing requirements to gen_py_module.egg-info/requires.txt
writing gen_py_module.egg-info/PKG-INFO
writing top-level names to gen_py_module.egg-info/top_level.txt
writing dependency_links to gen_py_module.egg-info/dependency_links.txt
writing manifest file 'gen_py_module.egg-info/SOURCES.txt'
reading manifest file 'gen_py_module.egg-info/SOURCES.txt'
writing manifest file 'gen_py_module.egg-info/SOURCES.txt'
Copying gen_py_module.egg-info to /usr/local/lib/python2.7/dist-packages/gen_py_module-1.0.0-py2.7.egg-info
```

Install lib data
```
python setup.py install_data
running install_data
copying gen_py_module/run/gen_py_module_run.py -> /usr/local/bin/
creating /usr/local/lib/python2.7/dist-packages/gen_py_module/conf
copying gen_py_module/conf/gen_py_module.cfg -> /usr/local/lib/python2.7/dist-packages/gen_py_module/conf/
copying gen_py_module/conf/gen_py_module_util.cfg -> /usr/local/lib/python2.7/dist-packages/gen_py_module/conf/
creating /usr/local/lib/python2.7/dist-packages/gen_py_module/conf/template
copying gen_py_module/conf/template/abstract_abc_class.template -> /usr/local/lib/python2.7/dist-packages/gen_py_module/conf/template/
copying gen_py_module/conf/template/abstract_base_class.template -> /usr/local/lib/python2.7/dist-packages/gen_py_module/conf/template/
copying gen_py_module/conf/template/class.template -> /usr/local/lib/python2.7/dist-packages/gen_py_module/conf/template/
copying gen_py_module/conf/template/empty.template -> /usr/local/lib/python2.7/dist-packages/gen_py_module/conf/template/
copying gen_py_module/conf/template/main.template -> /usr/local/lib/python2.7/dist-packages/gen_py_module/conf/template/
creating /usr/local/lib/python2.7/dist-packages/gen_py_module/log
copying gen_py_module/log/gen_py_module.log -> /usr/local/lib/python2.7/dist-packages/gen_py_module/log/
```

Or You can use docker to create image/container.

[![gen_py_module docker checker](https://github.com/vroncevic/gen_py_module/workflows/gen_py_module%20docker%20checker/badge.svg)](https://github.com/vroncevic/gen_py_module/actions?query=workflow%3A%22gen_py_module+docker+checker%22)

### Dependencies

**gen_py_module** requires next modules and libraries:

* [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/ats_utilities)

### Generation flow of py module

Base flow of generation process:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_py_module/dev/docs/gen_py_module_flow.png)

### Library structure

**gen_py_module** is based on OOP:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_py_module/dev/docs/gen_py_module.png)

Library structure:
```
.
├── conf/
│   ├── gen_py_module.cfg
│   ├── gen_py_module_util.cfg
│   └── template/
│       ├── abstract_abc_class.template
│       ├── abstract_base_class.template
│       ├── class.template
│       ├── empty.template
│       └── main.template
├── __init__.py
├── log/
│   └── gen_py_module.log
├── module/
│   ├── gen_module.py
│   ├── __init__.py
│   ├── module_selector.py
│   ├── read_template.py
│   └── write_template.py
└── run/
    └── gen_py_module_run.py
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_py_module/badge/?version=latest)](https://gen_py_module.readthedocs.io/projects/gen_py_module/en/latest/?badge=latest)

More documentation and info at:
* [gen_py_module.readthedocs.io](https://gen_py_module.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2020 by [vroncevic.github.io/gen_py_module](https://vroncevic.github.io/gen_py_module/)

**gen_py_module** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_py_module/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
