import pandas as pd
import numpy as np
import scrapy as cp
import requests

empresa = 'hapvida'
acao = 'HAPV3'
tipo = 'on'

url = f'https://br.advfn.com/bolsa-de-valores/bovespa/{empresa}-{tipo}-{acao}/historico/mais-dados-historicos?current=0&Date1=04/02/17&Date2=05/05/22'

# class="date-control date-control-right"
Select_ccs = 'html.fontawesome-i2svg-active.fontawesome-i2svg-complete body#afnmainbodid.ADVFN3 div div.exchanges-page div#container div.row div#content div.date-container table.control-container tbody tr td.edge-control a.date-control.date-control-right ::attr(href)'
xpath_href = '//a[contains(@class,"date-control date-control-right")]'

html = requests.get(url).content

sel = cp.Selector(text=html)

print(sel.css(Select_ccs).extract())
