Generate Python Module
-----------------------

**gen_py_module** is tool for generation PY Module.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|gen_py_module python checker| |gen_py_module python package| |github issues| |documentation status| |github contributors|

.. |gen_py_module python checker| image:: https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_python_checker.yml

.. |gen_py_module python package| image:: https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_py_module.svg
   :target: https://github.com/vroncevic/gen_py_module/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_py_module.svg
   :target: https://github.com/vroncevic/gen_py_module/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen_py_module/badge/?version=latest
   :target: https://gen-py-module.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

|gen_py_module python3 build|

.. |gen_py_module python3 build| image:: https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_py_module/actions/workflows/gen_py_module_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_py_module/releases

To install **gen_py_module** type the following

.. code-block:: bash

    tar xvzf gen_py_module-x.y.z.tar.gz
    cd gen_py_module-x.y.z/
    # python3
    wget https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py 
    python3 -m pip install --upgrade setuptools
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade build
    pip3 install -r requirements.txt
    python3 -m build --no-isolation --wheel
    pip3 install ./dist/gen_py_module-*-py3-none-any.whl
    rm -f get-pip.py
    chmod 755 /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_py_module_run.py
    ln -s /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_py_module_run.py /usr/local/bin/gen_py_module_run.py

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # pyton3
    pip3 install gen-py-module

Dependencies
-------------

**gen_py_module** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
---------------

**gen_py_module** is based on OOP.

Code structure

.. code-block:: bash

    gen_py_module/
        ├── conf/
        │   ├── gen_py_module.cfg
        │   ├── gen_py_module.logo
        │   ├── gen_py_module_util.cfg
        │   ├── project.yaml
        │   └── template/
        │       ├── abstract_abc_class.template
        │       ├── abstract_base_class.template
        │       ├── class.template
        │       ├── empty.template
        │       └── main.template
        ├── __init__.py
        ├── log/
        │   └── gen_py_module.log
        ├── pro/
        │   ├── __init__.py
        │   ├── read_template.py
        │   └── write_template.py
        └── run/
            └── gen_py_module_run.py
        
        6 directories, 15 files

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2017 - 2024 by `vroncevic.github.io/gen_py_module <https://vroncevic.github.io/gen_py_module>`_

**gen_py_module** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_py_module/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
