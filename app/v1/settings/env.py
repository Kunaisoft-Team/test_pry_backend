import dotenv


class Env :
    MYSQL_HOST = str
    MYSQL_USER = str
    MYSQL_PASSWORD = str
    MYSQL_DB :str
    secret_key : str
    token_expire : int


    def __init__(self):
        self.MYSQL_HOST = self.get_key('MYSQL_HOST')
        self.MYSQL_USER = self.get_key('MYSQL_USER')
        self.MYSQL_PASSWORD = self.get_key('MYSQL_PASSWORD')
        self.MYSQL_DB = self.get_key('MYSQL_DB')
        self.secret_key = self.get_key('SECRET_KEY')
        self.token_expire:int = int(self.get_key('ACCESS_TOKEN_EXPIRE_MINUTES'))


    def get_key(self,key):
        env = dotenv.dotenv_values()

        return env.get(key)
