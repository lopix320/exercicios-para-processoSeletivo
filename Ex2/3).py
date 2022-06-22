import json

diasMaioresMedia = 0
valorMaior = 0
valorMenor = 0
media = 0
i = 0
with open('dados.json') as arquivo:
    dados = json.load(arquivo)
    for dias in dados:
        media += dias.get('valor')
        i += 1
    media = media / i
    for dia in dados:
        if(dia.get('valor') > media):
            diasMaioresMedia += 1
        if(dia.get('valor') > valorMaior):
            valorMaior = dia.get('valor')
            valorMenor = valorMaior
        if(dia.get('valor') < valorMenor):
            valorMenor = dia.get('valor')

    print(f"Maior valor: {valorMaior}\nMenor valor: {valorMenor}\nDias maiores que a média mensal: {diasMaioresMedia}\nMedia Mensal: {media} ")
