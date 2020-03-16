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

z=0
with open('/home/anjaligeorgep/Downloads/federal.csv','rt')as fp:
    data = csv.reader(fp)
    for row in data:
        if "Tran Date" in row:
            z=1

        if z==1:
            details.append(row)
for n in range(1,len(details)):
    tr_date.append(details[n][1])
    tr_description.append(details[n][2])
    tr_withdraw.append(details[n][7])
    tr_deposit.append(details[n][8])
    tr_balance.append(details[n][9])

def json_form():
    temp = open("/home/anjaligeorgep/Desktop/json_federal.txt", "a")
    temp.write("{")

    for a,b,c,d,e in zip(tr_date,tr_description,tr_withdraw,tr_deposit,tr_balance):
        temp.write("{{date : {},\n".format(a))
        temp.write("description : {},\n".format(b))
        temp.write("withdraw: {},\n".format(c))
        temp.write("deposit : {},\n".format(d))
        temp.write("balance : {}}},\n".format(e))
    temp.write("}")

def csv_form():
    temp = open("/home/anjaligeorgep/Desktop/federal_store_csv.txt", "a")
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
