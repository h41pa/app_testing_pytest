from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
class AddRemoveElementsPage:
    LINK = "https://the-internet.herokuapp.com/add_remove_elements/"
    TITLE = (By.CSS_SELECTOR, "h3")
    ADD_ELEMENT_BUTTON = (By.XPATH, "//button[@onclick='addElement()']")
    DELETE_BUTTON = (By.XPATH, "//button[@onclick='deleteElement()']")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def load_page(self):
        self.driver.get(self.LINK)

    def click_add_button(self, number):
        for i in range(0, number):
            self.driver.find_element(*self.ADD_ELEMENT_BUTTON).click()


    def click_delete_button(self):
        self.driver.find_element(*self.DELETE_BUTTON).click()

    # what starts with get returns a text or a value
    def get_title(self):
        return self.driver.find_element(*self.TITLE).text

    # what start with is check True or False and in both cases returns
    def is_delete_button_displayed(self):
        return self.driver.find_element(*self.DELETE_BUTTON).is_displayed()


    def get_number_of_delete_buttons(self):
        return len(self.driver.find_elements(*self.DELETE_BUTTON))
