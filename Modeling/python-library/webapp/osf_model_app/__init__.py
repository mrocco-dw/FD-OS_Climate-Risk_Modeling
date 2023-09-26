import os
import flask
import webview
from flask import Flask, render_template

class OsfModel:
    def __init__(self):
        self._x = None

    def webapp(assets_dir="osf_model_app/", model_name="fd-model-visual-search.html"):

        assets_dir = assets_dir if assets_dir != "" else "osf_model_app/"
        model_name = model_name if model_name != "" else "fd-model-visual-search.html"

        templates_dir_abs = os.path.abspath( assets_dir  + "templates" )

        print(templates_dir_abs)
                
        app = Flask(__name__, template_folder=templates_dir_abs)

        @app.route('/', methods=['GET', 'POST'])

        def home(model_name="fd-model-visual-search.html"):
            location_file =  model_name
            return render_template(template_name_or_list=location_file)
        
        return app
    
