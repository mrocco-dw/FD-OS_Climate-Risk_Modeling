import sys
import os
import webview

sys.path.append('webapp/output/osf_model_app-0.0.1-py3.11.egg')
import osf_model_app

model_name = ""
model_name = os.getenv ('MODEL_NAME')

assets_dir = "./webapp/osf_model_app/assets"

app = osf_model_app.OsfModel.webapp(assets_dir, model_name)

app.run(host='0.0.0.0', port=5000)

webview.create_window('OSF Model WebApp', app)
webview.start()
