import random

# valor = random.randint(1,20) # entre 1 e 20
# print(valor)

# print('Gerar cinco números aleatórios entre 1 e 50: \n')
# for i in range(5):
#     n = random.randint(1,50)
#     print(f'Número gerado {n}')

# valor = random.random()
# print(f'Número gerado {round(valor * 10, 2)}') # round pega o valor multiplicado por 10 flutuante e arredonda para duas casas decimais

# valor = random.uniform(1,100)
# print(f'Número: {round(valor, 4)}')

L = [2,4,6,9,10,13,14,16,20,22,25,30]
# n = random.choice(L) choite escolhe um número da lista
# print(f'Número escolhido: {n}')
# n = random.sample(L,3)  pega os elementos conforme o parametro que seria 3
# print(f'Número escolhido: {n}')

# Embaralhar
print(f'Exibir a lista original: {L}')
print(f'Ebaralhar a lista e exibi-la:')
n = random.shuffle(L)
print(L)


