import pytest
from z_Teorie.pages.pagina_model import PaginaAutentificare


# @pytest.mark.usefixtures("browser")  # Folosim fixture-ul browser din conftest.py

def test_autentificare_corecta(browser):
    pagina = PaginaAutentificare(browser)
    pagina.deschide_pagina()
    pagina.introdu_username("tomsmith")
    pagina.introdu_parola("SuperSecretPassword!")
    pagina.apasa_autentificare()


    assert "You logged into a secure area!" in browser.page_source
