from cgitb import html
import pandas as pd
from selenium import webdriver
import time as t
from bs4 import BeautifulSoup


class webScraping:
    def import_ibv2(url="https://sistemaswebb3-listados.b3.com.br/indexPage/theorical/IBOV?language=pt-br"):

        browser = webdriver.Chrome()
        browser.get(url)
        t.sleep(2)
        browser.find_element_by_id('selectPage').send_keys('120')
        t.sleep(2)
        html = browser.page_source
        browser.close()
        bs = BeautifulSoup(html, 'html.parser')
        linhas = bs.find_all('td')
        linhas = linhas
        # print(len(linhas))
        # print(linhas)
        i = 0
        lista_act = []
        while i < (len(linhas)):
            lista_act.append(linhas[i].text)
            i += 1
        codigo = []
        j = 0
        while j < (len(lista_act)-8):
            codigo.append(lista_act[j])
            j += 5
        j = 1
        acao = []
        while j < (len(lista_act)-5):
            acao.append(lista_act[j])
            j += 5
        j = 2
        tipo = []
        while j < (len(lista_act)-6):
            tipo.append(lista_act[j])
            j += 5
        qtd_t = []
        j = 3
        while j < (len(lista_act)-7):
            qtd_t.append(lista_act[j])
            j += 5
        j = 4
        part_p = []
        while j < (len(lista_act)-6):
            part_p.append(lista_act[j])
            j += 5
        df = pd.DataFrame({
            'Codigo': codigo,
            'Acao': acao,
            'Tipo': tipo,
            'Qtde_Teo': qtd_t,
            'Part_%': part_p,
        })
        return df
