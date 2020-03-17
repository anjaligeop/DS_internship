from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import driverfile as dfr    #configuration file
import config as cfg        #configuration file


def download_html(bankname,driver):
    a = driver.page_source
    file_nm = open('/home/anjaligeorgep/Desktop/download_html/file_{}.html'.format(bankname), 'w')
    file_nm.write(a)


class Driver_ini:
    def get_driver(self):
        driver_path = cfg.webdriver_path["chrome"]
        self.driver = eval(driver_path)
        return self.driver



class Navigate():
    def __init__(self,bankname):
        self.bankname = bankname

    def login(self,bankname,driver):
        driver.get(cfg.bank_url[bankname])
        if bankname.upper() == "CITI":
            eval(dfr.findElement(cfg.login_id[bankname]["loginbtn"])).click()
            child = driver.window_handles[1]
            driver.switch_to.window(child)
        eval(dfr.findElement(cfg.login_id[bankname]["userid"])).click()
        eval(dfr.findElement(cfg.login_id[bankname]["userid"])).send_keys('username') #user name to be entered
        if bankname.upper() == "CITI":
            eval(dfr.findElement(cfg.login_id[bankname]["keyboardid"])).click()
        eval(dfr.findElement(cfg.login_id[bankname]["pwid"])).click()
        eval(dfr.findElement(cfg.login_id[bankname]["pwid"])).send_keys("pwd") #password to be entered
        if bankname.upper()=="CANARA":
            eval(dfr.findElement(cfg.login_id[bankname]["captchaid"])).click()
            a = input("captcha?")
            eval(dfr.findElement(cfg.login_id[bankname]["captchaid"])).send_keys(a)
        eval(dfr.findElement(cfg.login_id[bankname]["clicklogin"])).click()
        if bankname.upper()=="CANARA":
            child = driver.window_handles[1]
            driver.switch_to.window(child)

    def logout(self,bankname,driver):
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
            driver.close()

    def navigate_transaction(self,bankname,driver):
        if bankname.upper()=="FEDERAL":
            eval(dfr.findElement(cfg.navigate_id[bankname]["click0"])).click()
            eval(dfr.findElement(cfg.navigate_id[bankname]["click1"])).click()
            eval(dfr.findElement(cfg.navigate_id[bankname]["click2"])).click()
            eval(dfr.findElement(cfg.navigate_id[bankname]["click3"])).click()
            #click on download in pdf format
            download_html("federal",driver)

        elif bankname.upper()=="CITI":
            time.sleep(3)
            driver.switch_to.frame(2)
            eval(dfr.findElement(cfg.navigate_id[bankname]["click0"])).click()
            driver.switch_to.default_content()
            time.sleep(3)
            driver.switch_to.frame(3)
            eval(dfr.findElement(cfg.navigate_id[bankname]["click1"])).click()
            eval(dfr.findElement(cfg.navigate_id[bankname]["click2"])).click()
            download_html("citi",driver)
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
            download_html("canara",driver)
            driver.switch_to.default_content()
            #click on download in req format

if __name__=="__main__":
    try:
        bnm = "federal"     #input("enter bankname")
        dr = Driver_ini()
        driver = dr.get_driver()

        n = Navigate(bnm)
        n.login(bnm, driver)
        n.navigate_transaction(bnm, driver)
        n.logout(bnm, driver)





    except Exception as e:
        print("**ERROR**")
        print(e.__doc__)




