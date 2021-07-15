#!/bin/bash

if [[ -z "$OPENDR_HOME" ]]; then
       echo "OPENDR_HOME is not defined"
       exit 1
fi

TYPE="runtime"
if [ "$#" -ge 1 ]; then
       TYPE=$1
fi

pip install ConfigParser numpy cython torch==1.7.1

python parse_dependencies.py $TYPE
# install dependencies one by one to prevent interdependency errors
if [ -f "python_dependencies.txt" ]; then
       cat python_dependencies.txt | xargs python -m pip install
fi
if [ -f "linux_dependencies.txt" ]; then
       cat linux_dependencies.txt | xargs sudo apt-get install
fi
