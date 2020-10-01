# Selenium test: visit mercadolibre site, use of EC and explicit waits

import unittest
import time
from selenium import webdriver
from functions import persona
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TenthTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(
            "https://www.amazon.es")

    def test_010(self):

        time.sleep(5)
        localizador = self.driver.find_element(By.XPATH, "//a[contains(text(),'Trabajar en Amazon')]")
        self.driver.execute_script("arguments[0].click();", localizador)
        time.sleep(10)

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
