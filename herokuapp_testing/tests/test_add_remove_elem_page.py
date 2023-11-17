import time
from herokuapp_testing.pages.add_remove_elements_page import AddRemoveElementsPage


def test_add_element(driver):
    add_remove = AddRemoveElementsPage(driver)
    add_remove.load_page()
    add_remove.click_add_button(1)
    assert add_remove.is_delete_button_displayed(), "Delete button not Displayed"

def test_add_remove_element(driver):
    add_remove = AddRemoveElementsPage(driver)
    add_remove.load_page()
    add_remove.click_add_button(2)
    time.sleep(2)
    assert add_remove.get_number_of_delete_buttons() == 2, "There are more or less than 2 delete buttons"
    add_remove.click_delete_button()
    time.sleep(2)
    assert add_remove.get_number_of_delete_buttons() == 1, "There is more are less than 1 delete button"
    add_remove.click_delete_button()
    assert add_remove.get_number_of_delete_buttons() == 0, "Button is displayed on page"


def test_button_x8(driver):
    # Test if 8 delete buttons are displayed
    add_remove = AddRemoveElementsPage(driver)
    add_remove.load_page()
    add_remove.click_add_button(8)
    assert  add_remove.get_number_of_delete_buttons() == 8, "There are less or more than 8 buttons"
    # for i in range(0, 8):
    #     add_remove.click_add_button(1)
    # time.sleep(2)
    # assert len(driver.find_elements(*add_remove.DELETE_BUTTON)) == 8 ,"There are less or more than 8 buttons"

def test_page_title_is_correct(driver):
    add_remove = AddRemoveElementsPage(driver)
    add_remove.load_page()
    assert "Add/Remove Elements" == add_remove.get_title(), "Title Not Correct"


