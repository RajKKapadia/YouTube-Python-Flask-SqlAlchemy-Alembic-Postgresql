from flask import Flask

from src.views.user_view import user

app = Flask(__name__)

app.register_blueprint(user)
