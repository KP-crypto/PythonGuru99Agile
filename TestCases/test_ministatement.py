import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from Pages.CustomerPage import CustomerPage
from Pages.Homepage import HomePage
from Utilities.readrequirement import ReadConfig
import pytest

class Test_MiniStatement():
    url = ReadConfig.getApplicationURL()
    userid = ReadConfig.getUserid()
    password = ReadConfig.getPassword()

    @pytest.mark.regression
    def test_miniStatement(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.hp.setusernme(self.userid)
        self.hp.setpassword(self.password)
        self.hp.clickbtn()

        try:
            self.cp=CustomerPage(self.driver)
            self.cp.click_mini_statement()
            self.element=self.cp.select_class()
            drp=Select(self.element)
            drp.select_by_visible_text("3309")
            self.cp.click_submit()
            time.sleep(3)
            self.driver.save_screenshot("C:/Users/Acer/PycharmProjects/AgileDevelopment/Screenshots/records.png")
            rows=self.cp.verify_row_count()
            print(len(rows))

            if len(rows)=='5':
                assert True
                self.driver.close()
            else:
                assert False
        except Exception as e:
            print(e)
            self.driver.close()















