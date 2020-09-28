import unittest
import time
from selenium import webdriver
from functions import persona


class FourthTest(unittest.TestCase):

    def setUp(self):

        self.persona1 = persona.persona1
        self.persona1.passwd = '132456dni'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_004(self):

        self.driver.get(
            "https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
        self.driver.find_element_by_id("firstName").clear()
        self.driver.find_element_by_id("firstName").send_keys(self.persona1.nombre)

        self.driver.find_element_by_id("lastName").send_keys(self.persona1.apellido)
        self.driver.find_element_by_xpath("//INPUT[@id='lastName']").clear()
        self.driver.find_element_by_xpath("//INPUT[@id='lastName']").send_keys(self.persona1.apellido)

        self.driver.find_element_by_name("Username").clear()
        self.driver.find_element_by_name("Username").send_keys(self.persona1.email)

        self.driver.find_element_by_xpath("//div//..//input[@name='Passwd']")\
            .clear()
        self.driver.find_element_by_xpath("//div//..//input[@name='Passwd']").send_keys(self.persona1.passwd)

        self.driver.find_element_by_name("ConfirmPasswd").send_keys(self.persona1.passwd)

        self.driver.find_element_by_xpath("//*[@id='accountDetailsNext']").click()

        time.sleep(1)

        text = self.driver.find_element_by_xpath("//*[@id='headingText']/span").text
        assert text == "Verificar tu número", "Error"

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
