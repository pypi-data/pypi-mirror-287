class SpeedyBot:
    def __init__(self, token: str):
        self.token = token

    def getToken(self):
        return self.token
    
    def setToken(self, token: str):
        self.token = token
