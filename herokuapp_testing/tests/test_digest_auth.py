import time
from selenium.webdriver.common.by import By


LINK = "https://the-internet.herokuapp.com/digest_auth"

def test_check_if_login_is_successful(driver):
    driver.get(LINK)
    username = "admin"
    password = "admin"
    url_with_credentials = f"https://{username}:{password}@the-internet.herokuapp.com/digest_auth"
    driver.get(url_with_credentials)
    assert "Congratulations! You must have the proper credentials." in driver.find_element(By.CLASS_NAME, 'example').text, "ERROR , not logged"

