from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import config as cfg
import driverfile as dfr

def valid_page(bankname,page):
    page_titles=["FedNet :Dashboard","Citibank Online","Canara Bank Internet Banking"]
    soup = BeautifulSoup(page, 'html.parser')
    if bankname.upper()=="FEDERAL":
        title=soup.find('title')
        if title.text in page_titles:
            pass
    elif bankname.upper()=="CITI":
        title = soup.find('title')
        if title.text in page_titles:
            pass

    elif bankname.upper()=="CANARA":
        title = soup.find('title')
        if title.text in page_titles:
            pass


def login_validator(bankname):
    #options = Options()
    #options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path="/home/anjaligeorgep/Desktop/perfios/chromedriver")
#----------------------------------------------------------------------------------------------------------------------------------------------
    if bankname.upper()=="FEDERAL":
        #driver.get('https://www.fednetbank.com/corp/AuthenticationController?__START_TRAN_FLAG__=Y&FORMSGROUP_ID__=AuthenticationFG&__EVENT_ID__=LOAD&FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=1&BANK_ID=049&LANGUAGE_ID=001')

        login_elements_id = ["AuthenticationFG.USER_PRINCIPAL", "AuthenticationFG.ACCESS_CODE", "VALIDATE_CREDENTIALS"]

        for elem in login_elements_id:
            if driver.find_element_by_id(elem).is_displayed():
                pass



    if bankname.upper() == "CITI":
            #driver.get("https://www.online.citibank.co.in/products-services/online-services/internet-banking.htm")
            #driver.find_element_by_link_text("LOGIN NOW").click()
            #child = driver.window_handles[1]
            #driver.switch_to.window(child)
            login_elements_xpath = ["//input[@id='User_Id']", "//img[@id='skImg']",
                                    "//div[@class='fl width189 pt5 pb10']//input[@id='password']",
                                    "//div[@class='cl fl ls_login']"]
            try:
                for elem in login_elements_xpath:
                    if driver.find_element_by_xpath(elem).is_displayed():
                        pass
            except Exception as e:
                print("-----error-----")
                print(e.__doc__)


    if bankname.upper() == "CANARA":
        #driver.get('https://netbanking.canarabank.in/entry/ENULogin.jsp?')
        login_elements_xpath = ["//input[@id='fldLoginUserId']", "//input[@id='fldPassword']",
                                "//input[@class='btn btn-default']"]
        try:
            for elem in login_elements_xpath:
                if driver.find_element_by_xpath(elem).is_displayed():
                    pass
        except Exception as e:
            print("-----error-----")
            print(e.__doc__)


def summary_validator():
    pass
def transaction_validator():
    pass


