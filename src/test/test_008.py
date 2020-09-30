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


class EigthTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.persona2 = persona.persona2

    def test_008(self):

        self.driver.get(
            "https://www.mercadolibre.com.ar")
        time.sleep(5)

        self.payments = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'payment-data-title')]")

        self.count = 0

        for self.pay in self.payments:
            resultado_esperado = ["Tarjeta de crédito", "Tarjeta de débito", "Efectivo", "Más medios de pago"]
            assert resultado_esperado[self.count] == self.pay.text, "No coinciden"
            self.count = self.count + 1

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
