from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import config as cfg
import driverfile as dfr
import sys
def valid_page(bankname,page):
    
    page_titles=["FedNet :Dashboard","Citibank Online","Canara Bank Internet Banking"]
    soup = BeautifulSoup(page, 'html.parser')
    try:
        if bankname.upper()=="FEDERAL":
            title=soup.find('title')    
            if title.text in page_titles:
                print("successful login\n")
            else:                
                pass
        elif bankname.upper()=="CITI":
            title = soup.find('title')
            if title.text in page_titles:
                print("successful login\n")
            else:
                pass

        elif bankname.upper()=="CANARA":
            title = soup.find('title')
            if title.text in page_titles:
                print("successful login\n")
            else:
                pass
    except Exception as e:  
        path = os.getcwd()
        error="ERROR\n Did not reach homepage"
        filename = path + '/err'
        with open(filename, 'w') as f1:
            f1.write(error)
        

     
        print("Exception occcurred - "+str(e))
        



def summary_validator():
    pass
def transaction_validator():
    pass


