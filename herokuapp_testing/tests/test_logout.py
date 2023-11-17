import time

from herokuapp_testing.pages.login_page import LoginPage
from herokuapp_testing.pages.secure_page import SecurePage

def test_logout_successful(driver):
    login = LoginPage(driver)
    secure = SecurePage(driver)
    login.load_page()
    login.set_username("tomsmith")
    login.set_password("SuperSecretPassword!")
    login.click_login_button()
    time.sleep(3)
    secure.click_logout_button()
    assert "https://the-internet.herokuapp.com/login" in login.current_url(), "Not same Url"
    assert "You logged out of the secure area!" in login.get_flash_message(), "Your message is not as expected"
    assert "#5da423" in login.is_button_green_or_red(), "Not green, something bad!"
    assert login.is_login_button_displayed(), "Login button is not displayed"
    assert "Login Page" in login.is_login_page_message_displayed(), "Login page message not displayed"
