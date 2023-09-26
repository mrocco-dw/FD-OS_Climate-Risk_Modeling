import sys
import os
import webview

os.chdir('C:\\Users\\jpafonso\\github\\fd-data-engineering\\FD-OS_Climate-Risk_Modeling\\Modeling\\python-library\\webapp\\') # custom to usename
sys.path.append('output/osf_model_app-0.0.1-py3.11.egg')
import osf_model_app

# run_mode
# Default =1 Flask browser  or  !=1  WebView App
run_mode =""
run_mode = os.getenv("RUN_MODE")
run_mode = run_mode if run_mode != "1" else "1"

assets_dir = "osf_model_app/"

model_name = ""
model_name = os.getenv ('MODEL_NAME')
model_name = model_name if model_name != "" else "fd-model-visual-search.html"

app = osf_model_app.OsfModel.webapp(assets_dir, model_name)

if run_mode == "1" :
     app.run(host='0.0.0.0', port=5000, debug=True)
else :
     webview.create_window('------->>>>> OSF Model WebApp <<<<<-------', app)
     webview.start()

