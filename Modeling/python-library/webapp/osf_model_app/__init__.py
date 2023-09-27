import os
import flask
import webview
from flask import Flask, render_template

from osf_model_app.modelsources import HTML_TEMPLATE, HTML_HOME_TEMPLATE

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

        def homepage():
            return(HTML_HOME_TEMPLATE.substitute())
        
        @app.route('/fd-model-visual-search', methods=['GET', 'POST'])
        def home(model_name="fd-model-visual-search.html"):
            location_file =  model_name
            return render_template(template_name_or_list=location_file)

        @app.route('/<model_solution>', methods=['GET', 'POST'])
        def model_page(model_solution):
            location_file =  model_solution
            return render_template(template_name_or_list=model_solution)

        @app.route('/<some_place>', methods=['GET', 'POST'])
        def some_place_page(some_place):
            return(HTML_TEMPLATE.substitute(place_name=some_place))

        return app
    
