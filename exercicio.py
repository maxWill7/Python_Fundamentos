alunos = []

for i in range(3):
    print(f"Cadastro do aluno {i+1}")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3

    if media >= 6:
        status = "Aprovado"
    else:
        status = "Reprovado"

    aluno = {
        "nome": nome,
        "idade": idade,
        "notas": [nota1, nota2, nota3],
        "media": media,
        "status": status
    }

    alunos.append(aluno)
    print("-" * 30)

print("\nResultados finais:")
for aluno in alunos:
    print(f"Aluno {aluno['nome']} ({aluno['idade']} anos) teve média {aluno['media']:.1f} e está {aluno['status']}")