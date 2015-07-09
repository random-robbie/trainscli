from bs4 import BeautifulSoup
import requests



#table = 'livedepartureresults'
url= 'http://ojp.nationalrail.co.uk/service/ldbboard/dep/WKI?j=0'
r = requests.get(url)
res =  r.text
f = open("cache.txt","w")
f.writelines(res)
f.close()


soup = BeautifulSoup(res)
table = soup.find('table', attrs={'cellpadding':'0s'})
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
            print head[index] + ": " + value.string.strip()
        except:
            pass
    print "\n"


