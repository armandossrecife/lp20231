def adicionar_aluno(alunos):
    nome = input('Informe o nome do aluno: ')
    alunos.append(nome)

def buscar_aluno(alunos):
    nome = input('Informe o nome do aluno a ser buscado: ')
    if nome in alunos:
        print(nome)
    else:
        print('Aluno não encontrado.')

def exibir_em_ordem_alfabetica(alunos):
    alunos.sort()
    print(alunos)

def deletar_aluno(alunos):
    nome = input('Informe o nome do aluno a ser expurgado da existência: ')
    if nome in alunos:
        alunos.remove(nome)
        print(f'Deletando {nome}...')
    else:
        print('Não foi possível deletar o aluno.')

def menu_opcoes():
    print('1 - Adicionar aluno') 
    print('2 - Buscar aluno')
    print('3 - Exibir em ordem alfabética')
    print('4 - Deletar aluno')
    print('5 - SAIR')

def principal(alunos):
    while True:
        menu_opcoes()
        op = input('Qual a sua opção? ')
        if op == '1':
            adicionar_aluno(alunos)
        elif op == '2':
            buscar_aluno(alunos)
        elif op == '3':
            exibir_em_ordem_alfabetica(alunos)
        elif op == '4':
            deletar_aluno(alunos)
        elif op == '5':
            break

alunos = []
principal(alunos)