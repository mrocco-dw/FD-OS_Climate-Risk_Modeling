import flask
import webview
from flask import Flask

class OsfModel:
    def __init__(self):
        self._x = None

    def webapp(assets_dir, model_name):

        assets_dir = assets_dir if assets_dir else "./webapp/osf_model_app/assets"
        model_name = model_name if model_name else "fd-model-visual-search.html"
        
        app = Flask(__name__)

        @app.route('/')

        def home():

            return flask.send_from_directory(assets_dir, path=model_name)
        
        return app
    
