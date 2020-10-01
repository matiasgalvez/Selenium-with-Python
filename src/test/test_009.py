# Selenium test: visit mercadolibre site, use of EC and explicit waits

import unittest
import time
from selenium import webdriver
from functions import persona
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages import mercadolibre


class NinthTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.mercadolibre = mercadolibre.Mercadolibre

    def test_009(self):

        self.driver.get(
            "https://www.mercadolibre.com.ar")

        localizador1 = self.driver.find_element(By.XPATH, self.mercadolibre.menu_categorias_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(localizador1)
        action.perform()

        localizador2 = self.driver.find_element(By.XPATH, self.mercadolibre.menu_tecnologia_xpath)
        action.move_to_element(localizador2)
        action.perform()
        time.sleep(5)

        localizador3 = self.driver.find_element(By.XPATH, self.mercadolibre.menu_tvs_xpath)
        localizador3.click()

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
