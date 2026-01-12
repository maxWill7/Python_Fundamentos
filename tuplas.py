# tuplas são imutáveis,não pode ser modificadas

halogenios = ('f', 'cl', 'br', 'i', 'at')
gases_nobres = ('he', 'ne', 'ar', 'xe', 'kr', 'rn')
elementos = halogenios + gases_nobres
t1 = (5,8,44,15,5,7,9,4,8,7)
print(max(t1))

# operações não disponíveis em tuplas: .sort(), .append(), .reverse(), .pop()

# for elemento in elementos:
#     print(f'Elemento químico: {elemento}')

# lista a partir de uma tupla

# grupo2 = list(halogenios)
# grupo2[0] = 'h'
# print(grupo2)

grupo1 = ['li', 'na', 'k', 'rb', 'cs', 'fr']
alcalinos = tuple(grupo1)
print(type(alcalinos))

