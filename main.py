from webScraping import webScraping
""" 
    url1 = https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br
    url2 = https://sistemaswebb3-listados.b3.com.br/indexPage/theorical/IBOV?language=pt-br
    url3 = https://sistemaswebb3-listados.b3.com.br/indexPage/preview/IBOV?language=pt-br
 """
url1 = 'https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br'
url2 = 'https://sistemaswebb3-listados.b3.com.br/indexPage/theorical/IBOV?language=pt-br'
url3 = 'https://sistemaswebb3-listados.b3.com.br/indexPage/preview/IBOV?language=pt-br'


lista1 = webScraping(url=url1)

lista2 = webScraping(url=url2)

lista3 = webScraping(url=url3)
