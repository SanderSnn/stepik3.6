import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button_is_present(browser):
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, "button[type='submit']").is_displayed()
    time.sleep(10)
