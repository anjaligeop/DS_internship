from selenium import webdriver
from bs4 import BeautifulSoup
import os
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="/home/anjaligeorgep/Desktop/perfios/chromedriver")
driver.implicitly_wait(20)
driver.get('https://www.fednetbank.com/corp/AuthenticationController?__START_TRAN_FLAG__=Y&FORMSGROUP_ID__=AuthenticationFG&__EVENT_ID__=LOAD&FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=1&BANK_ID=049&LANGUAGE_ID=001')
driver.find_element_by_id("AuthenticationFG.USER_PRINCIPAL").click()
driver.find_element_by_id('AuthenticationFG.USER_PRINCIPAL').send_keys('USER-NAME')
driver.find_element_by_id("AuthenticationFG.ACCESS_CODE").click()
driver.find_element_by_id('AuthenticationFG.ACCESS_CODE').send_keys('PASSWORD')
driver.find_element_by_id("VALIDATE_CREDENTIALS").click()
driver.find_element_by_xpath("//div[@id='header-nav']/ul/li[5]/a/span/b").click()
driver.find_element_by_id("HREF_Logout").click()
