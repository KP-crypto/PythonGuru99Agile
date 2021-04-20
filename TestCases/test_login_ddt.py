import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from Pages.Homepage import HomePage
from Utilities.readrequirement import ReadConfig
from Utilities import Xlutils
import pytest

class TestDDT:
    url = ReadConfig.getApplicationURL()
    path="C:/Users/Acer/PycharmProjects/AgileDevelopment/TestData/Book 1 (1).xlsx"

    @pytest.mark.skip
    def test_ddt_invalid(self,setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        rows=Xlutils.getrowcount(self.path,'Sheet1')
        columns=Xlutils.getcolumncount(self.path,'Sheet1')

        for r in range(2,rows+1):
            self.username=Xlutils.readexel(self.path,'Sheet1',r,1)
            self.password=Xlutils.readexel(self.path,'Sheet1',r,2)
            self.hp.setusernme(self.username)
            self.hp.setpassword(self.password)
            self.hp.clickbtn()
            time.sleep(2)
            self.alert=Alert(self.driver)
            self.text=self.alert.text
            print(self.text)
            self.alert.accept()

        if "User or Password is not valid" in self.text:
            Xlutils.writeexel(self.path,'Sheet1',r,3,'Fail')

            self.driver.save_screenshot("C:/Users/Acer/PycharmProjects/AgileDevelopment/Screenshots/alertmsg.png")
            assert True
            self.driver.close()



















































