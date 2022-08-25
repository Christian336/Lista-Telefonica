#Dicionario onde os contatos serao armazenados
contato = {}

#Funcao para inserir um novo contato
def inserir(nome,telefone,email,twitter,instagram):
  lista = []
  
  lista.append(telefone)
  lista.append(email)
  lista.append(twitter)
  lista.append(instagram)

  contato[nome] = lista

#Funcao para consultar os dados do contato pelo nome
def consulta(nome):
    print(contato[nome])

#Funcao para deletar o contato pelo nome
def deletar(nome):
  del contato[nome]

#Funcao para alterar os dados de um contato
def alterar(nome):
  
  novo_nome = input("Novo nome: ")
  contato[novo_nome] = contato[nome]
  del contato[nome]
  
  novo_telefone = int(input("Novo telefone: "))
  contato[novo_nome][0] = novo_telefone
 
  novo_email = input("Novo e-mail: ")
  contato[novo_nome][1] = novo_email

  novo_twitter = input("Novo Twitter: ")
  contato[novo_nome][2] = novo_twitter
 
  novo_instagram = input("Novo Intagram: ")
  contato[novo_nome][3] = novo_instagram

#Funcao para adicionar mais de um novo contato
def adicionar(num):
  for pessoa in range(num):
    lista= []
    nome = input("Nome: ")
    telefone = int(input("Telefone: "))
    email = input("e-mail: ")
    twitter = input("Twitter: ")
    instagram = input("Instagram: ")

    lista.append(telefone)
    lista.append(email)
    lista.append(twitter)
    lista.append(instagram)

    contato[nome] = lista

#Funcao que gerar um relatorio com os dados de todos os contatos
def relatorio():
  
  nomes = list(contato.keys())
  telefones =[]
  emails = []
  twitters = []
  instagrams = []
  print(f"{'Nro':<20} {'Nome':<20}  {'Telefone':<20}  {'e-mail':<20} {'Twitter':<20} {'Instagram':<20}")
  for num in range(len(contato)):
    pessoa = str(nomes[num])
    t= str(contato[pessoa][0])
    telefones.append(t)
    e = str(contato[pessoa][1])
    emails.append(e)
    tw = str(contato[pessoa][2])
    twitters.append(tw)
    i = str(contato[pessoa][3])
    instagrams.append(i)
    print(f'{num+1:<20}{nomes[num]:<20}{telefones[num]:<20}{emails[num]:<20} {twitters[num]:<20} {instagrams[num]:<20}')

#Funcao para salvar os dados dos contatos em ordem
def salvar():
  nomes = list(contato.keys())
  telefones =[]
  emails = []
  twitters = []
  instagrams = []
  for num in range(len(contato)):
    pessoa = str(nomes[num])
    telefones.append(contato[pessoa][0])
    emails.append(contato[pessoa][1])
    twitters.append(contato[pessoa][2])
    instagrams.append(contato[pessoa][3])
    print( "* %s,%r,%s,%s,%s" %(nomes[num],telefones[num],emails[num],twitters[num],instagrams[num]))
    

#Funcao Menu do Programa
def menu():
  print("################ Menu #################")
  print("(1) Inserir um novo contato;")
  print("(2) Consultar um nome já cadastrado;")
  print("(3) Remover um contato;")
  print("(4) Alterar um contato;")
  print("(5) Inserir novos contatos;")
  print("(6) Gerar um relatório dos contatos;")
  print("(7) Salvar dados dos contatos em ordem;")
  print("(8) Encerrar Programa;")

#Funcao para escolha de opcao
def decisao(opcao):
    if opcao == 1:
      nome = input("Nome:")
      telefone = int(input("Telefone: "))
      email = input("e-mail: ")
      twitter = input("Twitter: ")
      instagram = input("Instagram: ")
      inserir(nome,telefone,email,twitter,instagram)
    elif opcao == 2:
      nome = input("Nome: ")
      consulta(nome)
    elif opcao == 3:
      nome = input("Nome: ")
      deletar(nome)
    elif opcao == 4:
      nome = input("Nome: ")
      alterar(nome)
    elif opcao == 5:
      num = int(input("Digite o número de contatos que deseja adicionar: "))
      adicionar(num)
    elif opcao == 6:
      relatorio()
    elif opcao == 7:
      salvar()
    


while True:
  menu()  

  opcao = int(input("Selecione uma ação: "))

  if opcao == 8:
      break

  decisao(opcao)


