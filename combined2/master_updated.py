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

def init_objects(bnm):
    #declare objects
    lin = gnc.Login(bnm)         #login obj
    nav = gnc.Navigate(bnm)      #navigate obj
    tr = gnc.Trans(bnm)            #transaction obj
    lout = gnc.Logout(bnm)       #logout obj
    return lin, nav, tr, lout

def main():
    bnm = input("enter bankname : ")
    uname = input("enter username : ")
    pwd = input("enter password : ")
    form = input("enter format (json, csv, xml) : ")
    account_detail={}

    lin, nav, tr, lout = init_objects(bnm) # Getting Login, Navigator, Transaction and Logout objects

    #Doing Login and Validating it
    page=lin.login(bnm, uname, pwd)
    vtr.valid_page(bnm,page)

    #Discovering accounts
    page_source=nav.navigate_transaction(bnm)   #Navigation
    account_detail.update(asum.scrape_summary(bnm, page_source)) #account num and balance as Dictionary


    #Navigating and parsing transactions
    for account in account_detail.keys():
        page_source1=tr.transaction_history(bnm,account)             #transaction
        account_detail[account].append(htmpr.parse_html(form, page_source1))

    #Logging out
    lout.logout(bnm)
    print(account_detail)

if __name__ == "__main__": main()
