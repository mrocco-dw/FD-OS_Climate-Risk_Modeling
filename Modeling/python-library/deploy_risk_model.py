import sys
import os

model_abs_path=os.path.abspath('risk-modeling-osf')
os.chdir(model_abs_path)
print(model_abs_path)

sys.path.append('output/osf_risk_model-0.0.1-py3.11.egg')
#
import osf_risk_model
#
# Execute Training of Model Neural Network and print results
#
source_json_file='osf_risk_model/data/sample-training-modeling-data.json'
obj = osf_risk_model.OsfRiskTrainingClass.model_loanbook_asset(source_json_file)
#
print ("<< --- Model Training with Pytorch newral-network done with accuraccy results displayed --- >>")
#
