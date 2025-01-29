from flask import Blueprint, request, jsonify
import services.server_service as ServerService


server_controller = Blueprint("server_controller", __name__)

@server_controller.route("/server/register", methods=["POST"])
def register_server():
    ip_address = request.form.get("IpAddress")

    if ip_address:
        server = ServerService.register_server(ip_address)
        return jsonify(server)
    return jsonify({}, 403)

@server_controller.route("/server/status", methods=["POST"])
def update_server_status():
    id = request.form.get("Id")
    status = request.form.get("Status")

    if id and status:
        server = ServerService.set_server_status(id, status)
        return jsonify(server)
    return jsonify({}, 403)
