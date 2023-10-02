#!/usr/bin/env bash
#
# python3 is required as main python
#
PATTERN_X="+(Linux*|wsl*)"
if [[ "$(uname)" == $PATTERN_X ]]; then
    export PYTHON_BUILD_COMMAND=python.exe # FOR WSL / Linux WSL
else
    export PYTHON_BUILD_COMMAND=python # For MacBook / IOs
fi
# idenpotent local build egg and launch webapp server
rm -rf Modeling/python-library/risk-modeling-osf/output/osf_risk_model-0.0.1-py3.11.egg
cd Modeling/python-library/risk-modeling-osf/
$PYTHON_BUILD_COMMAND create_model_egg.py
cd ..
$PYTHON_BUILD_COMMAND deploy_risk_model.py
#