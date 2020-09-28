# Selenium test: visit twitter site, fill all fields and advance to number verification step,
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
            "https://www.medicalwebexperts.com/")
        time.sleep(5)
        self.driver.find_element_by_xpath("(//div[@class='container-fluid']//..//a[@class='dropdown-toggle'])[1]").click()
        self.driver.find_element_by_xpath("(//div[@class='container-fluid']//..//a[@class='dropdown-toggle'])[1]").click()
        #self.driver.find_element_by_xpath("(//div[@class='container-fluid']//..//div[@class='service-box'])[1]").click()
        time.sleep(10)
        # //a[contains(text(), "Our Services")]
        self.driver.find_element_by_xpath("//*[@id='olark-wrapper']/button/div[2]").click()
        self.driver.find_element_by_xpath("//input[@placeholder='Enter your name...']").send_keys(self.persona2.nombre)
        self.driver.find_element_by_xpath("//input[@placeholder='Enter your email...']").send_keys(self.persona2.email)
        time.sleep(10)

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
