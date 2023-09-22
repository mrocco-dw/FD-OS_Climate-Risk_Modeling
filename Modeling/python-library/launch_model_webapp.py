import sys

sys.path.append('webapp/output/osf_model_app-0.0.1-py3.11.egg')

import webview
import osf_model_app

app = osf_model_app.OsfModel.webapp()

webview.create_window('OSF Model WebApp', app)
webview.start()
