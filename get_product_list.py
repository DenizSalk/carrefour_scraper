import time
import os
import requests
from bs4 import BeautifulSoup
maincat = ["cerez-cikolata-ve-biskuvi-c-1493",
		   "https://www.carrefoursa.com/tek-dondurma/c/1266",
		   "https://www.carrefoursa.com/multipack-dondurma/c/1270"
]
for cats in maincat:
	for x in range(1,100):
		url = cats
		urlend = '?q=%3AbestSeller&show=All'
		urlfinal = url + urlend
		reqs = requests.get(urlfinal)
		soup = BeautifulSoup(reqs.text, 'html.parser')
		for link in soup.find_all('div', attrs={'class' : 'product_click'}):
			catname = str(url.replace("https://www.carrefoursa.com/", "") + ".txt")
			catnamev2 = catname.replace("/", "-")
			print("https://www.carrefoursa.com" + link.find('a')['href'])
			with open(catnamev2, 'a') as f:
				f.write("https://www.carrefoursa.com" + link.find('a')['href'] + "" )
				f.close()
	else:
	  print("Finally finished!")