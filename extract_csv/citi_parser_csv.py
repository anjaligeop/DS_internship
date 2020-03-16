import csv
import pandas as pd
import xlrd
import re

details=[]
tr_date=[]
tr_description=[]
tr_deposit=[]
tr_withdraw=[]
tr_balance=[]
#with open('/home/anjaligeorgep/Downloads/4687648_1583142635111.CSV','rt')as f:

opening_balance=[]
with open('/home/anjaligeorgep/Downloads/citibank.csv','rt')as fp:
    for i, line in enumerate(fp, 1):
        if "Opening Balance"in line.strip():
            openbal=line
    open_bal = re.findall(r"[0-9\,]{1,}\.[0-9]{2}", openbal)

with open('/home/anjaligeorgep/Downloads/citibank.csv', 'rt')as fp:
    data = csv.reader(fp)
    for row in data:
        if len(row) == 6:
            details.append(row)

for n in range(len(details)):
    tr_date.append(details[n][0])
    tr_description.append(details[n][1])
    tr_withdraw.append(details[n][2])
    tr_deposit.append(details[n][3])

blank=["--"]
#calculating balance

bal=float(open_bal[0])
for i,j in zip(tr_withdraw,tr_deposit):
    if i.strip() in blank:
        tr_balance.append(bal+float(j))
        bal=bal+float(j)
    else:
        tr_balance.append(bal-float(i))
        bal = bal - float(i)


def json_form():
    temp = open("/home/anjaligeorgep/Desktop/json_citi.txt", "a")
    temp.write("{")
    for a,b,c,d,e in zip(tr_date,tr_description,tr_withdraw,tr_deposit,tr_balance):
        temp.write("{{date : {},\n".format(a))
        temp.write("description : {},\n".format(b))
        temp.write("withdraw: {},\n".format(c))
        temp.write("deposit : {},\n".format(d))
        temp.write("balance : {}}},\n".format(e))
    temp.write("}")

def csv_form():
    temp = open("/home/anjaligeorgep/Desktop/citi_store_csv.txt", "a")
    for a,b,c,d,e in zip(tr_date,tr_description,tr_withdraw,tr_deposit,tr_balance):
        temp.write("{},".format(a))
        temp.write("{},".format(b))
        temp.write("{},".format(c))
        temp.write("{},".format(d))
        temp.write("{}\n".format(e))



if __name__=="__main__":
    ty=input("enter format : ")
    if ty.upper()=="CSV":
        csv_form()
    elif ty.upper()=="JSON":
        json_form()





























