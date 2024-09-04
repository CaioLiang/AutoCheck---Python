def cadastrarCliente (id, nome, dict_clientes, lista_id, lista_nomes):
    dict_clientes[nome] = {id : ()}
    lista_id = lista_id.append(id)
    lista_nomes = lista_nomes.append(nome)

def cadastrarCodDiagnostico (id, nome, cod_diagnostico, dict_clientes):
    if user in dict_clientes.keys():
        lista_key = list(dict_clientes[nome].keys())
        id = lista_key[0]
    #integração no formato {asda : asdasd:{adasd}}
    lista_cod_diagnostico_atual = (dict_clientes[nome][id])
    dict_clientes[nome][id] = lista_cod_diagnostico_atual + (cod_diagnostico, ) 

dicionario_infos = {"consulta": {
                1: 
                    ("\nDIAGNÓSTICO " + 
                "\n\nDescrição: \n"+
                "\nRealiza o diagnóstico do problema do automóvel através do código de falha, "+
                "podendo ser fornecido diretamente ou diagnosticado conforme responda aos campos do decorrer das solicitações do programa. " + 
                "Após esse processo, o programa envia para a CAPS mais qualificada sobre o diagnóstico e agendando a visita futura, mostrando o código de falha, CAPS que irá realizar o atendimento e o Código de Diagnóstico.\n"),
                2: 
                    ("\nCENTRO AUTOMOTIVO MAIS PRÓXIMO " + 
                "\n\nDescrição: \n"+
                "\nInforma sobre as CAPS (Centro Automotivo Porto Seguro) mais próximos conforme sua localização.\n"),
                3:     
                    
                    ("\nACOMPANHAR DIAGNÓSTICO " + 
                "\n\nDescrição: \n"+
                "\nMostra o status de um diagnóstico já realizado anteriormente, para isso, precisa-se do código do diagnóstico fornecido, assim, informa sobre qual CAPS aguarda a chegada do cliente.\n"),
                4: 
                    ("\nFEEDBACK | FALE CONOSCO " + 
                "\n\nDescrição: \n"+
                "\nOpção que registra as opiniões e comentários dos usuários do aplicativo, sendo possível verificação do comentário registrado no site.\n")
                }}

def validacaoMatch(tamanho_max , numero_digitado):
    """
    Função para verificar se algum número está dentro das opções de um Match definido por algarismos em ordem crescente,
    assim, é solicitado o maior número dentro das opções possíveis e o número a ser verificado, com retorno de um número 
    válido dentro do intervalo de 1 até o maior número enviado.


    :param tamanho_max: int contendo a última opção de um match de números
    :param numero_digitado: int do número digitado pelo usuário
    :return: int de um número dentro das opções do match
    """
    lista_tam = []
    for i in range(1, tamanho_max+1, 1):
        lista_tam.append(i)
    while(True):
        if(numero_digitado in lista_tam):
            break
        else: 
            print(f"A opção digitada: '{numero_digitado}' não é uma das opções. Possiveis opções : {lista_tam}")
        numero_digitado = int(input("Digite uma opção: "))    
    return numero_digitado
     
def geraCodDiagnostico():
    """
    Função para gerar um número alaleatório entre 10000000 e 99999999.

    :return: int de um número aleatório entre 10000000 e 99999999
    """
    import random
    codigo_diagnostico = random.randint(10000000, 99999999)
    return codigo_diagnostico

def validaCodigoDiagnostico(cod_diagnostico):
    """
    Função para verificar se o código de dianóstico é válido , caso não, é solicitado ao usuário novamente em looping até a inserção 
    de um código válido e o retornando.  

    :param cod_diagnostico: int contendo o código de diagnóstico
    :return: int de um código de dignóstico válido
    """
    while True:
        if(cod_diagnostico >= 10000000 and cod_diagnostico <= 99999999):
            break
        print(f"\nO código '{cod_diagnostico}' digitado não é válido!\n"+
        "O formato do código são 8 digitos números inteiros entre 10000000 a 99999999.")
        cod_diagnostico = int(input("Digite novamente o código de diagnóstico: "))
    return cod_diagnostico

