from bs4 import BeautifulSoup
import requests
import json


#table = 'livedepartureresults'
url= 'http://ojp.nationalrail.co.uk/service/ldbboard/dep/WKI?j=0'
r = requests.get(url)
res =  r.text
f = open("cache.txt","w")
f.writelines(res)
f.close()


soup = BeautifulSoup(res, 'html.parser')
table = soup.find('table', attrs={'cellpadding':'0'})
tableHead = table.find_all('th')
head = []

for h in tableHead:
    head.append(h.string)
    #print h.string



rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    for index,value in enumerate(cols):
        try:
			info = head[index] + ": " + value.string.strip()
			with open("trains.json", "w") as writeJSON:
				json.dump(info, writeJSON)
				print head[index] + ": " + value.string.strip()
        except:
            pass
    print "\n"


