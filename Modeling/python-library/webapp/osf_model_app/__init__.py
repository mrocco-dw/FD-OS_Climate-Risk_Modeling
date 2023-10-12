import os
import flask
import webview
from flask import Flask, render_template, abort, send_file

from osf_model_app.modelsources import HTML_TEMPLATE, HTML_HOME_TEMPLATE

class OsfModel:
    def __init__(self):
        self._x = None

    def webapp(assets_dir="osf_model_app/", model_name="fd-model-visual-search.html"):

        assets_dir = assets_dir if assets_dir != "" else "osf_model_app/"
        model_name = model_name if model_name != "" else "fd-model-visual-search.html"

        templates_dir_abs = os.path.abspath( assets_dir  + "templates" )

        print(templates_dir_abs)
                
        app = Flask(__name__, static_folder=templates_dir_abs, template_folder=templates_dir_abs)
            
        @app.route('/', methods=['GET'])
        
        def list_templates_in_homepage(local_assets_dir="webapp/osf_model_app/"):
            
            local_assets_dir = local_assets_dir if local_assets_dir != "" else "webapp/osf_model_app/"
            local_templates_dir_abs = os.path.abspath( local_assets_dir  + "templates" )

            abs_path = local_templates_dir_abs
                         
            # Return 404 if path doesn't exist
            if not os.path.exists(abs_path):
                return abort(404)
            
            # Check if path is a file and serve
            if os.path.isfile(abs_path):
                return send_file(abs_path)
            
            my_files = os.listdir(abs_path)
            
            print(my_files)

            return render_template('home.html',files=my_files)
            #return(HTML_HOME_TEMPLATE.substitute(files=my_files))
        
        @app.route('/<model_solution>', methods=['GET', 'POST'])
        def model_page(model_solution):
            location_file =  model_solution
            return render_template(template_name_or_list=location_file)

        @app.route('/fd-model-visual-search', methods=['GET', 'POST'])
        def home(model_name="fd-model-visual-search.html"):
            location_file =  model_name
            return render_template(template_name_or_list=location_file)

        @app.route('/search/<some_place>', methods=['GET', 'POST'])
        def some_place_page(some_place):
            return(HTML_TEMPLATE.substitute(place_name=some_place))

        return app
    
