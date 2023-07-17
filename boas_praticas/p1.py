alunos = []
op = 0
while op < 5:
  op= int(input('1-adcionar aluno\n2-buscar aluno\n3-exibir em ordem alfabetica\n4-deletar aluno\n5-fechar programa\n'))
  if op == 1:
    alunos.append(input('informe o nome do aluno\n'))
  elif op == 2:
    call = False
    presa = input('informe o nome do aluno a ser buscado\n')
    for i in range(len(alunos)):
      if presa == alunos[i]:
        print(alunos[i])
        call = True
    if call == False:
      print('não encontrado')
  elif op == 3:
    alunos.sort()
    print(alunos)
  elif op == 4:
    presa = input('informe o nome do aluno a ser expurgado da existencia\n')
    call = False
    for i in range(len(alunos)):
      if presa == alunos[i]:
        print('deletando', alunos[i], ' ...')
        alunos.pop(i)
        call = True
    if call == False:
      print('não fui capaz de deletar a criança da existencia...')
      