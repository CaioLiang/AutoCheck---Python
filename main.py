from biblioteca import *

#AUTOCHECK NOTAS:
#Criar CRUD
#Documentar as novas funções
#Saida de dados em JSON
#Verificar 


# Dicionario de Usuários

lista_id = [0, 1, 2, 3, 4]
lista_nomes = ["admin", "allan.brito", "caio.liang", "levi.magni", "kaique.oliveira"]

dict_clientes = funcaoDictClientes(lista_id, lista_nomes)

dict_codDiagnostico = {}

#main

user = funcaoTelaLogin(dict_clientes, lista_id, lista_nomes)


while True:   
  
    print(f"\n{user}, Seja bem-vindo ao serviço de diagnóstico automotivo digital da Porto-Seguro! \n")
    
    print("╔═════════════════════════════════╗")
    print("║ **Bem-vindo ao Menu Principal** ║")
    print("║                                 ║")
    print("║ 1 - Informações                 ║")
    print("║ 2 - Serviços                    ║")
    print("║ 3 - Fale conosco                ║")
    print("║ 4 - Sair                        ║")
    print("╚═════════════════════════════════╝")
    
    menu_principal = tryExceptInputMenu("\nO que você quer fazer? Digite um número do menu: ")
    
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
    
    user = manterLogin(user, dict_clientes, lista_id, lista_nomes)
    
    #DEV       
    print("\n", dict_clientes)
    print("\n", lista_nomes)
    print("\n", lista_id)

print("\n", dict_clientes)
print("\n", lista_nomes)
print("\n", lista_id)


print("\nObrigado, volte sempre!")
#AUTOCHECK @2024