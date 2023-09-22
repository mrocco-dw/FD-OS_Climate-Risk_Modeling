import flask
import webview
from flask import Flask

class OsfModel:
    def __init__(none):
        self._x = None

    def webapp():    
        app = Flask(__name__)

        @app.route('/')

        def index():
            return flask.send_from_directory("./webapp/osf_model_app/assets", path="fd-model-visual-search.html")
        
        return app
    
