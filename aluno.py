alunos = ["Ana", "Hugo", "Mariana", "Pedro", "Ana Paula"]

aluno_procurado = input("Digite um nome: ")
for Ana in alunos:
    if aluno_procurado.lower() in Ana.lower():
        print(Ana)