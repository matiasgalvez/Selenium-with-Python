# Selenium test: visit random site, open different windows and switch between them

import unittest
import time
from selenium import webdriver
from functions import persona
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class SixthTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_005(self):

        self.driver.get(
            "http://echoecho.com/htmllinks10.htm")
        self.enlace = self.driver.find_element_by_xpath("//span[contains(text(),'Go to Yahoo')]")
        self.enlace.click()
        time.sleep(5)

        self.windows = self.driver.window_handles

        print(self.windows)

        self.driver.switch_to.window(self.windows[0])

        time.sleep(5)

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
