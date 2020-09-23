from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_id("id-search-field")
elem.clear()
elem.send_keys("pycon")
donate_btn = driver.find_element_by_xpath("//a[@class='donate-button']")
donate_btn.click()
assert "PSF" in driver.title
driver.close()