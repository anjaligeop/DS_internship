from bs4 import BeautifulSoup
import re

def acc_fed(page_source):
    detailsDS={}
    acc_num=[]
    amt = []
    account_type=[]
    branch=[]
    currency=[]

    soup = BeautifulSoup(page_source, 'html.parser')
    acc= soup.findAll('td', attrs={'class': 'radio clear-after'})
    for val in acc:
        val=val.text[1:]
        acc_num.append(val)
    atype=soup.findAll('td',attrs={'data-label':"Account Type : "})
    b=soup.findAll('td',attrs={'data-label':"Branch : "})
    c=soup.findAll('td',attrs={'data-label':"Currency : "})
    for i,j,k in zip(atype,b,c):
        account_type.append(i.text[1:])
        branch.append(j.text[1:])
        currency.append(k.text[1:])


    bal=soup.findAll('td',attrs={'class':'text-right'})

    for val in bal:
        val=val.text[:-3].replace(',','')
        amt.append(val[1:])

    fp = open("/home/anjaligeorgep/Desktop/download_html/acc_outputs/account_summary_federal.txt", "w")
    fp.write("[\n")

    for x,y,z,p,q in zip(acc_num,amt,account_type,branch,currency):
        detailsDS.update({x:[y,z,p,q]})
        fp.write('{{"accountNumber" : "{}",\n'.format(x))
        fp.write('"balance" : "{}",\n'.format(y))
        fp.write('"accountType":"{}",\n'.format(z))
        fp.write('"branch":"{}",\n'.format(p))
        fp.write('"currency":"{}}}",\n'.format(q))
    fp.write("]")

    return detailsDS

def acc_citi(page_source):
    detailsDS={}
    branch=[]
    currency=[]
    account_type=[]
    acc_num=[]
    amt=[]
    soup = BeautifulSoup(page_source,'html.parser')
    td=soup.findAll('td',attrs={'class': 'pad5 ligt_grey','align':'left'})
    bal=soup.findAll('td', attrs={'class': 'pad5 ligt_grey','align':'right'})

    atype=soup.findAll('p',attrs={'class':'dbfl box_b1'})
    b=soup.findAll('p',attrs={'class': 'pad5 ligt_grey','align':'top'})
    c=soup.findAll('p',attrs={'class':'dbfl box_b1','style':'width:70px'})

    


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

    fp = open("/home/anjaligeorgep/Desktop/download_html/acc_outputs/account_summary_citi.txt", "w")
    fp.write("[\n")
    for x,y in zip(acc_no,am):
        detailsDS.update({x:[y]})
        fp.write('{{"accountNumber" : "{}",\n'.format(x))
        fp.write('"balance" : "{}"}},\n'.format(y))
    fp.write("]")
    return detailsDS



def acc_canara(page_source):
    detailsDS={}
    branch=[]
    currency=[]
    account_type=[]
    acc_num = []
    amt = []
    details=[]
    soup = BeautifulSoup(page_source,'html.parser')
    tr = soup.findAll('tr', attrs={'class': 'alterrow2'})

    for x in range(len(tr)):
        td=tr[x].findAll('td')
        details.append(td[1].text.strip())

    acc_num.append(details[0])
    amt.append(details[3].replace(',',''))

    fp = open("/home/anjaligeorgep/Desktop/download_html/acc_outputs/account_summary_canara.txt", "w")
    fp.write("[\n")
    for x, y in zip(acc_num, amt):
        detailsDS.update({x:[y]})
        fp.write('{{"accountNumber" : "{}",\n'.format(x))
        fp.write('"balance" : "{}"}},\n'.format(y))
    fp.write("]")

    return detailsDS

