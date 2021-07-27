from selenium import webdriver
from selenium.webdriver import safari 
driver = Safari()
from selenium.webdriver.common.keys import keys
driver.get("https://www.google.com")
driver.find_element_by_name("q")
driver.send_Keys("RTS Labs")
driver.send_Keys(keys.Return)
driver.find_element_by_class("LC20lb DKV0Md")
