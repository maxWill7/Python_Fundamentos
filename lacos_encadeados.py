# for cont_ex in range(1,6):
#     print(f'\nRodada: {cont_ex}')
#     for cont_int in range(5, 0, -1):
#         print(f'Valor: {cont_int}')

# print('Laços encadeados!')

import random

for A in range(1,6):
    print(f'\nConjunto {A}')
    for B in range(5):
        num = random.randint(1,1000)
        print(f'Valor: {num}')
