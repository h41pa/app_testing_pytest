from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

LINK = "https://the-internet.herokuapp.com/context_menu"


def test_initial(driver):
    driver.get(LINK)
    expected_title = "The Internet"
    actual = driver.title
    assert expected_title == actual, "Error, unexpected title!"


def test_right_click_and_get_alert_text(driver):
    driver.get(LINK)
    source = (By.XPATH, '//*[@id="hot-spot"]')
    ActionChains(driver).context_click(driver.find_element(*source)).perform()
    alert = driver.switch_to.alert
    assert alert.text == "You selected a context menu", "Error,unxpected message"
    alert.accept()
    sleep(2)


def test_get_href(driver):
    driver.get(LINK)
    expected_href = "http://elementalselenium.com/"
    actual = driver.find_element(By.CSS_SELECTOR, "#page-footer > div > div > a").get_attribute('href')
    assert expected_href == actual, "Error, Unexpected href attribute"

