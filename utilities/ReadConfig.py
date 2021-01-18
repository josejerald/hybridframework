import configparser

conf = configparser.ConfigParser()
conf.read(".\\Configuration\\config.ini")

class ReadConfig:

    @staticmethod
    def get_url():
        return conf.get("login","baseurl")

    @staticmethod
    def get_username():
        return conf.get("login","login")

    @staticmethod
    def get_password():
        return conf.get("login","pwd")


