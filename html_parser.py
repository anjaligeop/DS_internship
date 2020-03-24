from pandas import DataFrame, read_csv
import pandas as pd
from bs4 import BeautifulSoup
import re

def fed_html(format):
    soup = BeautifulSoup(open("/home/anjaligeorgep/Desktop/download_html/file_federal.html"), features="lxml")
    tr_d = soup.find_all(title="Transaction Date")
    tr_particular = soup.find_all(title="Particulars")
    tr_amt = soup.find_all(title="Amount")
    tr_type=soup.find_all(title="Amount Type")
    tr_balance = soup.find_all(title="Balance Amount")
    c_num=[]
    x=[]
    y=[]
    z=[]
    p=[]
    q=[]
    tr_dt=[]
    amt=[]
    bal=[]
    for a, b, c, d, e in zip(tr_d,tr_particular,tr_type,tr_amt,tr_balance):
        x.append(a.text)
        y.append(b.text)
        z.append(c.text)
        p.append(d.text)
        q.append(e.text)
    y=y[1:]
    for val in p:
        amt.append(val.replace(',',''))
    for val in q:
        bal.append(val.replace(',',''))
    for dt in x:
        val=dt.split("-")
        tr_dt.append(val[2]+"-"+val[1]+"-"+val[0])


    if format.upper()=="JSON":
        temp = open("/home/anjaligeorgep/Desktop/federal_json.json", "w")  # store in json format
        temp.write("{\n")
        for a, b, c, d, e in zip(tr_dt,y,z,amt,bal):
            temp.write("{{date : {},\n".format(a))
            temp.write("cheque_num : \\N,\n")
            temp.write("description : {},\n".format(b))
            if c.upper() == "DR.":
                temp.write("withdraw : {},\n".format(d))
                temp.write("deposit : ,\n")
            else:
                temp.write("deposit : {},\n".format(d))
                temp.write("withdraw : ,\n")
            temp.write("balance : {}}},\n".format(e))
        temp.write("}")

    if format.upper()=="CSV":
        temp = open("/home/anjaligeorgep/Desktop/federal_csv", "w")  # store in csv format
        for a, b, c, d, e in zip(tr_dt, y, z, amt, bal):
            temp.write(a+",\\N,"+b+","+d+","+e+"\n")

    if format.upper()=="XML":
        temp = open("/home/anjaligeorgep/Desktop/federal_xml.xml", "w")  # store in xml format
        temp.write('<?xml version="1.0" encoding="utf-8"?>\n')
        temp.write("<root>\n")
        for a, b, c, d, e in zip(tr_dt, y, z, amt, bal):
            temp.write("<transaction>\n")
            temp.write("\t<date>{}</date>\n".format(a))
            temp.write("\t<cheque_num>\\N</cheque_num>\n")
            temp.write("\t<description>{}</description>\n".format(b))
            if c.upper() == "DR.":
                temp.write("\t<withdraw>{}</withdraw>\n".format(d))
                temp.write("\t<deposit></deposit>\n")
            else:
                temp.write("\t<deposit>{}</deposit>\n".format(d))
                temp.write("\t<withdraw></withdraw>\n")
            temp.write("\t<balance>{}</balance>\n".format(e))
            temp.write("</transaction>\n")
        temp.write("</root>")




#===============================================================================================================================
def citi_html(format):
    soup = BeautifulSoup(open("/home/anjaligeorgep/Desktop/download_html/file_citi.html"), features="lxml")
    rows1 = soup.findAll('table',attrs={'bgcolor':'#A7CBE3','cellpadding':'3'})
    tr_date = []
    tr_dt1=[]
    tr_particulars = []
    tr_withdraw = []
    tr_deposit = []
    tr_with=[]
    tr_depo=[]
    tr_balance = []
    tr_dt=[]
    tr_part=[]
    for r in range(len(rows1)):
        rows=rows1[r].findAll('tr')
        openbal=rows[1].findAll('td')
        bal=(openbal[4].text) #opening balance
        bal=float(bal.replace(',',''))

        for r in range(2,len(rows)-1):
            td = rows[r].findAll('td')
            tr_dt.append(td[0].text)
            tr_part.append(td[1].text.strip())
            tr_with.append(td[2].text.strip())
            tr_depo.append(td[3].text.strip())

    for x,y in zip(tr_with,tr_depo): #replace commas
        x=x.replace(',','')
        tr_withdraw.append(x)
        y=y.replace(',','')
        tr_deposit.append(y)

    for i in tr_dt:
        tr_dt1.append(i.replace(',','').strip())
    for dt in tr_dt1:
        val=dt.split("/")
        tr_date.append(val[2]+"-"+val[1]+"-"+val[0])

    for dcr in tr_part:
        tr_particulars.append(re.sub(' +', ' ', dcr))


    for i, j in zip(tr_withdraw, tr_deposit):
        if len(i.strip())==0:
            tr_balance.append(bal + float(j))
            bal = bal + float(j)
        else:
            tr_balance.append(bal - float(i))
            bal = bal - float(i)

    if format.upper() == "JSON":
        temp = open("/home/anjaligeorgep/Desktop/citi_json.json", "w")  # store in json format
        temp.write("{\n")
        for a, b, c, d, e in zip(tr_date, tr_particulars,tr_withdraw,tr_deposit, tr_balance):
            temp.write("{{date : {},\n".format(a))
            temp.write("cheque_num : \\N,\n")
            temp.write("description : {},\n".format(b))
            temp.write("withdraw: {},\n".format(c))
            temp.write("deposit : {},\n".format(d))
            temp.write("balance : {}}},\n".format(e))
        temp.write("}")

    if format.upper()=="CSV":
        temp = open("/home/anjaligeorgep/Desktop/citi_csv", "w")  # store in csv format
        for a, b, c, d, e in zip(tr_date, tr_particulars, tr_withdraw, tr_deposit, tr_balance):
            temp.write(a+","+"\\N,"+b.strip()+","+str(c)+","+str(d)+","+str(e)+"\n")


    if format.upper()=="XML":
        temp = open("/home/anjaligeorgep/Desktop/citi_xml.xml", "w")  # store in xml format
        temp.write('<?xml version="1.0" encoding="utf-8"?>\n')
        temp.write("<root>\n")
        for a, b, c, d, e in zip(tr_date, tr_particulars, tr_withdraw, tr_deposit, tr_balance):
            temp.write("\t<date>{}</date>\n".format(a))
            temp.write("\t<cheque_num>\\N</cheque_num>\n")
            temp.write("\t<description>{}</description>\n".format(b.strip()))
            temp.write("\t<withdraw>{}</withdraw>\n".format(c))
            temp.write("\t<deposit>{}</deposit>\n".format(d))
            temp.write("\t<balance>{}</balance>\n".format(e))
        temp.write("</root>")
