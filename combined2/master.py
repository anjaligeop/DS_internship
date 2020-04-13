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

bnm = input("enter bankname : ")
uname = input("enter username : ")
pwd = input("enter password : ")
form = input("enter format (json, csv, xml) : ")

#declare objects
lin = gnc.Login(bnm)         #login obj
nav = gnc.Navigate(bnm)      #navigate obj
tr=gnc.Trans(bnm)            #transaction obj
lout = gnc.Logout(bnm)       #logout obj

account_detail={}
page=lin.login(bnm, uname, pwd)                    #carry out login


vtr.valid_page(bnm,page)


page_source=nav.navigate_transaction(bnm)     #returns page source to collect account numbers....

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
form='csv'
for account in account_detail.keys():
    page_source1=tr.transaction_history(bnm,account)             #transaction
    if bnm.upper() == "FEDERAL":
        account_detail[account].append(htmpr.fed_html(form, page_source1))
    elif bnm.upper() == "CITI":
        account_detail[account].append(htmpr.citi_html(form, page_source1))
    elif bnm.upper() == "CANARA":
        account_detail[account].append(htmpr.canara_html(form, page_source1))

lout.logout(bnm)
print(account_detail)

'''
formats = ["csv", "json", "xml"]
if form not in formats:  # parsing transaction details
    form = "csv"

for i in account_num:
    account_detail[i].append(trans)
print(account_detail)
'''
'''
except Exception as e:
    print("**ERROR**")
    print(e.__doc__)
'''