from flask import Flask

from myapp.views import blue


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='guanfangyidiande'
    app.register_blueprint(blue)
    return app