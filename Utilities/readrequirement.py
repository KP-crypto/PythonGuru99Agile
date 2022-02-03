import configparser
from pathlib import Path

project_path = Path(__file__).parent.parent

config=configparser.RawConfigParser()
config.read(project_path+"/"+"/configuration/config.ini")

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


