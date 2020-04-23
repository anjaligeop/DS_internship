from bs4 import BeautifulSoup
import re

def acc_fed(page_source):
    detailsDS={}
    acc_num=[]
    amt = []
    account_type=[]
    currency=[]

    soup = BeautifulSoup(page_source, 'html.parser')
    acc= soup.findAll('td', attrs={'class': 'radio clear-after'})
    for val in acc:
        val=val.text[1:]
        acc_num.append(val)
    atype=soup.findAll('td',attrs={'data-label':"Account Type : "})
    c=soup.findAll('td',attrs={'data-label':"Currency : "})
    for i,k in zip(atype,c):
        account_type.append(i.text[1:])
        currency.append(k.text[1:])


    bal=soup.findAll('td',attrs={'class':'text-right'})

    for val in bal:
        val=val.text[:-3].replace(',','')
        amt.append(val[1:])

    for x,y,z,q in zip(acc_num,amt,account_type,currency):
        detailsDS.update({x:[{"balance":y},{"accountType":z},{"currency":q}]})
    return detailsDS

def acc_citi(page_source):
    detailsDS={}
    currency=[]
    account_type=[]
    acc_num=[]
    amt=[]
    soup = BeautifulSoup(page_source,'html.parser')
    td=soup.findAll('td',attrs={'class': 'pad5 ligt_grey','align':'left'})
    bal=soup.findAll('td', attrs={'class': 'pad5 ligt_grey','align':'right'})

    atype = soup.findAll('span', attrs={'style': 'font-weight: bold;'})
    for x in atype[:-1]:
        account_type.append(x.text.strip())

    c = soup.findAll('p', attrs={'class': 'dbfl box_b1', 'style': 'width:70px;'})
    for x in c[:-1]:
        currency.append(x.text)


    for x in range(len(td)):
        a=td[x].findAll('a')
        for r in a:
            acc_num.append(r.text.strip().replace('\n',''))
    for x in bal:
        amt.append(x.text.replace('Balance','').strip().replace(',',''))
    amt=amt[:-1]
    acc_num=acc_num[:-1]
    acc_no=[]
    for values in acc_num:
        acc_no.append(values[-12:])
    am=[]
    for x in amt:
        if x:
            am.append(x)
    i = 1
    for x,y,z,q in zip(acc_no,am,account_type,currency):
        detailsDS.update({i:{"accountSummary" :{"balance":y , "accountType":z ,"currency":q, "accountNumber":x}}})
        i = i+1

    return detailsDS



def acc_canara(page_source):
    detailsDS={}
    balance=[]
    acct=[]
    currency=[]
    account_type=[]
    acc_num = []
    acc=[]
    soup = BeautifulSoup(page_source,'html.parser')
    td = soup.findAll('td', attrs={'style': 'white-space:nowrap'})
    for a in td:
        acc.append(a.text)
    for a in acc:
        acc_num.append(a.split("-")[0].strip())

    acc_ty = soup.findChildren('caption')
    for x in acc_ty:
        acct = x.findChildren('span', attrs={'style': 'float:left; width:40%'})

    for x in acct:
        account_type.append(x.text.strip())

    table = soup.find_all('tbody')[4:]
    for rows in table:
        tr = rows.findAll('tr')
        for data in tr:
            td = data.find_all('td')[2:3]
            for x in td:
                pass
        currency.append(x.text)



    bal = soup.findAll('td', attrs={'class': 'ccyalign', 'width': '18%'})
    for x in bal:
        balance.append(x.text.replace(',', '').strip())

    for x, y,z,q in zip(acc_num, balance,account_type,currency):
        detailsDS.update({x:[{"balance":y},{"accountType":z},{"currency":q}]})

    return detailsDS

def scrape_summary(bank_name, page_source):
    if bank_name.upper() == "FEDERAL":
        return acc_fed(page_source)
    elif bank_name.upper() == "CITI":
        return acc_citi(page_source)
    elif bank_name.upper() == "CANARA":
        return acc_canara(page_source)