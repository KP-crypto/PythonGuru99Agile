from selenium import webdriver
from Pages.Homepage import HomePage
from Utilities.readrequirement import ReadConfig
from Utilities.customlogger import logging
import pytest

logging.info("############################### Login Test has began ##########################")

class TestLogin:

    url=ReadConfig.getApplicationURL()
    userid=ReadConfig.getUserid()
    password=ReadConfig.getPassword()

    logging.info("##########  verify Home Page Title #################################")

    @pytest.mark.sanity
    def test_loginpageTitle(self,setup):
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        title=self.driver.title
        assert "Guru99 Bank Home Page" in title
        self.driver.close()

    logging.info("############# verify Home Page Title test case completed ############################# ")


    logging.info("############### Login test has started ############################################")

    def test_valid_login(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.hp=HomePage(self.driver)
        self.hp.setusernme(self.userid)
        self.hp.setpassword(self.password)
        self.hp.clickbtn()
        logintitle=self.driver.title
        assert "Guru99 Bank Customer HomePage" in logintitle
        self.driver.close()

    logging.info("############## Login Test Completed Successfully ##############################")











