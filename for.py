# lista = [1,5,13,7,9,10,0,3]
# palavra = 'will'

# for i in lista:
#     print(i)

# for letra in palavra:
#     print(letra)

# for numero in range(11):
#     print(numero)

# nome = input('Digite seu nome:')
# for x in range(5):
#     print(f'{x+1} {nome}')

# range(valor_inicial, valor_final, incremento)
# for x in range(2,20,4):
#     print(x)

pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamante', 'Turmalina')

for pedra in pedras:
    if pedra == 'Quartzo':
        continue # continue significa que o laço for vai continuar e elimina o que esta dentro do if
    print(pedra)