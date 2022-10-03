from functools import partialmethod
import requests
import json
import pandas as pd


def eleicoes_data():
    data=requests.get('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')

    json_data = json.loads(data.content)

    candidato =[]
    partido = []
    votos = []
    porcentagem = []

    for informacoes in json_data['cand']:
        if informacoes['seq'] in ['1','2','3','4']:
            candidato.append(informacoes['nm'])
            partido.append(informacoes['cc'])
            votos.append(informacoes['vap'])
            porcentagem.append(informacoes['pvap'])
            

    eleicoes_dados = pd.DataFrame(list(zip(candidato,votos,porcentagem, partido)), columns=('Candidato','N_votos','porcentagem','partido'))

    print(eleicoes_dados)
eleicoes_data()