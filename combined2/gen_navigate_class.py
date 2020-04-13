from selenium import webdriver
import re
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import driverfile as dfr    #configuration file
import config as cfg        #configuration file


def download_html(name,driver):
    a = driver.page_source
    file_nm = open('/home/anjaligeorgep/Desktop/download_html{}'.format(name), 'w')
    file_nm.write(a)


class Driver_ini():
        driver = eval(cfg.webdriver_path["chrome"])



class Login(Driver_ini): #extending Driver_ini class
    def __init__(self,bankname):
        self.bankname = bankname

    def login(self,bankname,uname,pwd):
        driver = (Driver_ini.driver)
        driver.get(cfg.bank_url[bankname])
        time.sleep(2)

        #vtr.login_validator(bankname)

        if bankname.upper() == "CITI":
            eval(dfr.findElement(cfg.login_id[bankname]["loginbtn"])).click()
            child = driver.window_handles[1]
            driver.switch_to.window(child)
        eval(dfr.findElement(cfg.login_id[bankname]["userid"])).click()
        eval(dfr.findElement(cfg.login_id[bankname]["userid"])).send_keys(uname) #user name to be entered
        if bankname.upper() == "CITI":
            eval(dfr.findElement(cfg.login_id[bankname]["keyboardid"])).click()
        eval(dfr.findElement(cfg.login_id[bankname]["pwid"])).click()
        eval(dfr.findElement(cfg.login_id[bankname]["pwid"])).send_keys(pwd) #password to be entered
        #if bankname.upper()=="CANARA":
            #eval(dfr.findElement(cfg.login_id[bankname]["captchaid"])).click()
            #a = input("captcha?")
            #eval(dfr.findElement(cfg.login_id[bankname]["captchaid"])).send_keys(a)
        time.sleep(4)
        eval(dfr.findElement(cfg.login_id[bankname]["clicklogin"])).click()
        if bankname.upper()=="CANARA":
            child = driver.window_handles[1]
            driver.switch_to.window(child)
            time.sleep(2)

        return driver.page_source


class Logout(Driver_ini):
    def __init__(self,bankname):
        self.bankname = bankname

    def logout(self,bankname):
        driver =(Driver_ini.driver)
        if bankname.upper()=="FEDERAL":
            eval(dfr.findElement(cfg.logout_id[bankname]["logoutnav"])).click()
            eval(dfr.findElement(cfg.logout_id[bankname]["logoutbtn"])).click()
            driver.close()
        elif bankname.upper()=="CITI":
            time.sleep(2)
            driver.switch_to.frame(0)
            eval(dfr.findElement(cfg.logout_id[bankname]["logoutbtn"])).click()
            driver.close()
        elif bankname.upper()=="CANARA":
            time.sleep(5)
            driver.switch_to.frame(0)
            eval(dfr.findElement(cfg.logout_id[bankname]["logoutbtn"])).click()
            driver.switch_to.default_content()
            driver.close()

class Navigate(Driver_ini):
    def __init__(self,bankname):
        self.bankname = bankname

    def navigate_transaction(self,bankname):
        driver = (Driver_ini.driver)
        dropdown=[]
        if bankname.upper()=="FEDERAL":
            # account summary
            eval(dfr.findElement(cfg.navigate_id[bankname]["accid"])).click()
            eval(dfr.findElement(cfg.navigate_id[bankname]["all_accid"])).click()
            page_source=driver.page_source           #get the page source and return it to master

        elif bankname.upper()=="CITI":
            #account summary
            time.sleep(3)
            driver.switch_to.frame(2)
            eval(dfr.findElement(cfg.navigate_id[bankname]["click0"])).click()
            driver.switch_to.default_content()
            time.sleep(5)
            driver.switch_to.frame(3)
            eval(dfr.findElement(cfg.navigate_id[bankname]["clickA"])).click()
            eval(dfr.findElement(cfg.navigate_id[bankname]["clickB"])).click()
            eval(dfr.findElement(cfg.navigate_id[bankname]["clickC"])).click()
            page_source = driver.page_source
            driver.switch_to.default_content()

        elif bankname.upper()=="CANARA":
            time.sleep(10)
            driver.switch_to.frame(1)
            eval(dfr.findElement(cfg.navigate_id[bankname]["click0"])).click()
            driver.switch_to.default_content()
            time.sleep(10)
            driver.switch_to.frame(4)
            select_box = eval(dfr.findElement(cfg.navigate_id[bankname]["click4"]))
            options = [x for x in select_box.find_elements_by_tag_name("option")]

            for element in options:
                # print(element.get_attribute("value"))
                dropdown.append(element.get_attribute("value"))
            dropdown = dropdown[1:]

            x = 0
            for val in dropdown:  # store the page contents for each acc num
                Select(eval(dfr.findElement(cfg.navigate_id[bankname]["click4"]))).select_by_value(val)
                eval(dfr.findElement(cfg.navigate_id[bankname]["click5"])).click()
                time.sleep(2)
                page_source=driver.page_source
                x=x+1
            driver.switch_to.default_content()

        return page_source


