# Selenium test: visit amazon.es site, go to about amazon.es and get a screenshot

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

hora = time.strftime("%H%M%S")

class TenthTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(
            "https://www.amazon.es")

    def test_010(self):

        time.sleep(5)

        localizador = self.driver.find_element(By.XPATH, "//a[contains(text(),'Sobre Amazon.es')]")
        self.driver.execute_script("arguments[0].click();", localizador)
        time.sleep(5)
        title = "Sobre Amazon"
        self.driver.get_screenshot_as_file(f"E:\SeleniumWithPython\src\data\screenshots\{title}-{hora}.png")

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
