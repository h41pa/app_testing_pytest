from herokuapp_testing.pages.dropdown_page import DropDown


def test_drop_down(driver):
    dropdown = DropDown(driver)
    dropdown.load_page()
    dropdown.select_option_1()
    assert dropdown.is_option_1_selected(), "Option 1 is not displayed"
    dropdown.select_option_2()
    assert dropdown.is_option_2_selected(), "Option 2 is not displayed"
