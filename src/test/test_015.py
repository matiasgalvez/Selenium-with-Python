
import unittest
import time
from pages.spotify import Registro as Spoty_registro
from functions.persona import Persona
from selenium import webdriver
from selenium.webdriver.common.by import By


horaGlobal = time.strftime("%H%M%S")


class Test_019(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.persona1 = Persona("Matias", "Galvez", 37500685, "mattg1515@gmail.com")

        self.driver.get("https://www.spotify.com/ar/signup/?forward_url=https%3A%2F%2Fwww.spotify.com%2Far%2Fdownload%2F")


    def test_019(self):
        self.driver.find_element(By.XPATH, Spoty_registro.txt_email_xpath).clear()
        self.driver.find_element(By.XPATH, Spoty_registro.txt_email_xpath).send_keys(self.persona1.email)

        self.driver.find_element(By.XPATH, Spoty_registro.txt_email_confirm_xpath).clear()
        self.driver.find_element_by_xpath(Spoty_registro.txt_email_confirm_xpath).send_keys(self.persona1.email)

        title = "Test_017"
        self.driver.get_screenshot_as_file(f"../data/screenshots/{title}-{horaGlobal}.png")

        time.sleep(10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
