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


class SeventhTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.persona2 = persona.persona2

    def test_007(self):

        self.driver.get(
            "https://www.mercadolibre.com.ar")
        self.element1 = "//*[@class='afip']"
        self.element2 = "//*[@class='a']"

        wait = WebDriverWait(self.driver, 30)
        wait.until((EC.element_to_be_clickable((By.XPATH, self.element1))), "Elemento no encontrado")

        try:
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.visibility_of_element_located((By.XPATH, self.element2)))

        except TimeoutException:
            print(f"El elemento {self.element2} no se ha encontrado")

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
