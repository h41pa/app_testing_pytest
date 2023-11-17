import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# @pytest.fixture(scope="module") # definit o singura data pt toate modulele
# @pytest.fixture  # this allow to use the browser method(test configuration)
# def browser():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.implicitly_wait(6)
#     yield driver
#     driver.quit()

"""
TIPURI DE @pytest.fixture(scope=""):

 --- @pytest.fixture(scope="function") --- 
"function" (implicit): Aceasta este acoperirea implicită a fiecărei fixture. 
O astfel de fixture este inițializată înaintea fiecărei funcții de testare (funcția de test) 
și distrusă după încheierea funcției respective. 
Acesta este cel mai des utilizat scope.
import pytest

@pytest.fixture(scope="function")
def my_fixture():
    return "Some data"

def test_example_1(my_fixture):
    assert my_fixture == "Some data"

def test_example_2(my_fixture):
    assert my_fixture == "Some data"


--- @pytest.fixture(scope="class")  ---

"class": Dacă doriți să împărtășiți o fixture între mai multe funcții de test din aceeași clasă, 
puteți utiliza scope="class". Fixture-ul va fi inițializat o singură dată pentru întreaga clasă de teste 
și distrus după ce ultima funcție de test din acea clasă s-a încheiat.
import pytest

@pytest.fixture(scope="class")
def shared_fixture():
    return "Shared data"

class TestClass:
    def test_example_1(self, shared_fixture):
        assert shared_fixture == "Shared data"

    def test_example_2(self, shared_fixture):
        assert shared_fixture == "Shared data"
        
        
 --- @pytest.fixture(scope="module") --- 
"module": Cu scope="module", fixture-ul este inițializat o singură dată pentru întreaga module (fișier Python) 
care conține funcțiile de test care utilizează acea fixture.
import pytest

@pytest.fixture(scope="module")
def module_fixture():
    return "Module-level data"

def test_example_1(module_fixture):
    assert module_fixture == "Module-level data"

def test_example_2(module_fixture):
    assert module_fixture == "Module-level data"

 --- @pytest.fixture(scope="session") ---
 
"session": Un fixture cu scope="session" este inițializat o singură dată pentru întreaga sesiune de testare. 
Fixture-ul este disponibil pentru toate modulele și clasele de teste din întreaga sesiune. 
Acesta este util pentru a partaja resurse costisitoare între teste.
import pytest

@pytest.fixture(scope="session")
def session_fixture():
    return "Session-level data"

def test_example_1(session_fixture):
    assert session_fixture == "Session-level data"

def test_example_2(session_fixture):
    assert session_fixture == "Session-level data"


"""