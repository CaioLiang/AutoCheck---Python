from biblioteca import *

#AUTOCHECK NOTAS:

# Dicionario de usuários

lista_id = []
lista_nomes = []

dict_usuarios = lerLogin()

for usuario in dict_usuarios:
    lista_id.append(usuario[0]) 
    lista_nomes.append(usuario[1])

dict_clientes = funcaoDictClientes(lista_id, lista_nomes)

dict_codDiagnostico = {}

lista_cod_diagostico = lerCodDiagnostico()

#main

user = funcaoTelaLogin(dict_clientes, lista_id, lista_nomes)

caminho = 'credenciais.json'

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
            funcaoAdquirirServico(user, lista_id, dict_clientes, lista_cod_diagostico)        
        case 3:
            funcaoFaleConosco() 
        case 4:
            break
    
    user = manterLogin(user, dict_clientes, lista_id, lista_nomes)

    excluiCredenciais(caminho)  

    #DEV       
    print("\n", dict_clientes)
    print("\n", lista_nomes)
    print("\n", lista_id)


excluiCredenciais(caminho)

print("\n", dict_clientes)
print("\n", lista_nomes)
print("\n", lista_id)


print("\nObrigado, volte sempre!")
#AUTOCHECK @2024