def validaAno(automovel_ano):
    """
    Função para verificar se o ano digitado de um automóvel está entre o intervalo 
    determinado de 1885 e 2024.  

    :param automovel_ano: int contendo o ano do automóvel 
    :return: int do ano do automóvel dentro do prazo determinado
    """
    while True:
        if(automovel_ano >= 1885 and automovel_ano <= 2024):
            break
        print(f"\nAno '{automovel_ano}' não é válido!\n"+
        "As datas devem estar no intervalo de 1885-2024.")
        automovel_ano = int(input("Digite novamente o ano do automóvel: "))
    return automovel_ano

def validaMinCaracteres(texto, quantidade_min, texto_pergunta):
    """
    Função que recebe um texto para ser validado com uma quantidade de mínima de caracteres que deve conter, assim, 
    fica em looping até a entrada de um texto válido.  

    :param texto: String contendo o texto a ser verificado pela sua quantidade de caracteres
    :param quantidade_min: int contendo a quantidade mínima (igual ou maior) de caracteres obrigatório no texto 
    :param texto_pergunta: String contendo o texto da pergunta 
    :return: String contendo o texto com a quantidade obrigatória de caracteres
    """
    texto = str(texto)
    while len(texto) < quantidade_min:
        print(f"\nQuantidade de caracteres insuficientes!")
        texto = str(input(texto_pergunta))
    return texto

def validaCodFalha(cod_falha):
    """
    Função que valida o código de falha conforme formato de 5 caracteres com o primeiro caractere 
    sendo a definição de qual sistema afetado do automóvel.   

    :param cod_falha: String contendo o código de falha do automóvel
    :return: String do código de falha válido
    """
    cod_falha = str(cod_falha)
    while True:
        while len(cod_falha) != 5:
            print(f"\nQuantidade de caracteres inválido!")
            print("Formato esperado: CAAAA \nNota: C = Caracteres | A = Algarismos\n")
            cod_falha = str(input("Digite o código de falha: "))
        check_cod_falha_qntd = True 
        cod_falha_separado = separaString(cod_falha)
        PrimeiroCaracter = ["B", "C", "P", "U"]
        while cod_falha_separado[0] not in PrimeiroCaracter:
            print(f"\nPrimeiro Dígito Inválido")
            print("Formato esperado: CAAAA \nNota: C = Caracteres | A = Algarismos\n")
            print("Caracteres esperados: B, C, P, U\n")
            cod_falha = str(input("Digite o código de falha: "))
            check_cod_falha_qntd = False
            cod_falha_separado = separaString(cod_falha)
        check_cod_falha_primeiro_caractere = True
        if(check_cod_falha_qntd and check_cod_falha_primeiro_caractere):
            break
    return cod_falha
    
def separaString(palavra):
    """
    Função que separa as letras de uma determinada palavra com espaços em branco.

    :param palavra: String contendo a palavra que as letras serão separadas por espaços brancos
    :return: String contendo a palavra que entre as letras está separada por espaços brancos
    """
    palavra_separada = ""
    for letra in palavra:
        palavra_separada = palavra_separada + letra + " "
    return palavra_separada

#SISTEMA

def funcaoTelaLogin():
    
    print("***** AUTOCHECK - PORTO SEGURO ***** \n")
    print("╔═════════════════════════════════╗")
    print("║    **Bem-vindo à AutoCheck**    ║")
    print("║                                 ║")
    print("║ 1 - Login                       ║")
    print("║ 2 - Criar conta                 ║")
    print("╚═════════════════════════════════╝  \n")
    
    tela_login_menu = int(input("\nDigite um número do menu acima: "))
    tela_login_menu = validacaoMatch(2, tela_login_menu)
    
    if tela_login_menu == 1: 
        while True:
            user = input("Digite nome do seu usuario: ")
            #validar
            if user in dict_clientes.keys():
                print("Login realizado com sucesso!")
                return user
            print(f"Usuário: {user}. Não cadastrado!. Tente novamente!")        
    else:
        #validar
        user = input("Digite nome do seu usuario: ")
        while True:
            if user in dict_clientes.keys():
                print("Usuário já possui cadastro!")
            else:       
                cadastrarCliente((len(lista_id)), user, dict_clientes, lista_id, lista_nomes)
                return user       
            user = input("Digite nome do seu usuario: ")

