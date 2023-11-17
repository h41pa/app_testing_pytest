from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class KeyPress:
    BODY = (By.CLASS_NAME, "no-js")
    GREEN_MESSAGE = (By.ID, "result")
    EMPTY_FIELD = (By.ID, "target")
    LINK = "https://the-internet.herokuapp.com/key_presses"

    def __init__(self, driver: WebDriver):
        self.driver = driver


    def load_page(self):
        self.driver.get(self.LINK)

    def press_enter_key(self):
        self.driver.find_element(*self.BODY).send_keys(Keys.ENTER)

    def press_backspace_key(self):
        self.driver.find_element(*self.EMPTY_FIELD).send_keys(Keys.BACKSPACE)

    def press_delete_key(self):
        self.driver.find_element(*self.EMPTY_FIELD).send_keys(Keys.DELETE)

    def get_green_message(self):
        return self.driver.find_element(*self.GREEN_MESSAGE).text


