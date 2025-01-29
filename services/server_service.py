from models.server import Server


def register_server(server_ip_address: str): 
    server = Server(IpAddress=server_ip_address)
    server.save()
    return server

def set_server_status(id: str, status: str):
    server = Server.objects(pk=id).first()
    server.update(Status=status)
    return server