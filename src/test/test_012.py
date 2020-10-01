# Selenium test: visit google site, use of selenium keys

import unittest
import time
from selenium import webdriver
from functions import persona
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TenthTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(
            "https://www.google.com.ar/")

    def test_010(self):

        time.sleep(5)

        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys("Curso...")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys(Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys(Keys.ENTER)

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
