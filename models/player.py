import mongoengine as me

class Player(me.Document):
    Skins = me.ListField(default=[])
    Gamertag = me.StringField(required=True)
    SteamId = me.StringField(required=True, unique=True)
    CurrencyAmount = me.IntField(default=0)
