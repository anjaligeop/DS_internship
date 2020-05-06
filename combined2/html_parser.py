from bs4 import BeautifulSoup
import re
import csv

def fed_html(file_type, page_source1):
    if file_type == 'html':
        soup = BeautifulSoup(page_source1,'html.parser')
        tr_d = soup.find_all(title="Transaction Date")
        tr_particular = soup.find_all('td',attrs={'data-label':"Particulars : "})
        tr_amt = soup.find_all(title="Amount")
        tr_type=soup.find_all(title="Amount Type")
        tr_balance = soup.find_all(title="Balance Amount")
        trans={}
        x=[]
        y=[]
        z=[]
        p=[]
        q=[]
        pat=[]
        tr_dt=[]
        amt=[]
        bal=[]
        for a, b, c, d, e in zip(tr_d,tr_particular,tr_type,tr_amt,tr_balance):
            x.append(a.text)
            pat.append(b.text)
            z.append(c.text)
            p.append(d.text)
            q.append(e.text)

        for val in p:
            amt.append(val.replace(',',''))
        for val in q:
            bal.append(val.replace(',',''))
        for dt in x:
            val=dt.split("-")
            tr_dt.append(val[2]+"-"+val[1]+"-"+val[0])

        for val in pat:
            y.append(val[1:])
        trans_list = []
        for a, b, c, d, e in zip(tr_dt, y, z, amt, bal): #store in a dictionary
            trans_str = ''
            if c.upper() == "DR.":
                key="transactions"
                trans.setdefault(key,[])
                if c.upper() == "DR.":
                    ltr=[a,'',b,'',d,e] #date,chequeNum,particulars,withdraw,deposit,balance
                    trans_str = str(a) + ',NA,' + str(b) + ',' + str(d) + ',' + str(e)
                else:
                    trans_str = str(a) + ',NA,' + str(b) + ',-' + str(d) + ',' + str(e)
                    ltr = [a,'', b,d,'',e]

                trans[key].append(ltr)
                trans_list.append(trans_str)

        return trans_list
    if file_type == 'csv':
        rows = []
        trans_list = []
        with open(page_source1, 'r', encoding='utf-8-sig') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                rows.append(row)
        for row in rows:
            if row == '' :
                continue
            if not re.search(r'^\d+$', str(row[0]), re.I|re.S) or re.search(r'^\s*$', str(row[1]), re.I|re.S):
                continue
            dates = str(row[1]).split('-')
            date = dates[2] + '-' + dates[1] + '-' + dates[0]
            desc = str(row[2]).replace('\\', ' ')
            amt = ''
            if re.search(r'^\s*$', str(row[7]), re.I|re.S):
                amt = str(row[8])
            else:
                amt = '-' + str(row[7])
            amt = amt.replace(',', '')
            bal = str(row[9]).replace(',','')
            trans_list.append(date+ ',NA,' +desc+ ',' +amt+ ',' +bal)
        csvfile.close()
        return trans_list

#===============================================================================================================================
def citi_html(file_type, page_source1):
    soup = BeautifulSoup(page_source1,'html.parser')
    rows1 = soup.findAll('table',attrs={'bgcolor':'#A7CBE3','cellpadding':'3'})
    trans={}
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
        dcr=dcr.replace('\\',' ')
        tr_particulars.append(re.sub(' +', ' ', dcr))


    for i, j in zip(tr_withdraw, tr_deposit):
        if len(i.strip())==0:
            bal = bal + float(j)
            tr_balance.append(round(bal, 2))
        else:
            bal = bal - float(i)
            tr_balance.append(round(bal, 2))

    trans_list = []
    for a, b, c, d, e in zip(tr_date, tr_particulars, tr_withdraw, tr_deposit, tr_balance):
        key = "transactions"
        trans.setdefault(key, [])
        amt = str(d)
        if amt == '':
            amt = '-' + str(c)
        b = b.replace(',',' ')
        ltr=[str(a),'',str(b),str(amt),str(e)]
        trans_str = str(a)+ ',NA,' +str(b)+ ',' +str(amt)+ ',' +str(e)
        trans_list.append(trans_str)

    return trans_list
#===============================================================================================================================
def canara_html(file_type, page_source1):
    soup = BeautifulSoup(page_source1,'html.parser')
    trans={}
    tr_date = []
    tr_particulars = []
    tr_withdraw = []
    tr_deposit = []
    tr_balance = []
    tr_dt1=[]
    tr_dt=[]
    ch_n=[]
    tr_b=[]
    rows = soup.findAll('tr', attrs={'class': 'AlterRow2'}) #all transaction rows
    for r in range(1,len(rows)):
        td=rows[r].findAll('td')
        tr_dt.append(td[0].text)
        tr_particulars.append(td[3].text)
        tr_withdraw.append(td[5].text)
        tr_deposit.append(td[6].text)
        tr_b.append(td[7].text)
        ch_n.append(td[2].text)

    for v in tr_dt:
        tr_dt1.append(v[:10])
    for dt in tr_dt1:
        val=dt.split("-")
        tr_date.append(val[2]+"-"+val[1]+"-"+val[0])
    for v in tr_b:
        v=v.replace(',','')
        tr_balance.append(v)
    trans_list = []
    for a, cnum, b, c, d, e in zip(tr_date, ch_n, tr_particulars, tr_withdraw, tr_deposit, tr_balance):
        key = "transactions"
        trans.setdefault(key, [])
        ltr = [a, cnum, b, c, d, e]
        amt = str(d)
        if amt == '':
            amt = '-' + str(c)
        trans_str = str(a) + ',' + str(cnum) + ',' + str(b) + ',' + str(amt) + ',' + str(e)
        trans_list.append(trans_str)
        trans[key].append(ltr)

    return trans_list
#===============================================================================================================================

def parse_html(bank_name, file_type, page_source):
    if bank_name.upper() == "FEDERAL":
        return fed_html(file_type, page_source)
    elif bank_name.upper() == "CITI":
        return citi_html(file_type, page_source)
    elif bank_name.upper() == "CANARA":
        return canara_html(file_type, page_source)
