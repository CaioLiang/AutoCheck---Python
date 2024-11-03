from biblioteca import *
import os

#AUTOCHECK NOTAS:

# Dicionario de Usuários

lista_id = []
lista_nomes = []

dict_usuarios = lerLogin()

for usuario in dict_usuarios:
    lista_id.append(usuario[0]) 
    lista_nomes.append(usuario[1])

dict_clientes = funcaoDictClientes(lista_id, lista_nomes)

dict_codDiagnostico = {}

#main

user = funcaoTelaLogin(dict_clientes, lista_id, lista_nomes)

arquivo = 'credenciais.json'

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

    try: 
        os.path.exists(arquivo)
        os.remove(arquivo)
        print(f'O arquivo {arquivo} foi apagado com sucesso.')
    except:
        print(f'O arquivo {arquivo} não foi encontrado.')

    #DEV       
    print("\n", dict_clientes)
    print("\n", lista_nomes)
    print("\n", lista_id)

print("\n", dict_clientes)
print("\n", lista_nomes)
print("\n", lista_id)


print("\nObrigado, volte sempre!")
#AUTOCHECK @2024