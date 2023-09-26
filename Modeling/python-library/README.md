
  # Create Project

    ~/FD-OS_Climate-Risk_Modeling/Modeling/python-library/risk-modeling-osf$ python3 create_model_egg.py 
     zip_safe flag not set; analyzing archive contents...

     jcerqueira@A-LPTP-Pifd7NVa:/mnt/c/Users/jpafonso/github/fd-data-engineering/FD-OS_Climate-Risk_Modeling/Modeling/python-library/risk-modeling-osf$ python3.exe create_model_egg.py 
      C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.1520.0_x64__qbz5n2kfra8p0\Lib\site-packages\setuptools\command\install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
      warnings.warn(
      zip_safe flag not set; analyzing archive contents...


# Build Model and WebApp of OSF Risk Modelling

    ~/FD-OS_Climate-Risk_Modeling/Modeling/python-library$ python3 delta_risk_modeling_build_app.py
     29

    jcerqueira@A-LPTP-Pifd7NVa:/mnt/c/Users/jpafonso/github/fd-data-engineering/FD-OS_Climate-Risk_Modeling/Modeling/python-library$ python3.exe delta_risk_modeling_build_app.py 
     29

# Build WebApp of OSG , WebServer as RUNMODE=2  WebApp as RUNMODE=1

    jcerqueira@A-LPTP-Pifd7NVa:/mnt/c/Users/jpafonso/github/fd-data-engineering/FD-OS_Climate-Risk_Modeling/Modeling/python-library/webapp$ python3.exe create_webapp.py 
     C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.1520.0_x64__qbz5n2kfra8p0\Lib\site-packages\setuptools\command\install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
    warnings.warn(
     zip_safe flag not set; analyzing archive contents...

    jcerqueira@A-LPTP-Pifd7NVa:/mnt/c/Users/jpafonso/github/fd-data-engineering/FD-OS_Climate-Risk_Modeling/Modeling/python-library/webapp$ cd ..
    
    jcerqueira@A-LPTP-Pifd7NVa:/mnt/c/Users/jpafonso/github/fd-data-engineering/FD-OS_Climate-Risk_Modeling/Modeling/python-library$ export MODEL_NAME="fd-model-visual-search.html"

    jcerqueira@A-LPTP-Pifd7NVa:/mnt/c/Users/jpafonso/github/fd-data-engineering/FD-OS_Climate-Risk_Modeling/Modeling/python-library$ export RUNMODE="2"

    jcerqueira@A-LPTP-Pifd7NVa:/mnt/c/Users/jpafonso/github/fd-data-engineering/FD-OS_Climate-Risk_Modeling/Modeling/python-library$ export RUNMODE="1"

    jcerqueira@A-LPTP-Pifd7NVa:/mnt/c/Users/jpafonso/github/fd-data-engineering/FD-OS_Climate-Risk_Modeling/Modeling/python-library$ python3.exe launch_model_webapp.py 
    
     