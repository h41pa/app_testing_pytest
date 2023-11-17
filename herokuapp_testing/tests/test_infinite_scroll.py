import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

LINK = "https://the-internet.herokuapp.com/infinite_scroll"
ELEMENTS = (By.CLASS_NAME, "jscroll-added")


def test_initial_element_loading(driver):
    driver.get(LINK)
    initial_elements = driver.find_elements(*ELEMENTS)
    assert len(initial_elements) > 0, "nothing loaded"


def test_infinite_scroll_loading(driver):
    driver.get(LINK)
    initial_count = len(driver.find_elements(*ELEMENTS))

    for i in range(3):
        ActionChains(driver).send_keys(Keys.END).perform()
        time.sleep(2)

    new_count = len(driver.find_elements(*ELEMENTS))
    assert new_count > initial_count, "Error, Page didn't scroll"
    print(new_count, initial_count)


def test_performance_on_infinite_scroll(driver):
    driver.get(LINK)
    # Găsește numărul inițial de elemente
    initial_elements = driver.find_elements(*ELEMENTS)
    initial_count = len(initial_elements)
    # Începe să măsoare timpul
    start_time = time.time()
    # Simulează scroll în jos de mai multe ori
    for i in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    # Oprește măsurarea timpului
    end_time = time.time()
    eclapsed_time = end_time - start_time
    new_elements = driver.find_elements(*ELEMENTS)
    new_count = len(new_elements)

    assert new_count > initial_count , "Error"
    assert eclapsed_time < 10.0
