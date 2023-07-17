def menu():
    print("1. Inserir Pessoa") 
    print("2. Listar pessoas cadastradas")
    print("3. Buscar pessoa por CPF")
    print("4. Buscar pessoa por telefone")
    print("5. Remover pessoa por CPF")
    print("6. Sair do Programa")

def inserir_telefone():
    lista_tel = []
    while True:
        tel = input("Digite o telefone do aluno: ")
        lista_tel.append(tel)
        print("Deseja inserir mais algum telefone?")
        print("1 - Sim | 2 - Não")
        chavetel = input("? ")
        if chavetel == "2":
            break
    return lista_tel

def inserir_aluno(dicionario):
    cpf = input("Digite o CPF do aluno: ")
    while cpf in dicionario:
        cpf = input("CPF já cadastrado, insira outro cpf: ")
    nome = input("Digite o nome do aluno: ")
    endereco = input("Digite o endereço do aluno")
    telefones = inserir_telefone()
    aluno = {"CPF": cpf, "Nome": nome, "Endereço": endereco, "Telefones": telefones}
    dicionario[cpf] = aluno
    print("Aluno cadastrado")

def remover_aluno(dicionario):
    cpf = input("Digite o CPF do aluno: ")
    if cpf in dicionario:
        del dicionario[cpf]
    else:
        print("CPF não encontrado")

def buscar_pessoa_por_telefone(dicionario):
    telefone_procurado = input("Digite o telefone da pessoa: ")
    for cpf, pessoa in dicionario.items():
        if telefone_procurado in pessoa["Telefones"]:
            return cpf
    return None

def buscar_pessoa_por_cpf(dicionario):
    cpf_procurado = input("Digite o CPF da pessoa que você quer encontrar: ")
    if cpf_procurado in dicionario:
        return cpf_procurado
    return None

def principal(dicionario):
    while True:
        menu()
        chave = input("Digite o valor correspondente à função desejada: ")

        if chave == '1':
            inserir_aluno(dicionario)
        elif chave == '2':
            if len(dicionario) == 0:
                print("Lista Vazia")
            else:
                for cpf, pessoa in dicionario.items():
                    print(f"CPF: {cpf}, Nome: {pessoa['Nome']}")
        elif chave == '3':
            cpf_encontrado = buscar_pessoa_por_cpf(dicionario)
            if cpf_encontrado:
                pessoa = dicionario[cpf_encontrado]
                print(f"CPF: {cpf_encontrado}, Nome: {pessoa['Nome']}, Endereço: {pessoa['Endereço']}, Telefones: {pessoa['Telefones']}")
            else:
                print("Pessoa não encontrada")
        elif chave == '4':
            cpf_encontrado = buscar_pessoa_por_telefone(dicionario)
            if cpf_encontrado:
                pessoa = dicionario[cpf_encontrado]
                print(f"CPF: {cpf_encontrado}, Nome: {pessoa['Nome']}, Endereço: {pessoa['Endereço']}, Telefones: {pessoa['Telefones']}")
            else:
                print("Pessoa não encontrada")
        elif chave == '5':
            remover_aluno(dicionario)
        elif chave == '6':
            print("Fim do programa!")
            break

dicionario = {}
principal(dicionario)