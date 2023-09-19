import sys
sys.path.append('risk-modeling-esg/output/esg_risk_training-0.0.1-py3.11.egg')

import esg_risk_training

obj = esg_risk_training.EsgRiskTrainingClass()
obj.set_x(29)
print(obj.get_x())
