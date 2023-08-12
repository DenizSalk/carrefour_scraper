# -*- coding: utf-8 -*-
import json
import time
import requests
from bs4 import BeautifulSoup
files =["makyaj-urunleri-c-1710",
        "parfum-deodorant-c-1805tiras-urunleri-c-1736kagit-urunleri--c-1821",
        "sac-bakim-ve-aksesuar-c-1757",
        "saglik-urunleri-c-1831",
        ]
for categotyfile in files:
    final_file = categotyfile + ".txt"
    f = open(final_file, "r" , encoding="utf-8")
    print(final_file)
    lines = f.read().splitlines()
    data_list = []

    for url in lines:
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser', from_encoding='utf-8')
        try:
            category = soup.find('ol', attrs={'class': 'breadcrumb'}).get_text()
            categoryf = str(category)
        except:
            categoryf = "NULL"
            print("kategori okunamadı")
        try:
            name = soup.find('div', attrs={'class': 'name'}).get_text()
            namef = str(name)
        except:
            namef = "NULL"
            print("isim okunamadı")
        try:
            brand = soup.find('div', attrs={'class' : 'brand'}).get_text()
            brandf = str(brand)
        except:
            brandf = "NULL"
            print("marka okunamadı")
        try:
            itemprice = soup.find('span', attrs={'class' : 'js-variant-discounted-price'}).get_text()
            itempricef = str(itemprice)
        except:
            itempricef = "Null"
            print("fiyat okunamadı")
        data = {
            'category': categoryf,
            'name': namef,
            'brand': brandf,
            'itemprice': itempricef
        }
        data_list.append(data)
        newfile = "output2" + categotyfile + ".json"
        print(url)
        with open(newfile, 'w', encoding="utf-8") as f:
            json.dump(data_list, f, indent=4, ensure_ascii=False)