from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webdriver import WebDriver

class DropDown:
    LINK = "https://the-internet.herokuapp.com/dropdown"
    DROPDOWN_LIST = (By.ID, 'dropdown')
    OPTION_1 = (By.XPATH, "//select/option[@value='1']")
    OPTION_2 = (By.XPATH, "//select/option[@value='2']")


    def __init__(self, driver: WebDriver):
        self.driver = driver

    def load_page(self):
        self.driver.get(self.LINK)

    def select_option_1(self):
        Select(self.driver.find_element(*self.DROPDOWN_LIST)).select_by_value("1")

    def is_option_1_selected(self):
        return self.driver.find_element(*self.OPTION_1).is_displayed()

    def select_option_2(self):
        Select(self.driver.find_element(*self.DROPDOWN_LIST)).select_by_value("2")

    def is_option_2_selected(self):
        return self.driver.find_element(*self.OPTION_2).is_selected()

