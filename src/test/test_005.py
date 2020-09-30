# Selenium test: visit facebook site, fill all fields and advance to number verification step,
# asserting that a text in that step exists

import unittest
import time
from selenium import webdriver
from functions import persona
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class FifthTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.persona2 = persona.persona2
        self.persona2.passwd = '132456dni'

    def test_005(self):

        self.driver.get(
            "https://facebook.com")

        self.driver.find_element(By.ID, "u_0_2").click()

        time.sleep(1)

        self.driver.find_element(By.NAME, "firstname").clear()
        self.driver.find_element(By.NAME, "firstname").send_keys(self.persona2.nombre)

        self.driver.find_element(By.NAME, "lastname").clear()
        self.driver.find_element(By.NAME, "lastname").send_keys(self.persona2.apellido)

        self.driver.find_element(By.NAME, "reg_email__").clear()
        self.driver.find_element(By.NAME, "reg_email__").send_keys(self.persona2.email)

        self.driver.find_element(By.NAME, "reg_email_confirmation__").clear()
        self.driver.find_element(By.NAME, "reg_email_confirmation__").send_keys(self.persona2.email)

        self.driver.find_element(By.NAME, "reg_passwd__").clear()
        self.driver.find_element(By.NAME, "reg_passwd__").send_keys(self.persona2.passwd)

        day_options = Select(self.driver.find_element_by_id("day"))
        day_options.select_by_visible_text("15")

        month_options = Select(self.driver.find_element_by_id("month"))
        month_options.select_by_visible_text("sep")

        year_options = Select(self.driver.find_element_by_id("year"))
        year_options.select_by_visible_text("1993")

        self.driver.find_element_by_xpath("//input[@value='2']").click()
        time.sleep(5)

        self.driver.find_element_by_name("websubmit").click()
# //*[contains(@id, 'algo que quiero encontrar')]
    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
