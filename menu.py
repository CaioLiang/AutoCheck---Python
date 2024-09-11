from biblioteca import *

#AUTOCHECK NOTAS:
#Implementar TRY EXECPT
#Criar CRUD
#Saida de dados em JSON


# Dicionario de Usuários

lista_id = [0, 1, 2, 3, 4]
lista_nomes = ["admin", "allan.brito", "caio.liang", "levi.magni", "kaique.oliveira"]

dict_clientes = funcaoDictClientes(lista_id, lista_nomes)

#main

user = funcaoTelaLogin(dict_clientes, lista_id, lista_nomes)

while True:   
  
    print(f"\n{user}, Seja bem-vindo ao serviço de diagnóstico automotivo digital da Porto-Seguro! \n")
    
    print("╔═════════════════════════════════╗")
    print("║ **Bem-vindo ao Menu Principal** ║")
    print("║                                 ║")
    print("║ 1 - Consultar serviços          ║")
    print("║ 2 - Quero adquirir serviço      ║")
    print("║ 3 - Fale conosco                ║")
    print("║ 4 - Sair                        ║")
    print("╚═════════════════════════════════╝  \n")
    menu_principal = int(input("O que você quer fazer? Digite um número do menu: "))
    menu_principal = validacaoMatch(4, menu_principal)
    match menu_principal:
        case 1:
            funcaoConsultarServicos()
        case 2:
            funcaoAdquirirServico(user, lista_id, dict_clientes)        
        case 3:
            funcaoFaleConosco() 
        case 4:
            break
    
    manterLogin(user, dict_clientes, lista_id, lista_nomes)
           
    print("\n", dict_clientes)
    print("\n", lista_nomes)
    print("\n", lista_id)

print("\n", dict_clientes)
print("\n", lista_nomes)
print("\n", lista_id)
print("\nObrigado, volte sempre!")
#AUTOCHECK @2024