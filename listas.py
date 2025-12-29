# lista: representa uma sequencia de valores
# sintaxe: nome_lista = [valores]
# n1 = [4,6,7,8,0,3]
# n2 = [1,6,3,0,12,6]
# valores = n1 + n2

# # acesando valores da lista
# print(valores[1])

# # último valor acessa pelo valor negativo
# print(valores[-1])

# atribuir um valor diferente na lista
# valores[0] = 9
# print(valores[0])

# # acessando um valor a partir do primeiro valor
# print(valores[2:6])

# # quantidade de elementos da lista
# print(len(valores))

# # uma versão ordenada da lista
# print(sorted(valores))
# # valores reverso da lsia
# print(sorted(valores, reverse=True))
# # soma dos valores da lista
# print(sum(valores))
# # valores minimo e máximo
# print(min((valores)))
# print(max((valores)))

# # acrescentar um valor na lista
# valores.append(13)
# print(valores)
# # remover o último valor da lista
# valores.pop()
# print(valores)
# # inserir um valor a partir de:
# valores.insert(3,5)
# print(valores)
# # verificar se existe um valor na lista
# print(17 in valores)

# planetas = ['Mercúrio', 'Vênus', 'Marte', 'Saturno']
# for planeta in planetas:
#     print(planeta)

bebidas = []

for i in range(3):
    print(f'\nDigite uma bebida favorita:')
    bebida = input()
    bebidas.append(bebida) # adiciona uma bebida na lista de bebidas

bebidas.sort() # ordena em oredem alfabética a lista

print(f'\nBebidas escolhidas')

for bebida in bebidas:
    print(bebida)

print(f'\nSaúde')    


