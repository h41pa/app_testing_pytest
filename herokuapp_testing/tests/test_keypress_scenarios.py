from herokuapp_testing.pages.keypress_page import KeyPress


def test_check_if_enter_is_pressed(driver):
    keypress_page = KeyPress(driver)
    keypress_page.load_page()
    keypress_page.press_enter_key()
    assert "You entered: ENTER" in keypress_page.get_green_message(), "The ENTER key is not pressed"


def test_check_if_backspace_is_pressed(driver):
    keypress_page = KeyPress(driver)
    keypress_page.load_page()
    keypress_page.press_backspace_key()
    assert "You entered: BACK_SPACE" in keypress_page.get_green_message(), "Backspace key not working"

def test_check_if_delete_is_pressed(driver):
    keypress_page = KeyPress(driver)
    keypress_page.load_page()
    keypress_page.press_delete_key()
    assert "You entered: DELETE" in keypress_page.get_green_message(),"Delete key not working"

