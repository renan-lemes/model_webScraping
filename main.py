import pandas as pd
from selenium import webdriver
import time as t
from bs4 import BeautifulSoup


""" 
    url1 = https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br
    url2 = https://sistemaswebb3-listados.b3.com.br/indexPage/theorical/IBOV?language=pt-br
    url3 = https://sistemaswebb3-listados.b3.com.br/indexPage/preview/IBOV?language=pt-br
 """

url1 = 'https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br'
url2 = 'https://sistemaswebb3-listados.b3.com.br/indexPage/theorical/IBOV?language=pt-br'
url3 = 'https://sistemaswebb3-listados.b3.com.br/indexPage/preview/IBOV?language=pt-br'


def import_ibov_df(url='https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br'):
    browser = webdriver.Chrome()
    browser.get(url)
    browser.find_element_by_id('segment').send_keys('Setor de Atuação')
    t.sleep(3)
    browser.find_element_by_id('selectPage').send_keys('120')
    t.sleep(3)
    html = browser.page_source
    browser.close()
    bs = BeautifulSoup(html, 'html.parser')
    setor, cod, acao, tipo, qtde_t, part, part_a = [], [], [], [], [], [], []
    linhas = bs.find_all()
    i = 0
    print(linhas)
    while i < (len(linhas)):
        setor.append(linhas[i].text)
        cod.append(linhas[i+1].text)
        acao.append(linhas[i+2].text)
        tipo.append(linhas[i+3].text)
        qtde_t.append(linhas[i+4].text)
        part.append(linhas[i+5].text)
        part_a.append(linhas[i+6].text)
        i += 7

        df = pd.DataFrame({'Setor': setor[:-1],
                           'Acao': cod[:-1],
                           'Empresa': acao[:-1],
                           'Qntd_teorica': qtde_t[:-1],
                           'Part_%': part[:-1]})

        # Separando os setores e subsetores em colunas
        df['SubSetor'] = df['Setor'].apply(
            lambda s: s[s.rfind('/')+1:].strip())
        df['Setor'] = df['Setor'].apply(lambda s: s[:s.rfind('/')])

        # Convertendo os valores de string para int
        df['Qntd_teorica'] = df['Qntd_teorica'].apply(
            lambda s: s.replace(".", ""))
        df['Qntd_teorica'] = pd.to_numeric(df['Qntd_teorica'])
        df['Part_%'] = df['Part_%'].apply(lambda s: s.replace(",", ""))
        df['Part_%'] = pd.to_numeric(df['Part_%'])/1000
        df.sort_values('Part_%', ascending=False, inplace=True)

        # Criando uma colunas com a % acumulada
        df['Part_%_acum'] = df['Part_%'].cumsum()
        df.reset_index(drop=True, inplace=True)
        return df


df = import_ibov_df()

print(df)
#web2 = webScraping(url=url2)

#web3 = webScraping(url=url3)


# print(web2)
# print(web3)
