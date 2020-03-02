# federal bank

from pandas import DataFrame, read_csv
import pandas as pd
import xlrd
import re
import linecache
z = 0
tr_dates = []
tr_particulars = []
tr = []
tr_cd = []
tr_amt = []  #last value = total withdrawals
tr_balance = []  #last value = total deposits
totalw = []
totald = []
part2=[]

fp = open("/home/anjaligeorgep/Desktop/stmt.txt", "r")

for i, line in enumerate(fp, 1):
    if line.strip().startswith("Date"):
        z = z+1
    if line.strip().startswith("GRAND TOTAL"):
        amt = re.findall("[0-9\,]{1,}\.[0-9]{2}", line)  # withdrawal/deposit
        if len(amt) != 0:
            totalw.append(amt[0])
            totald.append(amt[1])
        break

    if z == 1: #page 1

        date = re.findall(r"[\d]{1,2}-[\d]{1,2}-[\d]{4}", line.strip()) #date
        if len(date) != 0:
            tr_dates.append(date[0])


        amt=re.findall("[0-9\,]{1,}\.[0-9]{2}",line) #withdrawal/deposit
        if len(amt) != 0:
            tr_amt.append(amt[0])
            tr_balance.append(amt[1])



        part=re.findall(r"[A-Z]+[/:][0-9]*[A-Z]*[/]{0,1}[a-z@0-9/]*",line) # second line of particulars

        if len(part)!=0: 

            the_lin=linecache.getline("/home/anjaligeorgep/Desktop/stmt.txt", i+1).strip()

            next_part=re.findall(r"[a-zA-Z0-9]+[/.@\-]+[A-Za-z/]*",the_lin)
            part2.append(next_part)

            tr_particulars.append(part[0])

#=======================================================================================================================

    if z == 2: #page 2

        date = re.findall(r"[\d]{1,2}-[\d]{1,2}-[\d]{2,4}", line) #date
        if len(date) != 0:
            tr_dates.append(date[0])

        amt = re.findall("[0-9\,]{1,}\.[0-9]{2}",line) #withdrawal/deposit
        if len(amt) != 0:
            tr_amt.append(amt[0])
            tr_balance.append(amt[1]) #balance

        part = re.findall(r"[A-Z]+[/:][0-9]*[A-Z]*[/]{0,1}[a-z@0-9/]*", line) #second line of particulars

        if len(part) != 0:

            the_lin = linecache.getline("/home/anjaligeorgep/Downloads/stmt.txt", i + 1).strip()

            next_part = re.findall(r"[a-zA-Z0-9]+[/.@\-]+[A-Za-z/]*", the_lin)
            part2.append(next_part)

            tr_particulars.append(part[0])


tr_amt1 = []
tr_balance1 = []
for a, b in zip(tr_amt, tr_balance): # remove commas in amounts
    a = a.replace(',', '')
    tr_amt1.append(a)
    b = b.replace(',', '')
    tr_balance1.append(b)


for i in range(len(tr_balance)-1):
    if tr_balance[i+1] > tr_balance[i]:
        tr.append("deposit")
    else:
        tr.append("withdraw")


tr_particulars1 = []
for d,x in zip(tr_particulars, part2):

    if len(x) != 0:
        tr_particulars1.append(str(d)+str(x[4]).strip())
    else:
        tr_particulars1.append(d)

for a, b, c, d, e in zip(tr_dates, tr_particulars1, tr_amt1, tr_balance1, tr_cd):
    print("\n"+a+","+b+","+c+","+d+","+e)

'''
df = pd.read_excel('/home/anjaligeorgep/Desktop/perfios/tr.xls',skiprows=10)
print(df)
'''


