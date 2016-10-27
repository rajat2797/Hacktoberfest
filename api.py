from bs4 import BeautifulSoup as BS 
import json
import requests
import datetime


Months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

schools = ["class","high secondary"]

UG = ["graduate","b.tech","ug","pg"]

schoolStudents ={"Name":[],"Organisation":[],"EndDate":[]}

PgStudents = {"Name":[],"Organisation":[],"EndDate":[]}

others = {"Name":[],"Organisation":[],"EndDate":[]}



def scholarships(preference = "schools"):
	flag = 0
	url = "http://www.motachashma.com/scholarships/"
	returnobj = requests.get(url).text
	returnobj = BS(returnobj,"html.parser")
	ans = returnobj.find_all(id="tablecontmid")
	table = ans[0].find_all("table")
	th = table[0].find_all("tr")
	for x in th :
		print "\n"*4
		data = x.find_all("td")
		for x in range(len(data)):
			if x == 2:
				for y in schools :
					if y in data[x].text.lower():
						flag = 1
						try:
							schoolStudents["Name"].append(data[x-2].text.decode("utf-8").replace("  ","").replace("\n",""))
						except :
							schoolStudents["Name"].append(data[x-2].text.replace("  ","").replace("\n",""))
						schoolStudents["Organisation"].append(data[x-1].text)
						schoolStudents["EndDate"].append(data[x+1].text.decode("utf-8").replace("  ","").replace("\n",""))

				for y in UG:
					if y in data[x].text.lower() :
						flag = 1
						try:
							PgStudents["Name"].append(data[x-2].text.decode("utf-8").replace("  ","").replace("\n",""))
						except :
							PgStudents["Name"].append(data[x-2].text.replace("  ","").replace("\n",""))
						PgStudents["Organisation"].append(data[x-1].text)
						PgStudents["EndDate"].append(data[x+1].text.decode("utf-8").replace("  ","").replace("\n",""))

				if 	flag == 0 :	
					try:
						others["Name"].append(data[x-2].text.decode("utf-8").replace("  ","").replace("\n",""))
					except :
						others["Name"].append(data[x-2].text.replace("  ","").replace("\n",""))
					others["Organisation"].append(data[x-1].text)
					others["EndDate"].append(data[x+1].text.decode("utf-8").replace("  ","").replace("\n",""))

				flag = 0	

	# print schoolStudents
	# print "\n"*5
	# print others
	# print "\n"*5
	# print PgStudents
	if preference == "schools":
		return schoolStudents
	if preference == "pg" :
		return PgStudents
	if preference == "others" :
		return others			




def CBSEevents():
	Events = {"Name":[],"PDF":[]}
	flag = 0
	now = datetime.datetime.now()
	month = Months[now.month-1]
	url = "http://cbseacademic.in/circulars.html"
	ans = requests.get(url).text
	data = BS(ans,"html.parser")
	circular = data.find_all("table",id="circulars")
	a = circular[0]
	for x in a:
		if len(x) != 1 :
			td = x.find_all("td")
			for indices in range(len(td)-2):
				if month == str(td[1].text) :
					link = td[2].find_all("a")
					Events["PDF"].append(link[0].get("href"))
					Events["Name"].append(td[2].text)
					print "\n"*4
				else :
					flag = 1
					break
			if flag == 1:
				break	
	# print Events

	return Events

def Competetive(options='contests',status='active'):
	contests = {}
	hackathons = {}
	hiring = {}
	data = requests.get("http://testchallengehunt.appspot.com/v1/all")
	a = data.json()
	hiring["active"] = a["hiring"]["active"]
	hiring["upcoming"] = a["hiring"]["upcoming"]
	contests["active"] = a["contests"]["active"]
	contests["upcoming"] = a["contests"]["upcoming"]
	hackathons["upcoming"] = a["hackathons"]["upcoming"]
	hackathons["active"] = a["hackathons"]["active"]
	ds_q = a["ds_q"]
	print "\n*"*10
	if options == 'contests':
		if status == 'active' :
			return contests["active"]
		else :
			return contests['upcoming']	
	elif options == 'hiring':
		if status == 'active' :
			return hiring["active"]
		else :
			return hiring["upcoming"]	
	elif options == 'hackathons':
		if status == 'active' :
			return hackathons["active"]
		else :
			return hackathons["upcoming"]



