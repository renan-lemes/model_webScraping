from webScraping import webScraping

df = webScraping(
    url="https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br")


print(df.meth())
