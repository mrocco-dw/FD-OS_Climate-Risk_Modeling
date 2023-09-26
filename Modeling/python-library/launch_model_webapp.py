import sys
import os
import webview

webserver_flask_abs_path=os.path.abspath('.')
webapp_abs_path=os.path.abspath('webapp')

os.chdir(webapp_abs_path)
sys.path.append('output/osf_model_app-0.0.1-py3.11.egg')
import osf_model_app

# run_mode
# Default =="2" Flask webserver  or ==1  WebView App

run_mode = os.getenv("RUNMODE", default="2")
print(run_mode)

assets_dir = "osf_model_app/"

model_name = os.getenv("MODEL_NAME", default="fd-model-visual-search.html")
print(model_name)

app = osf_model_app.OsfModel.webapp(assets_dir, model_name)

if run_mode == "2":
     os.chdir(webserver_flask_abs_path)
     app.run(host='0.0.0.0', port=5000, debug=True)
else:
     webview.create_window('--------------------------->>>>> OSF Model WebApp <<<<<---------------------------', app)
     webview.start()
