from webScraping import webScraping
""" 
    url1 = https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br
    url2 = https://sistemaswebb3-listados.b3.com.br/indexPage/theorical/IBOV?language=pt-br
    url3 = https://sistemaswebb3-listados.b3.com.br/indexPage/preview/IBOV?language=pt-br
 """
url1 = 'https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br'
url2 = 'https://sistemaswebb3-listados.b3.com.br/indexPage/theorical/IBOV?language=pt-br'
url3 = 'https://sistemaswebb3-listados.b3.com.br/indexPage/preview/IBOV?language=pt-br'


web1 = webScraping(url=url1)

#web2 = webScraping(url=url2)

#web3 = webScraping(url=url3)

print(web1)