def funcaoConsultarServicos():
    '''
    Procedimento de consulta dos serviços disponíveis com uma breve descrição de suas funções.
    '''
    print("\nAtualmente as funcionalidades do aplicativo são: \n")
    print("╔════════════════════════════════════════╗")
    print("║            **CONSULTA**                ║")
    print("║                                        ║")
    print("║ 1 - Diagnóstico                        ║")
    print("║ 2 - Centro Automotivo mais próxima     ║")
    print("║ 3 - Acompanhar diagnóstico             ║")
    print("║ 4 - Feedback | Fale conosco            ║")     
    print("╚════════════════════════════════════════╝  \n")

    consulta_menu = int(input("\nDigite o número que você quer mais detalhes: "))
    consulta_menu = validacaoMatch(4, consulta_menu)
    
    #dicionario que substitui o match case

    print(dicionario_infos["consulta"][consulta_menu])
    
    # match consulta_menu:
         
        # case 1:
        #     print("\nDIAGNÓSTICO " + 
        #         "\n\nDescrição: \n"+
        #         "\nRealiza o diagnóstico do problema do automóvel através do código de falha, "+
        #         "podendo ser fornecido diretamente ou diagnosticado conforme responda aos campos do decorrer das solicitações do programa. " + 
        #         "Após esse processo, o programa envia para a CAPS mais qualificada sobre o diagnóstico e agendando a visita futura, mostrando o código de falha, CAPS que irá realizar o atendimento e o Código de Diagnóstico.\n")
        # case 2: 
        #     print("\nCENTRO AUTOMOTIVO MAIS PRÓXIMO " + 
        #         "\n\nDescrição: \n"+
        #         "\nInforma sobre as CAPS (Centro Automotivo Porto Seguro) mais próximos conforme sua localização.\n")
        # case 3:
        #     print("\nACOMPANHAR DIAGNÓSTICO " + 
        #         "\n\nDescrição: \n"+
        #         "\nMostra o status de um diagnóstico já realizado anteriormente, para isso, precisa-se do código do diagnóstico fornecido, assim, informa sobre qual CAPS aguarda a chegada do cliente.\n")
        # case 4: 
        #     print("\nFEEDBACK | FALE CONOSCO " + 
        #         "\n\nDescrição: \n"+
        #         "\nOpção que registra as opiniões e comentários dos usuários do aplicativo, sendo possível verificação do comentário registrado no site.\n")

