from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import driverfile as dfr    #configuration file
import gen_navigate_class as gnc
import html_parser as htmpr
import account_summary as asum
import validator as vtr
import output_generator as ogn
import json
import sys



def init_objects(bnm):
    driver = gnc.Driver_ini.init_driver()    
    lin = gnc.Login(bnm)         #login obj
    nav = gnc.Navigate(bnm)      #navigate obj
    tr = gnc.Trans(bnm)            #transaction obj
    lout = gnc.Logout(bnm)       #logout obj
    return driver, lin, nav, tr, lout

def main(argvs):
    try:
        jsonParams = argvs[0:]
        params = json.loads(jsonParams)
        bnm = params['bankName'] 
        uname = params['loginId'] 
        pwd = params['password'] 
        form = params['format']  #xml,json,csv
        account_detail={}	
	
        driver, lin, nav, tr, lout = init_objects(bnm) # Getting Login, Navigator, Transaction and Logout objects

        #Doing Login and Validating it
        print("login\n")
        page=lin.login(bnm, uname, pwd, driver) 
        vtr.valid_page(bnm,page)	
        
        #Discovering accounts
        
        page_source=nav.navigate_transaction(bnm, driver)   #Navigation
        print("Discovered accounts\n")
        
        time.sleep(1)
        print("Fetching account summary\n")
        account_detail.update(asum.scrape_summary(bnm, page_source)) #account summary
        
        #Navigating and parsing transactions
        for key in account_detail:
            print("fetching transactions\n")
            account_detail[key]['transactions'] = []

            page_source1=tr.transaction_history(bnm,account_detail[key]['accountSummary']['accountNumber'],driver)     #transaction


            account_detail[key]['transactions'] = htmpr.parse_html(bnm, page_source1)
            print("completed\n")
        
        
        #Logging out
        lout.logout(bnm,driver)
        print("logout successful\n")
        ogn.main(account_detail, form)

    except Exception as e:
        print("Exception occcurred - "+str(e))
    finally:
        time.sleep(5)
        driver.quit()
        time.sleep(2)
        sys.exit()

if __name__ == "__main__": main('{"bankName":"canara", "loginId":"71204880", "password":"Mybd060195","format":"json"}')






