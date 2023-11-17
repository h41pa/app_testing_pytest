import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_autentificare_corecta(browser):
    # Navigăm către pagina de login
    browser.get("https://the-internet.herokuapp.com/login")

    # Identificăm elementele și efectuăm acțiunile specifice
    username_field = browser.find_element(By.ID, "username")
    password_field = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.CSS_SELECTOR, "#login > button")

    username_field.send_keys("tomsmith")
    password_field.send_keys("SuperSecretPassword!")
    login_button.click()

    # Verificăm dacă am fost autentificați cu succes
    assert "You logged into a secure area!" in browser.page_source