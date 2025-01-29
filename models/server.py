import mongoengine as me
from enum import Enum

class ServerStatus(Enum):
    STARTING = "STARTING"
    WAITING_FOR_PLAYERS = "WAITING_FOR_PLAYERS"
    GAME_IN_PROGRESS = "GAME_IN_PROGRESS"
    SHUTDOWN = "SHUTDOWN"

class Server(me.Document):
    IpAddress = me.StringField(required=True, unique=True)
    Status = me.StringField(default=ServerStatus.STARTING.value)
    players = me.ListField(field=me.StringField())

