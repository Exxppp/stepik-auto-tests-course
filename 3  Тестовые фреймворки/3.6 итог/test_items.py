from selenium.webdriver.common.by import By
import time


def test_find_btn_add_busket(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    assert browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    time.sleep(2)
