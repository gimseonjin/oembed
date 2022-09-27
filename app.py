from flask import Flask

import src.controller as controller


app = Flask(__name__)


app.register_blueprint(controller.app)

if __name__ == '__main__':    
    app.run()