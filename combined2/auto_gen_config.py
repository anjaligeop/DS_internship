dump=open("/home/anjaligeorgep/Desktop/sample1.txt","r")#contains katalon dump
f=open("/home/anjaligeorgep/Desktop/cfg.py","a")        #configuration file
bnm=input("enter bankname : ")
type_id=input("enter config name :")

i=0
clicks={bnm:{}}
for x in dump:
	if x.startswith("open"):
		url=x.split("|")
		y={bnm:url[1]}		
		f.write('bank_url = ' + repr(y) + '\n')
	if x.startswith("click"):		
		values=x.split("|")
		val=values[1].strip()	
		print(val)	
		if val.startswith("id"):
			clicks[bnm].update({'click'+str(i):val[3:]+",id"})	
			i=i+1				
		elif val.startswith("//"):
			clicks[bnm].update({'click'+str(i):val+",xpath"})
			i=i+1	
		elif val.startswith("link"):
			clicks[bnm].update({'click'+str(i):val[5:]+",text"})
			i=i+1	
		elif val.startswith("name"):
			clicks[bnm].update({'click'+str(i):val[5:]+",name"})
			i=i+1	
f.write(type_id+' = '+repr(clicks)+'\n')
		
		
f.close()

		


