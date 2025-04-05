#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 15:51:07 2025

@author: ricardo
"""
from flask import Flask
import requests
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')

def exibir_cotacoes():
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    requisicao_dic = requisicao.json()

    cotacao_dolar = float(requisicao_dic['USDBRL']['bid'])
    cotacao_euro = float(requisicao_dic['EURBRL']['bid'])
    cotacao_btc = float(requisicao_dic['BTCBRL']['bid'])

    hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    return (
        f'<h2>Cotação Atualizada em {hora}</h2>'
        f'<p><strong>Dólar:</strong> R${cotacao_dolar:.2f}</p>'
        f'<p><strong>Euro:</strong> R${cotacao_euro:.2f}</p>'
        f'<p><strong>Bitcoin:</strong> R${cotacao_btc:,.2f}</p>'
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

