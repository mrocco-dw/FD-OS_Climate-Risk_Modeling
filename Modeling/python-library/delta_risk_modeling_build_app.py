import sys
sys.path.append('risk-modeling-osf/output/osf_risk_training-0.0.1-py3.11.egg')

import osf_risk_training

obj = osf_risk_training.OsfRiskTrainingClass()
obj.set_x(29)
print(obj.get_x())
