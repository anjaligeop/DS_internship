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
driver.get('https://www.online.citibank.co.in/products-services/online-services/internet-banking.htm')
parent = driver.current_window_handle
driver.find_element_by_link_text("LOGIN NOW").click()
child=driver.window_handles[1]
driver.switch_to.window(child)
driver.find_element_by_id("User_Id").click()
driver.find_element_by_id('User_Id').send_keys('USERNAME')
driver.find_element_by_id("skImg").click()
driver.find_element_by_id("password").click()
driver.find_element_by_id('password').send_keys('PWD')
driver.find_element_by_xpath("//div[@id='main-wrapper']/div/div[2]/div[2]/div/div/div[2]/div[3]/div/a/div").click()
index=2
driver.switch_to.frame(2)
driver.find_element_by_link_text("Credit Card").click()
driver.switch_to.default_content()
index=0
driver.switch_to.frame(0)
driver.find_element_by_id("3").click()
driver.switch_to.default_content()
index=2
driver.switch_to.frame(2)
driver.find_element_by_link_text("View account summary").click()
driver.switch_to.default_content()
index=0
driver.switch_to.frame(0)
driver.find_element_by_id("224").click()
driver.switch_to.default_content()
index=2
driver.switch_to.frame(2)
driver.find_element_by_link_text("View Account Summary").click()
driver.switch_to.default_content()
index=0
driver.switch_to.frame(0)
driver.find_element_by_id("8").click()
driver.find_element_by_id("cboMenu").click()
Select(driver.find_element_by_id("cboMenu")).select_by_visible_text("Take me directly to...")
driver.find_element_by_id("cboMenu").click()
driver.switch_to.default_content()
index=2
driver.switch_to.frame(2)
driver.find_element_by_link_text("Insurance").click()
driver.find_element_by_link_text("View Account Summary").click()
driver.switch_to.default_content()
index=3
time.sleep(3)
driver.switch_to.frame(3)
driver.find_element_by_id("im012").click()
driver.find_element_by_xpath("//div[@id='box02']/table/tbody/tr[2]/td/a/font").click()
Select(driver.find_element_by_id("select2")).select_by_visible_text("PDF file")
driver.find_element_by_id("select2").click()
Select(driver.find_element_by_id("select2")).select_by_visible_text("CSV file")
Select(driver.find_element_by_id("select2")).select_by_visible_text("XLS file")
driver.switch_to.default_content()
index=0
driver.switch_to.frame(0)
driver.find_element_by_link_text("Sign out").click()
