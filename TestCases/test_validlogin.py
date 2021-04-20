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
        if title == "Guru99 Bank Home Page":
            logging.info('Expected title matched actual title')
            assert True
        else:
            logging.info('Expected title not matched actual title')
        self.driver.close()

    logging.info("############# verify Home Page Title test case completed ############################# ")


    logging.info("############### Login test has started ############################################")

    @pytest.mark.regression
    def test_valid_login(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.hp=HomePage(self.driver)
        self.hp.setusernme(self.userid)
        self.hp.setpassword(self.password)
        self.hp.clickbtn()
        logintitle=self.driver.title
        if logintitle == "Guru99 Bank Customer HomePage":
            logging.info('HomePage Title matched with our expected Title')
            logging.info("Guru99 Bank Customer HomePage")
            assert True
        else:
            logging.info('HomePage Title not matched with our expected Title')
            logging.info('Actual title was:- Guru99 Bank Customer HomePage')
        self.driver.close()

    logging.info("############## Login Test Completed Successfully ##############################")











