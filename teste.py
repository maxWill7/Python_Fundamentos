nome = input('Digite seu nome:')
idade = input('Digite sua idade:')
nota1 = float(input('Digite sua nota:'))
nota2 = float(input('Digite sua nota:'))
nota3 = float(input('Digite sua nota:'))
media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print(f'Parabéns {nome}, você foi aprovado!')
else:
    print(f'Infelizmente {nome}, você foi reprovado!')

# Lista vazia para guardar todos os alunos
alunos = []

# Vamos repetir 2 vezes (cadastrar 2 alunos)
for i in range(2):
    print(f"Cadastro do aluno {i+1}")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    # Cria um dicionário com os dados de UM aluno
    aluno = {"nome": nome, "idade": idade}

    # Adiciona esse aluno dentro da lista de alunos
    alunos.append(aluno)

    print("-" * 30)

# Depois do loop, mostramos todos os alunos cadastrados
print("Lista final de alunos:")
print(alunos)