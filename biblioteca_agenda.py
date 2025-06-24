#0 Validação data

def validar_data(data):
    try:
        dia, mes, ano = data.split('/')
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        if 1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 2100:
            return True
        else:
            return False
    except ValueError:
        return False
        
#1 Adicionar Contatos

def adicionar_contato(agenda):
    nome = input("Digite o nome do contato: ")
    if nome.lower() in agenda:
        print("O contato já existe na agenda.")
        return

    telefone = None

    while True:
        telefone_entrada = input("Digite o telefone do contato: ")

        if len(telefone_entrada) != 14 or telefone_entrada[0] != '(' or telefone_entrada[3] != ')' or telefone_entrada[9] != '-':
            print("O telefone deve estar no formato (xx)xxxxx-xxxx. Tente novamente.")
        else:
            telefone  = telefone_entrada
            break 
        
    email = input("Digite o email do contato: ")
    data_alteracao = input("Digite a data de alteração do contato (no formato dd/mm/aaaa): ")
    while not validar_data(data_alteracao):
        print("A data deve estar no formato dd/mm/aaaa e ser uma data válida. Tente novamente.")
        data_alteracao = input("Digite a data de alteração do contato (no formato dd/mm/aaaa): ")

    agenda[nome.lower()] = {
        'nome': nome,
        'telefone': telefone,
        'email': email,
        'data_alteracao': data_alteracao
    }
    print(f'O contato {nome} foi adicionado.')

#2 Remover contatos

def remover_contato(agenda):
    nome=input("Insira o nome do contato que deseja remover:").lower()
    if nome.lower() not in agenda.keys():
      return "Contato inexistente!"
    else:
      agenda.pop(nome.lower())
    return "O contato foi removido com sucesso!"
    
#3 Atualizar Contatos

def atualizar_contato(agenda):
    nome=input("Digite o nome do contato a ser atualizado:").lower()

    if nome in agenda:
        agenda.pop(nome.lower())
        print("O contato existe na agenda, a partir de agora insira para atualizar")
        nome = input("Digite o nome do contato: ")
        
        telefone = None

        while True:
            telefone_entrada = input("Digite o novo telefone do contato: ")

            if len(telefone_entrada) != 14 or telefone_entrada[0] != '(' or telefone_entrada[3] != ')' or telefone_entrada[9] != '-':
                print("O telefone deve estar no formato (xx)xxxxx-xxxx. Tente novamente.")
            else:
                telefone  = telefone_entrada
                break 
            
        email = input("Digite o novo email do contato: ")
        data_alteracao = input("Digite a data de alteração do contato (no formato dd/mm/aaaa): ")
        while not validar_data(data_alteracao):
            print("A data deve estar no formato dd/mm/aaaa e ser uma data válida. Tente novamente.")
            data_alteracao = input("Digite a data de alteração do contato (no formato dd/mm/aaaa): ")

        agenda[nome.lower()] = {
            'nome': nome,
            'telefone': telefone,
            'email': email,
            'data_alteracao': data_alteracao
        }
        print(f'O contato {nome} foi atualizado.')


#4 Visualizar Agenda

def visualizar_agenda(agenda):
    for items in agenda.items():
        print(items[1])

#5 Filtrar contatos
        
def filtrar_contato(agenda):
    print("1. Filtrar por número de Telefone")
    print("2. Filtrar por email")
    print("3. Filtrar por data de alterção do contato")
        
    escolha=input("escolha uma das formas acima, para filtrar o contato, se o mesmo existir:")
        
    if escolha=="1":
        telefone = input("Digite o telefone do contato no formato (xx)xxxxx-xxxx : ")
        for items in agenda.items():
            if items[1]['telefone']== telefone:
                print(items[1])
            else:
                print("O número digitado não está na agenda!")
            
    
    if escolha=="2":
        email= input("Digite o email do contato: ")
        for items in agenda.items():
            if items[1]['email']== email:
                print(items[1])
            else:
                print("O email digitado não está na agenda!")
    if escolha=="3":
        data = input("Digite a data de alteração do contato (no formato dd/mm/aaaa): ")
        while not validar_data(data):
            print("A data deve estar no formato dd/mm/aaaa e ser uma data válida. Tente novamente.")
            data = input("Digite a data de alteração do contato (no formato dd/mm/aaaa): ")
        for items in agenda.items():
            if items[1]['data_alteracao']== data:
                    print(items[1])
            else:
                print("A data digitada não está associada a nenhum contato da agenda!")
        
            


