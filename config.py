
webdriver_path={"chrome":'webdriver.Chrome(executable_path="/home/anjaligeorgep/Desktop/perfios/chromedriver")'}

bank_url={"federal":"https://www.fednetbank.com/corp/AuthenticationController?__START_TRAN_FLAG__=Y&FORMSGROUP_ID__=AuthenticationFG&__EVENT_ID__=LOAD&FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=1&BANK_ID=049&LANGUAGE_ID=001","canara":"https://netbanking.canarabank.in/entry/ENULogin.jsp?","citi":"https://www.online.citibank.co.in/products-services/online-services/internet-banking.htm"}

login_id = {"federal":{"userid":"AuthenticationFG.USER_PRINCIPAL,id",
                       "pwid":"AuthenticationFG.ACCESS_CODE,id",
                       "clicklogin":"VALIDATE_CREDENTIALS,id",},

            "canara":{"userid":"fldLoginUserId,id",
                      "pwid":"fldPassword,id",
                      "captchaid":"fldcaptcha,id",
                      "clicklogin":"//input[@value='SIGN IN'],xpath",},

            "citi":{"loginbtn":"LOGIN NOW,text",
                    "userid":"User_Id,id",
                    "keyboardid":"skImg,id",
                    "pwid":"password,id",
                    "clicklogin":"//div[@id='main-wrapper']/div/div[2]/div[2]/div/div/div[2]/div[3]/div/a/div,xpath",}
            }

navigate_id={"federal":{"click0":"Accounts,id",
                        "click1":"Accounts-Info_Operative-Accounts,id",
                        "click2":"//button[@id='txnHistoryBtn']/span,xpath",
                        "click3":"Caption6715787,id",
                        },
             "canara":{"click0":"grpspan_A_A07,id",
                       "click1":"RRASMlink,id",
                        "click2":"//table[@id='graphtable']/tbody/tr[3]/td/div[2],xpath",
                        "click3":"//*[@id='infoBox']/div[3],xpath",
                       },
             "citi":{"click0":"View Account Summary,text",
              "click1":"im012,id",
              "click2":"//div[@id='box02']/table/tbody/tr[2]/td/a/font,xpath",}

             }

logout_id={"federal":{"logoutnav":"//div[@id='header-nav']/ul/li[5]/a/span/b,xpath",
                      "logoutbtn":"HREF_Logout,id"},
           "canara":{"logoutbtn":"Logout,text",
                     "closewindow":"fldSubmit,name"},
           "citi":{"logoutbtn":"Sign out,text"}

}
