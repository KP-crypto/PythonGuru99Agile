class CustomerPage:

    link_mimi_statement_link_text="Mini Statement"
    select_text_name="accountno"
    btn_submit_name="AccSubmit"
    table_body_xpath="//tr//td//table"
    table_rows_xpath="//tr//td//table//tr"
    table_col_xpath="//tr//td//table//tr[1]//th"
    link_continue_text="Continue"
    click_link_logout_xpath="//a[contains(text(),'Log out')]"

    def __init__(self,driver):
        self.driver=driver

    def click_mini_statement(self):
        self.driver.find_element_by_link_text(self.link_mimi_statement_link_text).click()

    def select_class(self):
        element=self.driver.find_element_by_name(self.select_text_name)
        return element

    def click_submit(self):
        self.driver.find_element_by_name(self.btn_submit_name).click()

    def verify_row_count(self):
        rows=self.driver.find_elements_by_xpath(self.table_rows_xpath)
        return rows

    def click_logout(self):
        self.driver.find_element_by_xpath(self.click_link_logout_xpath).click()










