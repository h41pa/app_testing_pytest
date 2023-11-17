"""
Pentru autocomplete pentru metodele Webdriver in cadrul claselor in pages
trebuie sa te asigura ca instanta self.driver este de tip WebDriver , si nu este necesar sa configurezi fisier
pentru driver , doar folosing BDD  trebuie

from selenium.webdriver.remote.webdriver import WebDriver
si dupa initializeaza in clasa

class Name:

    def __init__(self, driver: WebDriver):
        self.driver = driver


~~~~~~~ Pentru configurare driver deschidere pagina:  #####


##### pentru folosirea driverului din alt fisier conftest :  #####
-cream conftest.py
- care are @pytest.fixture ca decorator deasupra de definirea driverului.
- in fisierele test ne asiguram ca avem urmatoarea sintaxa
@pytest.mark.usefixtures("browser") - folosim decoratorul pentru a aplica fixture-ul browser , dupa importuri punem asta
  - nu mai este necesar sa specificam browser in def doar in pagina pentru ca are nevoie de driver pentru a deschide


def test_autentificare_corecta(browser):  # browser cara param daca vrei metodele webdriver
    # Aici putem folosi browser fără a-l adăuga ca parametru
    pagina = PaginaAutentificare(browser)
    pagina.deschide_pagina()
    pagina.introdu_username("tomsmith")
    pagina.introdu_parola("SuperSecretPassword!")
    pagina.apasa_autentificare()

    assert "You logged into a secure area!" in browser.page_source


##### cand configuram driver in fiecare fisier intern din test. exemplu #####

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

"""