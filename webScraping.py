from cgitb import html
from crypt import methods
import pandas as pd
from selenium import webdriver
import time as t
from bs4 import BeautifulSoup


class webScraping:
    def __init__(self, url):
        self.url = url
        browser = webdriver.Chrome()
        browser.find_element_by_id('selectPage').send_keys('120')
        t.sleep(2)
        html = browser.page_source
        browser.close()
        self.bs = BeautifulSoup(html, 'html.parser')
        return self.bs
