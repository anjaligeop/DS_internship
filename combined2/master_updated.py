from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import driverfile as dfr    #configuration fil
import gen_navigate_class as gnc
import html_parser as htmpr
import account_summary as asum
import validator as vtr

def init_objects(bank_name):
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
    if bnm.upper() == "FEDERAL":
        account_detail.update(asum.acc_fed(page_source))  #account num and balance as Dictionary
        account_num=list(account_detail.keys())   #account number
    elif bnm.upper() == "CITI":
        account_detail.update(asum.acc_citi(page_source))
        account_num = list(account_detail.keys())
    elif bnm.upper() == "CANARA":
        account_detail.update(asum.acc_canara(page_source))
        account_num = list(account_detail.keys())
    print(account_detail)

    #Navigating and parsing transactions
    form='csv'
    for account in account_detail.keys():
        page_source1=tr.transaction_history(bnm,account)             #transaction
        if bnm.upper() == "FEDERAL":
            account_detail[account].append(htmpr.fed_html(form, page_source1))
        elif bnm.upper() == "CITI":
            account_detail[account].append(htmpr.citi_html(form, page_source1))
        elif bnm.upper() == "CANARA":
            account_detail[account].append(htmpr.canara_html(form, page_source1))

    #Logging out
    lout.logout(bnm)
    print(account_detail)

if __name__ == "__main__": main()