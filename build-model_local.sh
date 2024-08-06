#!/usr/bin/env bash
#
# python3 is required as main python
#

# set -ex

source tmp311/bin/activate

PYTHON=python

echo "`$PYTHON -V`, `which $PYTHON`"

# PATTERN_X="+(Linux*|wsl*|MINGW64_NT-10.0-19045|MINGW64_NT-**.*-**)"
# if [[ "$(uname)" == $PATTERN_X ]]; then
#     export PYTHON_BUILD_COMMAND=python3.11.exe #=python.exe # FOR WSL / Linux WSL
# else
#     export PYTHON_BUILD_COMMAND=python # For MacBook / IOs
# fi


# idenpotent local build egg and launch webapp server
rm -rf Modeling/python-library/risk-modeling-osf/output/osf_risk_model-0.0.1-py3.11.egg
cd Modeling/python-library/risk-modeling-osf/
$PYTHON create_model_egg.py
cd ..
$PYTHON deploy_risk_model.py
#
