from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="/home/anjaligeorgep/Desktop/perfios/chromedriver")
driver.implicitly_wait(10)
driver.get('https://netbanking.canarabank.in/entry/ENULogin.jsp?')
parent = driver.current_window_handle
driver.find_element_by_id("fldLoginUserId").click()
driver.find_element_by_id('fldLoginUserId').send_keys('USER NAME')
driver.find_element_by_id("fldPassword").click()
driver.find_element_by_id('fldPassword').send_keys('PASSWORD')
driver.find_element_by_id("fldcaptcha").click()
a=input("Enter captcha: ") #manually enter captcha
driver.find_element_by_id('fldcaptcha').send_keys(a)
driver.find_element_by_xpath("//input[@value='SIGN IN']").click()
child=driver.window_handles[1]

driver.switch_to.window(child)
index=1
time.sleep(5)
driver.switch_to.frame(1)
driver.find_element_by_id("grpspan_A_A07").click()
driver.find_element_by_id("RRASMlink").click()
driver.switch_to.default_content()
index=4
time.sleep(5)
driver.switch_to.frame(4)
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.find_element_by_xpath("//table[@id='graphtable']/tbody/tr[3]/td/div[2]").click()
time.sleep(5)

driver.find_element_by_xpath("//*[@id='infoBox']/div[3]").click()
Select(driver.find_element_by_id("fldsearchformat")).select_by_visible_text("PDF Format")
driver.find_element_by_id("fldsearchformat").click()
driver.switch_to.default_content()
index=0
time.sleep(5)
driver.switch_to.frame(0)
driver.find_element_by_link_text("Invest & Insure").click()
driver.find_element_by_link_text("Logout").click()
driver.switch_to.default_content()
driver.find_element_by_name("fldSubmit").click()

