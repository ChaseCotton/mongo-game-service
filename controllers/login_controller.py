from flask import Blueprint, request, jsonify
from models.player import Player
import services.steam_service as SteamService

login_controller = Blueprint("login_controller", __name__)

@login_controller.route("/login/steam", methods=["POST"])
def login_steam():
    session_ticket = request.form.get("SessionTicket")
    player = None
    if session_ticket:
        steam_id = SteamService.login(session_ticket)
        player = Player.objects(SteamId=steam_id).first()
        if player is None:
            gamertag = SteamService.get_player_gamertag(steam_id)
            player = Player(SteamId=steam_id, Gamertag=gamertag)
            player.save()
    return jsonify(player)