#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 15:51:07 2025

@author: ricardo
"""

import requests
from datetime import datetime
'''
requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

requisicao_dic = requisicao.json()
cotacao_dolar = requisicao_dic['USDBRL']['bid']
cotacao_euro = requisicao_dic['EURBRL']['bid']
cotacao_btc = requisicao_dic['BTCBRL']['bid']

print(f'Cotação Atualizada. {datetime.now()}\nDólar: R${cotacao_dolar}\nEuro: R${cotacao_euro}\nBTC: R${cotacao_btc}')
'''
requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
requisicao_dic = requisicao.json()

# Extraindo as cotações e convertendo para float
cotacao_dolar = float(requisicao_dic['USDBRL']['bid'])
cotacao_euro = float(requisicao_dic['EURBRL']['bid'])
cotacao_btc = float(requisicao_dic['BTCBRL']['bid'])

# Exibindo as cotações com 2 casas decimais
print(f'Cotação Atualizada. {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
print(f'Dólar: R${cotacao_dolar:.2f}')
print(f'Euro: R${cotacao_euro:.2f}')
print(f'BTC: R${cotacao_btc:,.2f}')













