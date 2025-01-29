import os 
from flask_dotenv import DotEnv
from flask import Flask, jsonify
from flask_mongoengine import MongoEngine

from middleware.format_response import format_response_middleware

from models.player import Player

from controllers.login_controller import login_controller
from controllers.server_controller import server_controller

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


env = DotEnv()
env.init_app(app, os.path.join(basedir, ".env"))

app.config["MONGODB_SETTINGS"] = {
    "db": "GameService",
    "host": os.getenv("MONGO_URI"),
    "port": 27017
}

db = MongoEngine(app)

app.register_blueprint(login_controller)
app.register_blueprint(server_controller)

app.after_request(format_response_middleware)

@app.route("/")
def home():
    return "Hello"

@app.route("/player/<string:SteamId>/<string:Gamertag>")
def get_player(SteamId, Gamertag):
    if SteamId == "steam_id":
        return {"Gamertag": "savs"}
    else:
        player = Player(Gamertag=Gamertag, SteamId=SteamId)
        player.save()
        return jsonify(player)