import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from Pages.Homepage import HomePage
from Pages.CustomerPage import CustomerPage
from Utilities.readrequirement import ReadConfig
import pytest

class Test_Logout():
    url = ReadConfig.getApplicationURL()
    userid = ReadConfig.getUserid()
    password = ReadConfig.getPassword()


    def test_logout(self,setup):
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.hp.setusernme(self.userid)
        self.hp.setpassword(self.password)
        self.hp.clickbtn()
        time.sleep(2)
        self.cp=CustomerPage(self.driver)
        self.cp.click_logout()
        time.sleep(2)
        self.alert=Alert(self.driver)
        logout_msg=self.alert.text
        assert "You Have Succesfully Logged Out!!" in logout_msg
        time.sleep(2)
        self.alert.accept()


