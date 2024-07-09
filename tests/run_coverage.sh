#!/bin/bash
#
# @brief   gen_py_module
# @version v1.0.1
# @date    Sat Aug 1 07:52:38 2017
# @company None, free software to use 2017
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf htmlcov gen_py_module_coverage.xml gen_py_module_coverage.json .coverage
rm -rf fresh_new/ full_simple_new/ latest_pro/ simple_read/ simple_write/
ats_coverage_run.py -n gen_py_module -p ../README.md
rm -rf fresh_new/ full_simple_new/ latest_pro/ simple_read/ simple_write/
python3 -m coverage run -m --source=../gen_py_module unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html -d htmlcov
python3 -m coverage xml -o gen_py_module_coverage.xml 
python3 -m coverage json -o gen_py_module_coverage.json
python3 -m coverage report --format=markdown -m
