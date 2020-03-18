from pandas import DataFrame, read_csv
import pandas as pd
from bs4 import BeautifulSoup

def fed_html():
    soup = BeautifulSoup(open("/home/anjaligeorgep/Desktop/download_html/file_federal.html"), features="lxml")

    tr_date = soup.find_all(title="Transaction Date")
    tr_particular = soup.find_all(title="Particulars")
    tr_amt = soup.find_all(title="Amount")
    tr_type=soup.find_all(title="Amount Type")
    tr_balance = soup.find_all(title="Balance Amount")
    x=[]
    y=[]
    z=[]
    p=[]
    q=[]
    for a, b, c, d, e in zip(tr_date,tr_particular,tr_type,tr_amt,tr_balance):
        x.append(a.text)
        y.append(b.text)
        z.append(c.text)
        p.append(d.text)
        q.append(e.text)


    temp = open("/home/anjaligeorgep/Desktop/federal_json.txt", "w")  # store in json format
    temp.write("{\n")
    for a, b, c, d, e in zip(x,y,z,p,q):
        temp.write("{{date : {},\n".format(a))
        temp.write("description : {},\n".format(b))
        if c.upper() == "DR.":
            temp.write("withdraw : {},\n".format(d))
            temp.write("deposit : ,\n")
        else:
            temp.write("deposit : {},\n".format(d))
            temp.write("withdraw : ,\n")
        temp.write("balance : {}}},\n".format(e))
    temp.write("}")


#===============================================================================================================================
def citi_html():
    soup = BeautifulSoup(open("/home/anjaligeorgep/Desktop/download_html/file_citi.html"), features="lxml")
    rows1 = soup.findAll('table',attrs={'bgcolor':'#A7CBE3','cellpadding':'3'})
    tr_date = []
    tr_particulars = []
    tr_withdraw = []
    tr_deposit = []
    tr_with=[]
    tr_depo=[]
    tr_balance = []

    for r in range(len(rows1)):
        rows=rows1[r].findAll('tr')
        openbal=rows[1].findAll('td')
        bal=(openbal[4].text) #opening balance
        bal=float(bal.replace(',',''))

        for r in range(2,len(rows)-1):
            td = rows[r].findAll('td')
            tr_date.append(td[0].text)
            tr_particulars.append(td[1].text.strip())
            tr_with.append(td[2].text.strip())
            tr_depo.append(td[3].text.strip())

    for x,y in zip(tr_with,tr_depo): #replace commas
        x=x.replace(',','')
        tr_withdraw.append(x)
        y=y.replace(',','')
        tr_deposit.append(y)

    for i, j in zip(tr_withdraw, tr_deposit):
        if len(i.strip())==0:
            tr_balance.append(bal + float(j))
            bal = bal + float(j)
        else:
            tr_balance.append(bal - float(i))
            bal = bal - float(i)

    temp = open("/home/anjaligeorgep/Desktop/citi_json.txt", "w")  # store in json format
    temp.write("{\n")
    for a, b, c, d, e in zip(tr_date, tr_particulars,tr_withdraw,tr_deposit, tr_balance):
        temp.write("{{date : {},\n".format(a))
        temp.write("description : {},\n".format(b))
        temp.write("withdraw: {},\n".format(c))
        temp.write("deposit : {},\n".format(d))
        temp.write("balance : {}}},\n".format(e))
    temp.write("}")


#===============================================================================================================================
def canara_html():
    soup = BeautifulSoup(open("/home/anjaligeorgep/Desktop/download_html/file_canara.html"), features="lxml")
    tr_date = []
    tr_particulars = []
    tr_withdraw = []
    tr_deposit = []
    tr_balance = []

    rows = soup.findAll('tr', attrs={'class': 'AlterRow2'}) #all transaction rows
    for r in range(1,len(rows)):
        td=rows[r].findAll('td')
        tr_date.append(td[0].text)
        tr_particulars.append(td[3].text)
        tr_withdraw.append(td[5].text)
        tr_deposit.append(td[6].text)
        tr_balance.append(td[7].text)

    temp = open("/home/anjaligeorgep/Desktop/canara_json.txt", "w")  # store in json format
    temp.write("{\n")
    for a, b, c, d, e in zip(tr_date, tr_particulars, tr_withdraw, tr_deposit, tr_balance):
        temp.write("{{date : {},\n".format(a))
        temp.write("description : {},\n".format(b))
        temp.write("withdraw: {},\n".format(c))
        temp.write("deposit : {},\n".format(d))
        temp.write("balance : {}}},\n".format(e))
    temp.write("}")

#===============================================================================================================================

if __name__=="__main__":
    a=input("enter bank name : ")
    if a.upper()=="FEDERAL":
        fed_html()
    elif a.upper()=="CITI":
        citi_html()
    elif a.upper()=="CANARA":
        canara_html()






