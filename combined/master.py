from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import driverfile as dfr    #configuration file
import config as cfg        #configuration file
import gen_navigate_class as gnc
import html_parser as htmpr


if __name__=="__main__":
    try:
        bnm = input("enter bankname : ")
        uname = input("enter username : ")
        pwd = input("enter password : ")
        form=input("enter format (json, csv, xml) : ")

        lin = gnc.Login(bnm)
        nav = gnc.Navigate(bnm)
        lout = gnc.Logout(bnm)

        lin.login(bnm, uname, pwd)
        nav.navigate_transaction(bnm)
        lout.logout(bnm)

        formats = ["csv", "json", "xml"]
        if form not in formats:     #parsing transaction details
            form="csv"
        if bnm.upper()=="FEDERAL":
            htmpr.fed_html(form)
        elif bnm.upper()=="CITI":
            htmpr.citi_html(form)
        elif bnm.upper()=="CANARA":
            htmpr.canara_html(form)

    except Exception as e:
        print("**ERROR**")
        print(e.__doc__)
