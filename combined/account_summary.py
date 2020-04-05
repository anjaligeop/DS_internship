from bs4 import BeautifulSoup
import re

def acc_fed():
    acc_num=[]
    amt = []
    soup = BeautifulSoup(open("/home/anjaligeorgep/Desktop/download_html/account_summary/federal/fed_acc.html"), features="lxml")
    acc= soup.findAll('td', attrs={'class': 'radio clear-after'})
    for val in acc:
        val=val.text[1:]
        acc_num.append(val)

    bal=soup.findAll('td',attrs={'class':'text-right'})

    for val in bal:
        val=val.text[:-3].replace(',','')
        amt.append(val[1:])

    fp = open("/home/anjaligeorgep/Desktop/download_html/acc_outputs/account_summary_federal.txt", "w")
    fp.write("[\n")

    for x,y in zip(acc_num,amt):
        fp.write('{{"accountNumber" : "{}",\n'.format(x))
        fp.write('"balance" : "{}"}},\n'.format(y))
    fp.write("]")
    return acc_num

def acc_citi():
    acc_num=[]
    amt=[]
    soup = BeautifulSoup(open("/home/anjaligeorgep/Desktop/download_html/account_summary/citi/citi_acc.html"), features="lxml")
    td=soup.findAll('td',attrs={'class': 'pad5 ligt_grey','align':'left'})
    bal=soup.findAll('td', attrs={'class': 'pad5 ligt_grey','align':'right'})
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
        fp.write('{{"accountNumber" : "{}",\n'.format(x))
        fp.write('"balance" : "{}"}},\n'.format(y))
    fp.write("]")
    return acc_no



def acc_canara():
    acc_num = []
    amt = []
    details=[]
    soup = BeautifulSoup(open("/home/anjaligeorgep/Desktop/download_html/account_summary/canara/canara_acc.html"), features="lxml")
    tr = soup.findAll('tr', attrs={'class': 'alterrow2'})

    for x in range(len(tr)):
        td=tr[x].findAll('td')
        details.append(td[1].text.strip())

    acc_num.append(details[0])
    amt.append(details[3].replace(',',''))

    fp = open("/home/anjaligeorgep/Desktop/download_html/acc_outputs/account_summary_canara.txt", "w")
    fp.write("[\n")
    for x, y in zip(acc_num, amt):
        fp.write('{{"accountNumber" : "{}",\n'.format(x))
        fp.write('"balance" : "{}"}},\n'.format(y))
    fp.write("]")
    return acc_num


