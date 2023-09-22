import flask
import webview
from flask import Flask

class OsfModel:
    def __init__(none):
        self._x = None

    def webapp(assets_dir):
        
        app = Flask(__name__)

        @app.route('/')

        def index():
            return "Open Sustainable Finance - Model Demo"
        
        @app.route('/model-visual-search')

        def model_ri_sligo(path):
            return flask.send_from_directory(assets_dir, path="fd-model-visual-search.html")
        
        return app
    
