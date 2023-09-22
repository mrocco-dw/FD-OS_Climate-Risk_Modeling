import sys
#import os
#os.chdir('/mnt/c/Users/jpafonso/github/fd-data-engineering/FD-OS_Climate-Risk_Modeling/Modeling/python-library')

sys.path.append('webapp/output/osf_model_app-0.0.1-py3.11.egg')

import webview
import osf_model_app

assets_dir = "./webapp/osf_model_app/assets"

app = osf_model_app.OsfModel.webapp(assets_dir)

webview.create_window('OSF Model WebApp', app)
webview.start()
