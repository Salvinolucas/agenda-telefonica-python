import biblioteca_agenda as ba

agenda = {}

while True:
    
    print("\n---- Agenda Telefônica ----")
    print("1. Adicionar contato")
    print("2. Remover contato")
    print("3. Atualizar contato")
    print("4. Visualizar todos os contatos") 
    print("5. Filtrar contato")
    print("6. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        ba.adicionar_contato(agenda)
    elif escolha == "2":
        ba.remover_contato(agenda)
    elif escolha == "3":
        ba.atualizar_contato(agenda)
    elif escolha=="4":
        ba.visualizar_agenda(agenda)
    elif escolha=="5":
        ba.filtrar_contato(agenda)
    elif escolha=="6":
        print("A agenda foi fechada!")
        break
    else:
        print("Opção inválida. Digite novamente.")

