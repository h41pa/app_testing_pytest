from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    URl = "https://the-internet.herokuapp.com/login"
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "fa-sign-in")
    FLASH = (By.ID, "flash")
    LOGIN_PAGE_MESSAGE = (By.CSS_SELECTOR, "div>h2")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def load_page(self):
        self.driver.get(self.URl)

    def set_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_login_page_message_displayed(self):
        return self.driver.find_element(*self.LOGIN_PAGE_MESSAGE).text

    def is_login_button_displayed(self):
        return self.driver.find_element(*self.LOGIN_BUTTON).is_displayed()

    def get_flash_message(self):
        return self.driver.find_element(*self.FLASH).text

    def current_url(self):
        return self.driver.current_url

    def is_button_green_or_red(self):
        rgb = self.driver.find_element(*self.FLASH).value_of_css_property('background-color')
        button_color = Color.from_string(rgb).hex
        return button_color

    def get_bottom_href(self):
        return self.driver.find_element(By.XPATH, '//*[@id="page-footer"]/div/div/a').get_attribute("href")
