Brasileirao = ('Palmeiras',
'Flamengo',
'Athletico-PR',
'Fluminense',
'Red Bull Bragantino',
'Bahia',
'Cruzeiro',
'Coritiba',
'São Paulo',
'Botafogo',
'Atlético-MG',
'Vitória',
'Corinthians',
'Internacional',
'Santos',
'Grêmio',
'Vasco da Gama',
'Mirassol',
'Remo',
'Chapecoense')

print('-'*50)
print(f'Os 5 primeiros colocados são {Brasileirao[:5]}')
print('-'*50)
print(f'Os 4 ultimos colocados são {Brasileirao[-4:]}')
print('-'*50)
print(f'Os times em ordem alfabetica {sorted(Brasileirao)}')
print('-'*50)
print(f'A Chape esta localizada na {Brasileirao.index('Chapecoense')+1}º posição')