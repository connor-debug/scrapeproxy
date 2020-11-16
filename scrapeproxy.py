#!/usr/bin/env python3
import sys
import bs4
import requests

sys.stderr.write("This is a test for scrapping\n")
res = requests.get('https://www.socks-proxy.net')

#sys.stderr.write(res.text)

soup = bs4.BeautifulSoup(res.text, 'html.parser')
sys.stderr.write(soup.prettify())

sys.stderr.write(str(soup.textarea))

f = open("proxys.txt", "w")
f.write(str(soup.textarea))
f.close()