def funcaoAdquirirServico(user):
    '''
    Procedimento de adquirir um serviço da AutoCheck, na qual proporciona: Diagnóstico, Centro Automotivo mais próximo e Acompanhar diagnóstico.
    '''
    print("\nOlá, esses são os serviços do Centro Automotivo Porto Seguro: \n")
    print("╔════════════════════════════════════════╗")
    print("║            **SERVIÇOS**                ║")
    print("║                                        ║")
    print("║ 1 - Diagnóstico                        ║")
    print("║ 2 - Centro Automotivo mais próximo     ║")
    print("║ 3 - Acompanhar diagnóstico             ║")     
    print("╚════════════════════════════════════════╝  \n")
    
    servico_menu = int(input("\nDigite uma das opções: "))
    servico_menu = validacaoMatch(3, servico_menu)
    match servico_menu: 
        case 1:
            print("\nEntendo, preciso de mais informações do seu automóvel: \n" +
            "Preencha os seguintes campos: \n")
            automovel_ano = int(input("Ano: "))
            automovel_ano = validaAno(automovel_ano)
            automovel_montadora = input("Montadora: ")
            automovel_montadora = validaMinCaracteres(automovel_montadora, 3, "Montadora: ")
            automovel_modelo = input("Modelo: ")
            automovel_modelo = validaMinCaracteres(automovel_modelo, 3, "Modelo: ")
            automovel_motor = input("Motor: ")
            automovel_motor = validaMinCaracteres(automovel_motor, 7, "Motor: ")
            print("\n\nSobre o código de falha: \n")
            print("╔════════════════════════════════════════╗")
            print("║           **INFORMAÇÕES**              ║")
            print("║                                        ║")
            print("║ 1 - Tenho o Código de Falha            ║")
            print("║ 2 - Não tenho o Código de Falha        ║")     
            print("╚════════════════════════════════════════╝  \n")


            diagnostico_codigo_falha = int(input("\nDigite uma das opções: "))
            diagnostico_codigo_falha = validacaoMatch(2, diagnostico_codigo_falha)
            match diagnostico_codigo_falha: 
                case 1: 
                    cod_falha_usuario = input("Digite o código de falha: ")
                    cod_falha_usuario = validaCodFalha(cod_falha_usuario)
                    sintomas_automovel = input("Entendo, descreve o problema do seu automóvel: ") 
                    sintomas_automovel = validaMinCaracteres(sintomas_automovel, 10, "Entendo, descreve o problema do seu automóvel: ")
                    print("\nSucesso, seu diagnóstico foi encaminhado para : CENTRO AUTOMOTIVO - BELA VISTA - RUA PEDROSO. Entraremos em contato em breve! \n")
                    print(f"Código de Falha: {cod_falha_usuario}")
                    print("Descrição da falha: Em análise.")
                    print("Orçamento prévio: Em análise")
                    cod_diagnostico = geraCodDiagnostico()
                    print(f"Código do Diagnóstico: {cod_diagnostico}\n")
                case 2:
                    sintomas_automovel = input("Entendo, descreve o problema do seu automóvel: ") 
                    sintomas_automovel = validaMinCaracteres(sintomas_automovel, 10, "Entendo, descreve o problema do seu automóvel: ")
                    print("\nConforme seu relato sobre o estado do carro, \n" + 
                    "As possiveis áreas afetadas são: \n")
                    print("╔════════════════════════════════════════╗")
                    print("║           **ÁREA AFETADA**             ║")
                    print("║                                        ║")
                    print("║ 1 - Elétrica                           ║")
                    print("║ 2 - Mecânica                           ║")     
                    print("╚════════════════════════════════════════╝  \n")
                    
                    
                        
                    area_afetada = int(input("Digite um das opções : "))
                    area_afetada = validacaoMatch(2, area_afetada)
                    
                    print("\nPossui mais detalhes da causa do problema? \n")  
                    print("╔════════════════════════════════════════╗")
                    print("║         **DETALHES DA CAUSA**          ║")
                    print("║                                        ║")
                    print("║ 1 - SIM                                ║")
                    print("║ 2 - NÃO                                ║")     
                    print("╚════════════════════════════════════════╝  \n")

                    conhecimento_causa = int(input("Digite uma das opções: ") )
                    conhecimento_causa = validacaoMatch(2, conhecimento_causa)
                    if(conhecimento_causa == 1):
                        
                        #implementar biblioteca PANDAS
                        dict_cod_falha = {
                        #"cod_falha": ("descrição tecnica", valor estimado)
                        "C0800": ("Tensao Bateria Tensão da bateria", 340.00),   
                        "P0645": ("ArCondicionado Ar Condicionado", 998.30),                                  
                        "P0087": ("PressaoSistema Pressão do sistema", 256.90),                                   
                        "P0300": ("FalhaIgnicao Falha de ignição", 40.00),                                   
                        "P0418": ("Rele Bomba Ar Rele da bomba de ar", 49.80),                                                            
                        "P0650": ("Mau funcionamentodocircuitode controle daluz", 340.00),   
                        "P1712": ("SensVelocRodaDD Sensor de velocidade da roda dianteira direita", 134.44),
                        "P0217": ("TemperaturaMotor Temperatura do motor", 70.41),
                        "P0263": (" Cilindro1– Falhade balanceamento", 100.13),
                        "C0238": ("SensVelocidRoda Sensor de velocidade da roda", 200.39),
                        "P0805": ("Mau funcionamentodocircuitodosensorde posiçãodaembreagem", 120.85),
                        "P0381": ("Mau funcionamentodocircuitoindicadordasvelasaquecedora", 278.24),                              
                        "Em análise": ("Em análise", 0.00)
                        }
                        
                        match area_afetada:
                            case 1:
                                print("\nEntre as possiveis falhas estão: \n")  
                                print("╔════════════════════════════════════════════╗")
                                print("║         **POSSÍVEL FALHA ELÉTRICA**        ║")
                                print("║                                            ║")
                                print("║ 1 - Bateria                                ║")
                                print("║ 2 - Ar condicionado                        ║")
                                print("║ 3 - Sistema eletrônico e sensores          ║")
                                print("║ 4 - Sistema de Ignição                     ║")
                                print("║ 5 - Fusíveis e Relés                       ║")
                                print("║ 6 - Luzes e Faróis                         ║")
                                print("║ 7 - Alternador e o regulador de voltagem   ║")
                                print("║ 8 - Outros                                 ║")    
                                print("╚════════════════════════════════════════════╝  \n")
                                
                                
                                falha_eletrica = int(input("Digite um número do menu: "))
                                falha_eletrica = validacaoMatch(8, falha_eletrica)     
                                match falha_eletrica:
                                    case 1:                                     
                                        # descricao_codfalha = "Tensao Bateria Tensão da bateria"
                                        cod_falha = "C0800"
                                        # orcamento_previo = 340.00  
                                    case 2:
                                        # descricao_codfalha = "ArCondicionado Ar Condicionado"
                                        cod_falha = "P0645"
                                        # orcamento_previo = 998.30
                                    case 3:
                                        # descricao_codfalha = "PressaoSistema Pressão do sistema"
                                        cod_falha = "P0087" 
                                        # orcamento_previo = 256.90
                                    case 4:
                                        # descricao_codfalha = "FalhaIgnicao Falha de ignição"
                                        cod_falha = "P0300"
                                        # orcamento_previo = 40.00
                                    case 5:
                                        # descricao_codfalha = "Rele Bomba Ar Rele da bomba de ar"
                                        cod_falha = "P0418"
                                        # orcamento_previo = 133.00
                                    case 6:
                                        # descricao_codfalha = "Mau funcionamentodocircuitode controle daluz"
                                        cod_falha = "P0650"
                                        # orcamento_previo = 49.80
                                    case 7:
                                        # descricao_codfalha = "Alternador Alternador"
                                        cod_falha = "P0620"
                                        # orcamento_previo = 580.00
                                    case 8:
                                        # descricao_codfalha = "Em análise"
                                        # orcamento_previo = "Em análise"
                                        cod_falha = "Em análise"
                    
                                print("\nSucesso, seu diagnóstico foi encaminho para : CENTRO AUTOMOTIVO - BELA VISTA - RUA PEDROSO. Entraremos em contato em breve! \n") 
                                print(f"Código de Falha: {cod_falha}")
                                print(f"Descrição da falha: {dict_cod_falha[cod_falha][0]}")
                                print("Orçamento prévio: R$: {:.2f}".format(float(dict_cod_falha[cod_falha][1])))
                                cod_diagnostico = geraCodDiagnostico()
                                print(f"Código do Diagnóstico: {cod_diagnostico}\n")
                            
                            case 2: 
                                
                                print("\nEntre as possiveis falhas estão: \n")  
                                print("╔════════════════════════════════════════════╗")
                                print("║        **POSSÍVEIS FALHA MECÂNICA**        ║")
                                print("║                                            ║")
                                print("║ 1 - Alinhamento                            ║")
                                print("║ 2 - Arrefecimento                          ║")
                                print("║ 3 - Balanceamento e Geometria              ║")
                                print("║ 4 - Discos e Pastilhas de Freio            ║")
                                print("║ 5 - Embreagens                             ║")
                                print("║ 6 - Filtros e Velas de Ignição             ║")
                                print("║ 7 - Outros                                 ║")   
                                print("╚════════════════════════════════════════════╝  \n")

                                falha_mecanica = input("O que você quer fazer? Digite um número do menu: ")
                                falha_mecanica_convertido = int(falha_mecanica)
                                falha_mecanica_convertido = validacaoMatch(7, falha_mecanica_convertido)
                
                                match falha_mecanica_convertido:
                                    case 1:
                                        # descricao_codfalha = "SensVelocRodaDD Sensor de velocidade da roda dianteira direita"
                                        cod_falha = "P1712"
                                        # orcamento_previo = 134.44                                       
                                    case 2:
                                        # descricao_codfalha = "TemperaturaMotor Temperatura do motor"
                                        cod_falha = "P0217"
                                        # orcamento_previo = 70.14 
                                    case 3:
                                        # descricao_codfalha = "Cilindro1– Falhade balanceamento "
                                        cod_falha = "P0263" 
                                        # orcamento_previo = 100.13 
                                    case 4:
                                        # descricao_codfalha = "SensVelocidRoda Sensor de velocidade da roda"
                                        cod_falha = "C0238"
                                        # orcamento_previo = 200.39 
                                    case 5:
                                        # descricao_codfalha = "Mau funcionamentodocircuitodosensorde posiçãodaembreagem"
                                        cod_falha = "P0805"
                                        # orcamento_previo = 120.85 
                                    case 6:
                                        # descricao_codfalha = "Mau funcionamentodocircuitoindicadordasvelasaquecedora"
                                        cod_falha = "P0381"
                                        # orcamento_previo = 278.24 
                                    case 7:
                                        # descricao_codfalha = "Em análise"
                                        cod_falha = "Em análise"
                                        # orcamento_previo = 0 

                                print("\nSucesso, seu diagnóstico foi encaminhado para : CENTRO AUTOMOTIVO - BELA VISTA - RUA PEDROSO. Entraremos em contato em breve! \n")
                                print(f"Código de Falha: {cod_falha}")
                                print(f"Descrição da falha: {dict_cod_falha[cod_falha][0]}")
                                print("Orçamento prévio: R$: {:.2f}".format(float(dict_cod_falha[cod_falha][1])))
                                cod_diagnostico = geraCodDiagnostico()
                                print(f"Código do Diagnóstico: {cod_diagnostico}\n")
                    else:
                        print("\nSucesso, seu diagnóstico foi encaminhado para : CENTRO AUTOMOTIVO - BELA VISTA - RUA PEDROSO. Entraremos em contato em breve! \n")                            
                        print("Descrição da falha: Em análise pelo especialista. Aguarde contato!")
                        print(f"Orçamento prévio: Em análise.")
                        cod_diagnostico = geraCodDiagnostico()
                        print(f"Código do Diagnóstico: {cod_diagnostico}\n")                

                    #adicionando cliente no dicionario - dict_clientes 
                    cadastrarCodDiagnostico(len(lista_id), user, cod_diagnostico, dict_clientes)  
        
        
        
        
        
        case 2:

            print("\nCentro Automotivo Porto Seguro mais próximo\n")
            localizacao_atual = input("Informe a sua localização: ")
            localizacao_atual = validaMinCaracteres(localizacao_atual, 15, "Informe a sua localizacao: ")
            print(f"\nNo endereço {localizacao_atual}, os Centro Automotivo Porto Seguro mais próximos e disponiveis se encontram em: " +
                "\n\n1 - Av. Inocêncio Seráfico, 1070 - Vila Silva Ribeiro, Carapicuíba - SP, 06380-021\n" +
                "\n2 - Alameda Araguaia, 211 - Alphaville Industrial, Barueri - SP, 06455-000\n" +
                "\n3 - Alameda Araguaia, 3600 - Tamboré, Barueri - SP, 06455-000 \n")            
        case 3:
            print("\nAcompanhamento de Diagnóstico \n")
            cod_diagnostico = int(input("Digite seu código de diagnóstico: "))
            cod_diagnostico = validaCodigoDiagnostico(cod_diagnostico)
            print(f"\nO Diagnóstico de código: '{cod_diagnostico}' está registrado na : CENTRO AUTOMOTIVO - BELA VISTA - RUA PEDROSO. Estamos no seu aguardo! \n") 
            print("Descrição da falha: Em análise")
            print(f"Orçamento prévio: Em análise.")
            print(f"Código do Diagnóstico: {cod_diagnostico}\n")

