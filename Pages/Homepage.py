class HomePage:
    userid_text_name="uid"
    password_text_name="password"
    btn_click_name="btnLogin"
    btn_click_reset_name="btnReset"
    link_logout_text="Log out"


    def __init__(self,driver):
        self.driver=driver

    def setusernme(self,userid):
        self.driver.find_element_by_name(self.userid_text_name).send_keys(userid)

    def setpassword(self,password):
        self.driver.find_element_by_name(self.password_text_name).send_keys(password)

    def clickbtn(self):
        self.driver.find_element_by_name(self.btn_click_name).click()

    def clickreset(self):
        self.driver.find_element_by_name(self.btn_click_reset_name).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.link_logout_text).click()







