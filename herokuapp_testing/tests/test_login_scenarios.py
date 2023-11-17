import time

from herokuapp_testing.pages.login_page import LoginPage
from herokuapp_testing.pages.secure_page import SecurePage


def test_url_and_login_message(driver):
    login = LoginPage(driver)
    login.load_page()
    assert "Login Page" == login.is_login_page_message_displayed(), "Not same text"
    assert "https://the-internet.herokuapp.com/login" == login.current_url(), "Not same url"


def test_check_if_login_is_successful(driver):
    login = LoginPage(driver)
    secure = SecurePage(driver)
    login.load_page()
    time.sleep(5)
    login.set_username("tomsmith")
    login.set_password("SuperSecretPassword!")
    login.click_login_button()
    time.sleep(3)
    assert "You logged into a secure area!" in secure.get_flash_msj(), "Your login does not look successful."
    assert "#5da423" in secure.is_button_green_or_red(), f"Seems it's not green , it s {secure.is_button_green_or_red()}"
    assert "Secure Area" == secure.is_secure_area_page_message_displayed(), "Secure Area is not displayed"
    assert secure.is_logout_button_displayed(), "Logout button is not displayed"


def test_login_with_invalid_password(driver):
    login = LoginPage(driver)
    login.load_page()
    login.set_username("tomsmith")
    login.set_password("SuperSecretPasswordd! ")
    login.click_login_button()
    assert "Your password is invalid!" in login.get_flash_message(), "Something it's wrong"
    assert "#c60f13" in login.is_button_green_or_red(), "button colour not red as supposed"


def test_login_with_invalid_username(driver):
    login = LoginPage(driver)
    login.load_page()
    login.set_username("tomsmith-")
    login.set_password("SuperSecretPasswordd!")
    login.click_login_button()
    assert "Your username is invalid!" in login.get_flash_message(), "Something it's wrong "
    assert "#c60f13" in login.is_button_green_or_red(), "Supposed to be red but it's not"

def test_login_without_username(driver):
    login = LoginPage(driver)
    login.load_page()
    login.set_password("SuperSecretPassword!")
    login.click_login_button()
    assert "Your username is invalid!" in login.get_flash_message(), "Something is not working as it should"

def test_login_without_password(driver):
    login = LoginPage(driver)
    login.load_page()
    login.set_username("tomsmith")
    login.click_login_button()
    assert "Your password is invalid!" in login.get_flash_message(), "Something is not working as it should"

def test_href_attribute(driver):
    login = LoginPage(driver)
    login.load_page()
    assert "http://elementalselenium.com/" in login.get_bottom_href() , "Something wnet wrong."