def funcaoFaleConosco():
    '''
    Procedimento de feedback da experiência conforme categoria: elogio, reclamação, problemas de funcionalidades ou outros.
    '''
    print("\nComo a gente pode te ajudar: \n")
    print("╔════════════════════════════════════════════╗")
    print("║              **FALE CONOSCO**              ║")
    print("║                                            ║")
    print("║ 1 - Elogio / Reclamação                    ║")
    print("║ 2 - Problema com o aplicativo              ║")
    print("║ 3 - Mais informações                       ║")   
    print("╚════════════════════════════════════════════╝  \n")  

    fale_conosco = int(input("Selecione uma das opções: "))
    fale_conosco = validacaoMatch(3, fale_conosco)
    match fale_conosco:
        case 1:
            print("╔════════════════════════════════════════════╗")
            print("║               **OPINIÃO**                  ║")
            print("║                                            ║")
            print("║ 1 - Elogio                                 ║")
            print("║ 2 - Reclamação                             ║")
            print("╚════════════════════════════════════════════╝  \n") 

            fale_conosco_opiniao = int(input("Digite uma das opções: "))
            fale_conosco_opiniao = validacaoMatch(2, fale_conosco_opiniao)
            match fale_conosco_opiniao:
                case 1:
                    opiniao_usuario_elogio = input("\nMuito obrigado pelo contato, escreva seu elogio: ")
                    opiniao_usuario_elogio = validaMinCaracteres(opiniao_usuario_elogio, 5, "\nMuito obrigado pelo contato, escreva seu elogio: ")
                case 2:
                    opiniao_usuario_reclamacao = input("\nMuito obrigado pelo contato, escreva sua reclamação: ")
                    opiniao_usuario_reclamacao = validaMinCaracteres(opiniao_usuario_reclamacao, 5, "\nMuito obrigado pelo contato, escreva sua reclamação: ")
            print("\nSua opinião foi registrada! Entre no site para consultar sua opinião: " + 
                "\nhttps://centrosautomotivosportoseguro.campanhaporto.com.br\n")
        
        case 2:
            print("╔══════════════════════════════════════════════╗")
            print("║        **PROBLEMA COM O APLICATIVO**         ║")
            print("║                                              ║")
            print("║ 1 - Atendimento                              ║")
            print("║ 2 - Diagnóstico                              ║")
            print("║ 3 - Funcionalidade                           ║")
            print("║ 4 - Outros                                   ║")
            print("╚══════════════════════════════════════════════╝  \n") 
                
            problema_aplicativo = int(input("\nDigite uma das opções: "))
            problema_aplicativo = validacaoMatch(4, problema_aplicativo)
            match problema_aplicativo:
                case 1:
                    problema_aplicativo_atendimento = input("\nLamentamos o ocorrido com o atendimento. Por favor, detalhe o problema: ")
                    problema_aplicativo_atendimento = validaMinCaracteres(problema_aplicativo_atendimento, 5, "\nLamentamos o ocorrido com o atendimento. Por favor, detalhe o problema: ")
                case 2:
                    problema_aplicativo_diagnostico = input("\nLamentamos o ocorrido com o diagnóstico. Por favor, detalhe o problema: ")
                    problema_aplicativo_diagnostico = validaMinCaracteres(problema_aplicativo_diagnostico, 5, "\nLamentamos o ocorrido com o diagnóstico. Por favor, detalhe o problema: ")
                case 3:
                    problema_aplicativo_funcionalidade = input("\nLamentamos o ocorrido com as funcionalidades. Por favor, detalhe o problema: ")
                    problema_aplicativo_funcionalidade = validaMinCaracteres(problema_aplicativo_funcionalidade, 5, "\nLamentamos o ocorrido com as funcionalidades. Por favor, detalhe o problema: ")
                case 4:
                    problema_aplicativo_outros = input("\nLamentamos o ocorrido. Por favor, detalhe o problema: ")
                    problema_aplicativo_outros = validaMinCaracteres(problema_aplicativo_outros, 5, "\nLamentamos o ocorrido. Por favor, detalhe o problema: ")

            print("\nAgradecemos pelo contato! Sua opinião foi registrada! Entre no site para consultar sua opinião: " + 
                "\nhttps://centrosautomotivosportoseguro.campanhaporto.com.br\n")
        case 3:
            
            print("\nPara mais informações:")
            print("\nEntre em contato em: https://centrosautomotivosportoseguro.campanhaporto.com.br\n")

lista_id = [0, 1, 2, 3]
lista_nomes = ["admin", "allan.brito", "caio.liang", "levi.magni"]

dict_clientes = dict(zip(lista_nomes , lista_id))

#AUTOCHECK NOTAS:
#Integração para o formato dict-dict
#Dar opção de trocar de usuário
#Criar CRUD

#main
while True:   

    user = funcaoTelaLogin()
    
    print("\nBem vindo ao serviço de diagnóstico automotivo digital da Porto-Seguro! \n")
    
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
            funcaoAdquirirServico(user)        
        case 3:
            funcaoFaleConosco() 
        case 4:
            break
print("\n", dict_clientes)
print("\n", lista_nomes)
print("\n", lista_id)
print("\nObrigado, volte sempre!")
#AUTOCHECK @2024