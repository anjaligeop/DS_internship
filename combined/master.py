from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import driverfile as dfr    #configuration fil
import gen_navigate_class as gnc
import html_parser as htmpr
import account_summary as asum

try:
    bnm = input("enter bankname : ")
    uname = input("enter username : ")
    pwd = input("enter password : ")
    form = input("enter format (json, csv, xml) : ")

    #declare objects
    lin = gnc.Login(bnm)
    nav = gnc.Navigate(bnm)     #gets account summary
    tr=gnc.Trans(bnm)		#gets transaction 
    lout = gnc.Logout(bnm)

    lin.login(bnm, uname, pwd)                    #carry out login
    accounts=nav.navigate_transaction(bnm)   ##dropdown values in case of canara & fed, account summary html files have been saved



    if bnm.upper() == "FEDERAL":
        account_num=asum.acc_fed() #account_summary.py executed that returns  account numbers
    elif bnm.upper() == "CITI":
        account_num=asum.acc_citi()

    elif bnm.upper() == "CANARA":
        account_num=asum.acc_canara()

    tr.transaction_history(bnm,accounts,account_num)
    lout.logout(bnm)



    formats = ["csv", "json", "xml"]
    if form not in formats:  # parsing transaction details
        form = "csv"
    if bnm.upper() == "FEDERAL":
        htmpr.fed_html(form)
    elif bnm.upper() == "CITI":
        htmpr.citi_html(form)
    elif bnm.upper() == "CANARA":
        htmpr.canara_html(form)




except Exception as e:
    print("**ERROR**")
    print(e.__doc__)
