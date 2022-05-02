from cgitb import html
from dataclasses import replace
from typing_extensions import Self
import pandas as pd
from selenium import webdriver
import time as t
from bs4 import BeautifulStoneSoup

""" 
    como saber se euma ação é preferencial ou ordinaria
    saber a data 
    
"""


class import_advfn:
    def __init__(self, acao, empresa, date_init='28/01/17', date_end='28/04/22'):
        self.acao = acao
        self.empresa = empresa.strip().lower().replace(
            ' ', '-')                                         # Ex : itau unibanco
        self.date_init = date_init                            # Ex : 28/01/17
        self.date_end = date_end                              # Ex : 28/04/22
        if self.acao[-1] == '4':
            self.tipo = 'pm'
        else:
            self.tipo = 'on'

    def push_action(self):

        for i in range(21, 0, -1):
            url = 'http://br.advfn.com/bolsa-de-valores/bovespa/{self.empresa}-{self.tipo}-{self.acao}/historico/mais-dados-historicos?current={i}&Date1={self.date_init}&Date2={self.date_end}'
            browser = webdriver.get(url)
            browser.get(url)
            t.sleep(3)
            html.browser.page_source
            browser.close()
            bs = BeautifulStoneSoup(html, 'html.parser')
            linhas = bs.find_all('tr', attrs={'class': 'result'})
            j = 0
            data = []
            while j < len(linhas):
                data.append(linhas[j].text)
                j += 1
            k = 0
            datanew = []
            while k < len(data):
                datanew.append(data[k].split('\n'))
                k += 1
            l = 1
            Days, Close, Variation, Variation_p, Open, Max, Min, Vol = [], [], [], [], [], [], [], []
            while l < len(datanew):
                Days.append(datanew[l][1])
                Close.append(datanew[l][2])
                Variation.append(datanew[l][3])
                Variation_p.append(datanew[l][4])
                Open.append(datanew[l][5])
                Max.append(datanew[l][6])
                Min.append(datanew[l][7])
                Vol.append(datanew[l][8])
        df = pd.DataFrame({
            'Data': Days,
            'Fechamento': Close,
            'Variacao': Variation,
            'Variacao_%': Variation_p,
            'Abertura': Open,
            'Maxima': Max,
            'Minima': Min,
            'Volume': Vol,
        })
        df['Fechamento'] = df['Fechamento'].map(t: t.replace(",", "."))
        df['Fechamento'] = df['Fechamento'].map(t: float(t))
        df['Variacao'] = df['Variacao'].map(t: t.replace(",", "."))
        df['Variacao'] = df['Variacao'].map(t: float(t))
        df['Variacao_%'] = df['Variacao_%'].map(t: t.replace(",", "."))
        df['Variacao_%'] = df['Variacao_%'].map(t: float(t))
        df['Abertura'] = df['Abertura'].map(t: t.replace(",", "."))
        df['Abertura'] = df['Abertura'].map(t: float(t))
        df['Maxima'] = df['Maxima'].map(t: t.replace(",", "."))
        df['Maxima'] = df['Maxima'].map(t: float(t))
        df['Minima'] = df['Minima'].map(t: t.replace(",", "."))
        df['Minima'] = df['Minima'].map(t: float(t))
        df['Volume'] = df['Volume'].map(t: float(t))
        df = df.to_csv(f'{self.acao}_{self.date_init}_{self.date_end}.csv')
