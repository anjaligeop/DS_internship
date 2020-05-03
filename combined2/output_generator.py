import xml.etree.ElementTree as ET
import json
import re
import os

def generate_xml(account_details):
	data = ET.Element('accounts')
	for keys in account_details:
		account = ET.SubElement(data, 'account')
		accountSummary = ET.SubElement(account, 'accountSummary')
		acc_num = ET.SubElement(accountSummary, 'accountNumber')
		acc_type = ET.SubElement(accountSummary, 'accountType')
		balance = ET.SubElement(accountSummary, 'balance')
		currency = ET.SubElement(accountSummary, 'currency')
		acc_num.text = account_details[keys]['accountSummary']['accountNumber']
		acc_type.text = account_details[keys]['accountSummary']['accountType']
		balance.text = account_details[keys]['accountSummary']['balance']
		currency.text = account_details[keys]['accountSummary']['currency']
		transactions = ET.SubElement(account, 'transactions')
		trans_lst = account_details[keys]['transactions']
		for trans in trans_lst:
			elements = trans.split(',')
			transaction = ET.SubElement(transactions, 'transaction')
			date = ET.SubElement(transaction, 'date')
			cq_num = ET.SubElement(transaction, 'chequeNumber')
			des = ET.SubElement(transaction, 'description')
			amt = ET.SubElement(transaction, 'amount')
			bal = ET.SubElement(transaction, 'balance')
			date.text = elements[0]
			cq_num.text = '\\N'
			des.text = elements[2]
			amt.text = elements[3]
			bal.text = elements[4]
	mydata = ET.tostring(data)
	myfile = open("out.xml", "w")
	final_data = re.search(r'^b\'(.*?)\'$', str(mydata), re.I|re.S).group(1)
	myfile.write(str(final_data))

def generate_json(account_details):
	out_dict = {}
	out_dict['accounts'] = []
	for keys in account_details:
		out_dict['accounts'].append(account_details[keys])
	path = os.getcwd()
	json_content = json.dumps(out_dict)
	filename = path + '/out.json'
	with open(filename, 'w') as f1:
		f1.write(json_content)

def generate_csv(account_details):
	string = ''
	for keys in account_details:
		string = string + "#AccountStart " + str(account_details[keys]['accountSummary']['accountNumber']) + ",bank\n"
		string = string + "#BeginResult\n"
		string = string + "#JSON " + str(account_details[keys]['accountSummary']) +"\n"
		transaction_list = account_details[keys]['transactions']
		string = string + str(len(transaction_list)) + "\n" # total number of transactions
		for trans in transaction_list:
			string = string + trans + "\n"
		string = string + "#EndResult\n"
		string = string + "#AccountEnd\n"
	path = os.getcwd()
	filename = path + '/out'
	with open(filename, 'w') as f1:
		f1.write(string)

def main(account_details, form):
	if form.upper() == "XML":
		generate_xml(account_details)
	elif form.upper() == "JSON":
		generate_json(account_details)
	elif form.upper() == "CSV":
		generate_csv(account_details)
	else:
		generate_csv(account_details)
