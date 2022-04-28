import pandas as pd
from selenium import webdriver
import time as t
from bs4 import BeautifulSoup
import numpy as np
import scrapy as sp
import requests


url = 'https://statusinvest.com.br/acoes/variacao/ibovespa'
html = requests.get(url).content
sel = sp.Selector(text=html)

Xpath = '//*[@class="info w-100"]'
Xpath2 = '/*[@id="asUp"]'

ps = sel.xpath(Xpath)
ps2 = sel.xpath(Xpath2)

print(ps)
