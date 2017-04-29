#!/bin/bash

rm modules.cfg 2>> /dev/null
touch modules.cfg

for module in "$@"
do
    echo $module >> modules.cfg
done

python3 testsuite.py
