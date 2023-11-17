from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.remote.webdriver import WebDriver


class SecurePage:
    URL = "https://the-internet.herokuapp.com/secure"
    FLASH = (By.ID, "flash")
    LOGOUT_BUTTON = (By.CLASS_NAME, "icon-signout")
    SECURE_AREA = (By.CSS_SELECTOR, "#content h2")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def load_page(self):
        self.driver.get(*self.URL)

    def is_secure_area_page_message_displayed(self):
        return self.driver.find_element(*self.SECURE_AREA).text

    def is_logout_button_displayed(self):
        return self.driver.find_element(*self.LOGOUT_BUTTON).is_displayed()

    def get_flash_msj(self):
        return self.driver.find_element(*self.FLASH).text

    def click_logout_button(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()

    def is_button_green_or_red(self):
        rgb = self.driver.find_element(*self.FLASH).value_of_css_property('background-color')
        button_colour = Color.from_string(rgb).hex
        return button_colour
