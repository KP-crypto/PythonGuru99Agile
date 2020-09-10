from selenium import webdriver
from Pages.Homepage import HomePage
from Utilities.readrequirement import ReadConfig
import pytest

class TestLogin:
    url=ReadConfig.getApplicationURL()
    userid=ReadConfig.getUserid()
    password=ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_loginpageTitle(self,setup):
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        title=self.driver.title
        assert "Guru99 Bank Home Page" in title
        self.driver.close()



    @pytest.mark.sanity
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