#===============================================================================================================================
def canara_html(format):
    soup = BeautifulSoup(open("/home/anjaligeorgep/Desktop/download_html/file_canara.html"), features="lxml")
    tr_date = []
    tr_particulars = []
    tr_withdraw = []
    tr_deposit = []
    tr_balance = []
    tr_dt1=[]
    tr_dt=[]
    ch_n=[]
    rows = soup.findAll('tr', attrs={'class': 'AlterRow2'}) #all transaction rows
    for r in range(1,len(rows)):
        td=rows[r].findAll('td')
        tr_dt.append(td[0].text)
        tr_particulars.append(td[3].text)
        tr_withdraw.append(td[5].text)
        tr_deposit.append(td[6].text)
        tr_balance.append(td[7].text)
        ch_n.append(td[2].text)

    for v in tr_dt:
        tr_dt1.append(v[:10])
    for dt in tr_dt1:
        val=dt.split("-")
        tr_date.append(val[2]+"-"+val[1]+"-"+val[0])

    if format.upper() == "JSON":
        temp = open("/home/anjaligeorgep/Desktop/canara_json.json", "w")  # store in json format
        temp.write("{\n")
        for a,cnum, b, c, d, e in zip(tr_date, ch_n,tr_particulars, tr_withdraw, tr_deposit, tr_balance):
            temp.write("{{date : {},\n".format(a))
            if len(cnum)!=0:
                temp.write("cheque_num : {},\n".format(cnum))
            else:
                temp.write("cheque_num : \\N,\n")
            temp.write("description : {},\n".format(b))
            temp.write("withdraw: {},\n".format(c))
            temp.write("deposit : {},\n".format(d))
            temp.write("balance : {}}},\n".format(e))
        temp.write("}")

    if format.upper()=="CSV":
        temp = open("/home/anjaligeorgep/Desktop/canara_csv", "w")  # store in csv format
        for a,cnum, b, c, d, e in zip(tr_date,ch_n, tr_particulars, tr_withdraw, tr_deposit, tr_balance):
            if len(cnum) != 0:
                temp.write(a+","+cnum+","+b+","+c+","+d+","+e+"\n")
            else:
                temp.write(a + ",\\N," + b + "," + c + "," + d + ","+e + "\n")


    if format.upper()=="XML":
        temp = open("/home/anjaligeorgep/Desktop/canara_xml.xml", "w")  # store in xml format
        temp.write('<?xml version="1.0" encoding="utf-8"?>\n')
        temp.write("<root>\n")
        for a,cnum, b, c, d, e in zip(tr_date,ch_n, tr_particulars, tr_withdraw, tr_deposit, tr_balance):
            temp.write("<transaction>\n")
            temp.write("\t<date>{}</date>\n".format(a))
            if len(cnum) != 0:
                temp.write("\t<cheque_num>{}</cheque_num>\n".format(cnum))
            else:
                temp.write("\t<cheque_num>\\N</cheque_num>\n")
            temp.write("\t<description>{}</description>\n".format(b))
            temp.write("\t<withdraw>{}</withdraw>\n".format(c))
            temp.write("\t<deposit>{}</deposit>\n".format(d))
            temp.write("\t<balance>{}</balance>\n".format(e))
            temp.write("</transaction>\n")
        temp.write("</root>")
#===============================================================================================================================

if __name__=="__main__":
    formats=["csv","json","xml"]
    a=input("enter bank name : ")
    format=input("enter the format (json,csv,xml) :")
    if format not in formats:
        format="csv"
    if a.upper()=="FEDERAL":
        fed_html(format)
    elif a.upper()=="CITI":
        citi_html(format)
    elif a.upper()=="CANARA":
        canara_html(format)






