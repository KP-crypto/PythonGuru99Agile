import configparser

config=configparser.RawConfigParser()
config.read("C:/Users/Acer/PycharmProjects/AgileDevelopment/configuration/config.txt")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url=config.get('common info','URL')
        return url

    @staticmethod
    def getUserid():
        userid = config.get('common info', 'userID')
        return userid

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password