class Trans(Driver_ini):
    def __init__(self,bankname):
        self.bankname=bankname
    def transaction_history(self,bankname,account):
        driver = (Driver_ini.driver)

        if bankname.upper() == "FEDERAL":
            eval(dfr.findElement(cfg.transaction_id[bankname]["click0"])).click()
            eval(dfr.findElement(cfg.transaction_id[bankname]["click1"])).click()
            eval(dfr.findElement(cfg.transaction_id[bankname]["click2"])).click()
            eval(dfr.findElement(cfg.transaction_id[bankname]["click3"])).click()
            eval(dfr.findElement(cfg.transaction_id[bankname]["click4"])).send_keys(account)
            eval(dfr.findElement(cfg.transaction_id[bankname]["click5"])).click()
            driver.execute_script(
                'document.getElementById("TransactionHistoryFG.FROM_TXN_DATE").removeAttribute("readonly")')
            eval(dfr.findElement(cfg.transaction_id[bankname]["dateFrom"])).clear()
            eval(dfr.findElement(cfg.transaction_id[bankname]["dateFrom"])).send_keys("01-12-2019")
            driver.execute_script(
                'document.getElementById("TransactionHistoryFG.TO_TXN_DATE").removeAttribute("readonly")')
            eval(dfr.findElement(cfg.transaction_id[bankname]["dateTo"])).clear()
            eval(dfr.findElement(cfg.transaction_id[bankname]["dateTo"])).send_keys("01-01-2020")
            eval(dfr.findElement(cfg.transaction_id[bankname]["click6"])).click()
            page_source1 = driver.page_source




        elif bankname.upper() == "CANARA":
            time.sleep(10)
            driver.switch_to.frame(4)

            select = eval(dfr.findElement(cfg.transaction_id[bankname]["click0"]))
            option = select.find_element_by_xpath('.//option[contains(@value, "{}")]'.format(account))
            option.click()

            eval(dfr.findElement(cfg.transaction_id[bankname]["click0"])).click()
            eval(dfr.findElement(cfg.transaction_id[bankname]["click1"])).click()
            eval(dfr.findElement(cfg.transaction_id[bankname]["click2"])).click()

            Select(eval(dfr.findElement(cfg.transaction_id[bankname]["click3"]))).select_by_visible_text(
                "Specify Period")
            # enter date
            time.sleep(3)
            eval(dfr.findElement(cfg.transaction_id[bankname]["dateFrom"])).click()
            eval(dfr.findElement(cfg.transaction_id[bankname]["dateFrom"])).send_keys('01-01-2020')
            eval(dfr.findElement(cfg.transaction_id[bankname]["dateTo"])).clear()
            eval(dfr.findElement(cfg.transaction_id[bankname]["dateTo"])).send_keys("30-03-2020")
            eval(dfr.findElement(cfg.transaction_id[bankname]["click1"])).click()
            time.sleep(2)
            page_source1 = driver.page_source
            driver.switch_to.default_content()



        elif bankname.upper() == "CITI":
            driver.switch_to.frame(0)
            time.sleep(5)
            eval(dfr.findElement(cfg.transaction_id[bankname]["click0"])).click()
            driver.switch_to.default_content()
            time.sleep(5)
            driver.switch_to.frame(2)
            eval(dfr.findElement(cfg.transaction_id[bankname]["click1"])).click()
            driver.switch_to.default_content()
            time.sleep(5)
            driver.switch_to.frame(3)
            eval(dfr.findElement(cfg.transaction_id[bankname]["click2"])).click()
            time.sleep(3)
            driver.find_element_by_partial_link_text(account).click()
            Select(eval(dfr.findElement(cfg.transaction_id[bankname]["click3"]))).select_by_visible_text("Date Range")
            driver.execute_script('document.getElementsByName("textfield4")[0].removeAttribute("readonly")')
            eval(dfr.findElement(cfg.transaction_id[bankname]["dateFrom"])).clear()
            eval(dfr.findElement(cfg.transaction_id[bankname]["dateFrom"])).send_keys("01/01/2020")
            driver.execute_script('document.getElementsByName("textfield5")[0].removeAttribute("readonly")')
            eval(dfr.findElement(cfg.transaction_id[bankname]["dateTo"])).clear()
            eval(dfr.findElement(cfg.transaction_id[bankname]["dateTo"])).send_keys("30/03/2020")
            eval(dfr.findElement(cfg.transaction_id[bankname]["click4"])).click()
            time.sleep(3)
            page_source1 = driver.page_source
            driver.switch_to.default_content()
            time.sleep(3)

        return  page_source1




