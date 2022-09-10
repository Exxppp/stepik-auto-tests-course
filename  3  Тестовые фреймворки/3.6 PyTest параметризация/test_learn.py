import time
import math
import pytest
from selenium.webdriver.common.by import By

list_link = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]


class TestStepik:
    text = ""

    @pytest.mark.parametrize("link", list_link)
    def test_correct(self, browser, link):
        browser.implicitly_wait(5)
        browser.get(link)
        input_value = browser.find_element(By.CSS_SELECTOR, ".textarea")
        answer = math.log(int(time.time()))
        input_value.send_keys(str(answer))
        browser.find_element(By.CLASS_NAME, "submit-submission").click()
        text = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
        if text != "Correct!":
            TestStepik.text += text

    def test_print(self):
        print(TestStepik.text)
