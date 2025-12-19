pessoa = {"nome": "William", "idade": 30}
print(pessoa["nome"])
print(pessoa["idade"])

pessoas = []
for i in range(2):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    pessoa = {"nome": nome, "idade": idade}
    pessoas.append(pessoa)

print("Lista final:", pessoas)