from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import driverfile as dfr
import config as cfg

driver_path = cfg.webdriver_path["chrome"]
driver=eval(driver_path)

def login(bankname):
    driver.get(cfg.bank_url[bankname])
    if bankname.upper() == "CITI":
        eval(dfr.findElement(cfg.login_id[bankname]["loginbtn"])).click()
        child = driver.window_handles[1]
        driver.switch_to.window(child)
    eval(dfr.findElement(cfg.login_id[bankname]["userid"])).click()
    eval(dfr.findElement(cfg.login_id[bankname]["userid"])).send_keys('username') 
    if bankname.upper() == "CITI":
        eval(dfr.findElement(cfg.login_id[bankname]["keyboardid"])).click()
    eval(dfr.findElement(cfg.login_id[bankname]["pwid"])).click()
    eval(dfr.findElement(cfg.login_id[bankname]["pwid"])).send_keys('pwd') 
    if bankname.upper()=="CANARA":
        eval(dfr.findElement(cfg.login_id[bankname]["captchaid"])).click()
        a = input("captcha?")
        eval(dfr.findElement(cfg.login_id[bankname]["captchaid"])).send_keys(a)
    eval(dfr.findElement(cfg.login_id[bankname]["clicklogin"])).click()
    if bankname.upper()=="CANARA":
        child = driver.window_handles[1]
        driver.switch_to.window(child)
def logout(bankname):
    if bankname.upper()=="FEDERAL":
        eval(dfr.findElement(cfg.logout_id[bankname]["logoutnav"])).click()
        eval(dfr.findElement(cfg.logout_id[bankname]["logoutbtn"])).click()
        driver.close()
    elif bankname.upper()=="CITI":
        driver.switch_to.frame(0)
        eval(dfr.findElement(cfg.logout_id[bankname]["logoutbtn"])).click()
        driver.close()
    elif bankname.upper()=="CANARA":
        time.sleep(5)
        driver.switch_to.frame(0)
        eval(dfr.findElement(cfg.logout_id[bankname]["logoutbtn"])).click()
        driver.switch_to.default_content()
        eval(dfr.findElement(cfg.logout_id[bankname]["closewindow"])).click()

def download_html(bankname):
    a=driver.page_source
    file_nm = open('/home/anjaligeorgep/Desktop/download_html/file_{}.html'.format(bankname), 'w')
    file_nm.write(a)

def navigate_transaction(bankname):
    if bankname.upper()=="FEDERAL":
        eval(dfr.findElement(cfg.navigate_id[bankname]["click0"])).click()
        eval(dfr.findElement(cfg.navigate_id[bankname]["click1"])).click()
        eval(dfr.findElement(cfg.navigate_id[bankname]["click2"])).click()
        eval(dfr.findElement(cfg.navigate_id[bankname]["click3"])).click()
        #click on download in pdf format
        download_html("federal")
    elif bankname.upper()=="CITI":
        time.sleep(3)
        driver.switch_to.frame(2)
        eval(dfr.findElement(cfg.navigate_id[bankname]["click0"])).click()
        driver.switch_to.default_content()
        time.sleep(3)
        driver.switch_to.frame(3)
        eval(dfr.findElement(cfg.navigate_id[bankname]["click1"])).click()
        eval(dfr.findElement(cfg.navigate_id[bankname]["click2"])).click()
        download_html("citi")
        driver.switch_to.default_content()
        #click on download in pdf format

    elif bankname.upper()=="CANARA":
        time.sleep(5)
        driver.switch_to.frame(1)
        eval(dfr.findElement(cfg.navigate_id[bankname]["click0"])).click()
        eval(dfr.findElement(cfg.navigate_id[bankname]["click1"])).click()
        driver.switch_to.default_content()
        time.sleep(5)
        driver.switch_to.frame(4)
        eval(dfr.findElement(cfg.navigate_id[bankname]["click2"])).click()
        eval(dfr.findElement(cfg.navigate_id[bankname]["click3"])).click()  #account detail(wrong xpath generated")
        download_html("canara")
        driver.switch_to.default_content()
        #click on download in req format

if __name__=="__main__":
    bnm="federal"
    login(bnm)
    navigate_transaction(bnm)
    logout(bnm)
