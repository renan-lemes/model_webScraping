from crypt import methods
import pandas as pd
from selenium import webdriver
import time as t
from bs4 import BeautifulSoup


class webScraping:
    def __init__(self, url) -> pd.DataFrame:
        self.url = url

    @classmethod
    def meth(self):
        self.browser = webdriver.Chrome()
        self.browser.get(self.url)
        self.browser.find_element_by_id(
            'segment').send_keys('Setor de Atuação')
        t.sleep(2)
        self.browser.find_element_by_id('selectPage').send_keys('120')
        t.sleep(2)
        self.html = self.browser.page_source
        self.browser.close()
        self.bs = BeautifulSoup(self.html, 'html.parser')
        self.linhas = self.bs.find_all('td')

        setor, cod, acao, tipo, qtde_t, part, part_a = [], [], [], [], [], [], []
        i = 0
        while i < (len(self.linhas)):
            setor.append(self.linhas[i].text)
            cod.append(self.linhas[i+1].text)
            acao.append(self.linhas[i+2].text)
            tipo.append(self.linhas[i+3].text)
            qtde_t.append(self.linhas[i+4].text)
            part.append(self.linhas[i+5].text)
            part_a.append(self.linhas[i+6].text)
            i += 7

        df = pd.DataFrame({'Setor': setor[:-1],
                           'Acao': cod[:-1],
                           'Empresa': acao[:-1],
                           'Qntd_teorica': qtde_t[:-1],
                           'Part_%': part[:-1]})
        df['SubSetor'] = df['Setor'].apply(
            lambda s: s[s.rfind('/')+1:].strip())
        df['Qntd_teorica'] = df['Qntd_teorica'].apply(
            lambda s: s.replace(".", ""))
        df['Qntd_teorica'] = pd.to_numeric(df['Qntd_teorica'])
        df['Part_%'] = df['Part_%'].apply(lambda s: s.replace(",", ""))
        df['Part_%'] = pd.to_numeric(df['Part_%'])/1000
        df.sort_values('Part_%', ascending=False, inplace=True)
        df['Part_%_acum'] = df['Part_%'].cumsum()
        df.reset_index(drop=True, inplace=True)
        return df
