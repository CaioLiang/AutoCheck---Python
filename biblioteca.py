 #ADICIONAIS
from conexaoBD import *  
import os

def tryExceptInputMenu(label):
    while True:
        try:
            opcao_menu = int(input(f"{label}"))
            break
        except ValueError as error:
            print(f"\nValor Inválido! '{error}' não faz parte de uma das opções.")
    return opcao_menu

def cadastrarCliente (id, nome, dict_clientes, lista_id, lista_nomes):
    id += 1
    dict_clientes[nome] = {id : ()}
    lista_id = lista_id.append(id)
    lista_nomes = lista_nomes.append(nome)
    cpf = gera_cpf()
    print()
    sql_insert_usuario = f"INSERT INTO TB_USUARIO (nome_usuario, cpf_usuario, endereco_usuario, tel_usuario) VALUES ('{nome}', '{cpf}', 'Rua padrao autocheck, 366', '11987654330')"
    comandoConexaoBD(sql_insert_usuario)
    sql_insert_login = f"INSERT INTO tb_login (id_usuario, login_usuario, senha_usuario) VALUES ({id}, '{nome}', 'SEM_SENHA')"
    comandoConexaoBD(sql_insert_login)
    
def cadastrarCodDiagnostico (id, user, cod_diagnostico, dict_clientes):
    if user in dict_clientes.keys():
        lista_key = list(dict_clientes[user].keys())
        id = lista_key[0]
    lista_cod_diagnostico_atual = (dict_clientes[user][id])
    dict_clientes[user][id] = lista_cod_diagnostico_atual + (cod_diagnostico, ) 
    
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
    try:
        numero_digitado = int(numero_digitado)    
    except ValueError as error:
        print(f"\nValor Inválido! '{error}' não faz parte de uma das opções.")
    
    lista_tam = []
    for i in range(1, tamanho_max+1, 1):
        lista_tam.append(i)
    while True:
        if numero_digitado in lista_tam:
            break
        else: 
            print(f"A opção digitada: '{numero_digitado}' não é uma das opções. Possiveis opções : {lista_tam}")
        numero_digitado = tryExceptInputMenu("\nDigite uma opção: ")
            
    return numero_digitado
     
def geraCodDiagnostico(lista_id_diagnostico):
    """
    Função para gerar o próximo número da lista de diagnostico.

    :return: int do próximo número
    """
    lista_id_diagnostico.append(len(lista_id_diagnostico) + 1)
    
    return len(lista_id_diagnostico)

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
        automovel_ano = tryExceptInputMenu("Digite novamente o ano do automóvel: ")
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

def manterLogin(user, dict_clientes, lista_id, lista_nomes):

    print("╔═════════════════════════════════╗")
    print("║         **MANTER LOGIN**        ║")
    print("║                                 ║")
    print("║ 1 - Sim                         ║")
    print("║ 2 - Não                         ║")
    print("╚═════════════════════════════════╝  \n")

    decisao_login = input(f"Quer manter logado com a conta:'{user}'? Escolha uma das opções acima: ")
    decisao_login = validacaoMatch(2, decisao_login)
    if decisao_login == 1: 
        return user
    return funcaoTelaLogin(dict_clientes, lista_id, lista_nomes)

def funcaoDictClientes(lista_id, lista_nomes):
    dict_clientes = dict(zip(lista_nomes , lista_id))
    for  users in dict_clientes.keys():
        dict_clientes[users] = {dict_clientes[users]: ()}
    return dict_clientes

def exportarJson(dict_diagnostico): 
    
    print("\nDeseja exportar arquivo em JSON?\n" + 
      "1 = SIM\n" + 
      "2 = NÃO\n")

    exportar = int(input("Digite uma das opcões: "))
    validacaoMatch(2, exportar)
    
    if exportar == 1:
        import json
        
        with open (f'codigo_diagonostico_{dict_diagnostico['cod_diagnostico']}.json', 'w', encoding='utf-8') as arquivo:
            json.dump(dict_diagnostico, arquivo, ensure_ascii= False, indent=4)
        
        print("Diagnóstico exportado em JSON!\n")

def credenciaisJson():
    import json
    
    print("\nCONEXÃO COM BANCO DE DADOS\n" +
          "\nForneça suas credencias para conexão com banco de dados da ORACLE - FIAP: \n")
    
    print("\nNota: digite seu LOGIN no seguinte modelo 'rm ou p' + 'numeros' | ex: rm111111 \n")
    
    user = input("Digite o seu login: ")
    password = input("Digite a sua senha: ")
    
    
    dict_credenciais = {
        'login' : user,
        'senha' : password
    }
        
    with open (f'credenciais.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dict_credenciais, arquivo, ensure_ascii= False, indent=4)         

def comandoConexaoBD(query_script):
    while True:
        try:
            conn = conecta_banco()
            cursor = conn.cursor()
            cursor.execute(query_script)  

            if query_script.strip().upper().startswith(('INSERT', 'UPDATE', 'DELETE')):
                conn.commit()
            
            if query_script.strip().upper().startswith('SELECT'):
                resultados = cursor.fetchall()
                
                if resultados:
                    print("Consulta retornou resultados.")
                else:
                    print("Consulta não retornou resultados.")
                
                print("Comando executado com sucesso!")
                return resultados
            
            print("Comando executado com sucesso!")
            break
        except Exception as e: 
            print("\nERRO DE CREDENCIAIS\n")
            print(f"\nErro: {e}\n")
            credenciaisJson()  

    cursor.close()
    conn.close()
    
def lerLogin():
    dicionario = comandoConexaoBD('SELECT * FROM TB_LOGIN')
    print("\n----------------LEITURA DOS USUARIOS - BANCO ----------------\n")
    return dicionario

def gera_digito_verificador(cpf_parcial):
    soma = 0
    peso = len(cpf_parcial) + 1
    for digito in cpf_parcial:
        soma += int(digito) * peso
        peso -= 1
    resto = 11 - (soma % 11)
    return 0 if resto > 9 else resto

def gera_cpf():
    import random
    
    cpf_parcial = [str(random.randint(0, 9)) for _ in range(9)]
    digito1 = gera_digito_verificador(cpf_parcial)
    cpf_parcial.append(str(digito1))
    digito2 = gera_digito_verificador(cpf_parcial)
    cpf_parcial.append(str(digito2))
    return ''.join(cpf_parcial)

def excluiCredenciais(arquivo):
    try: 
        os.path.exists(arquivo)
        os.remove(arquivo)
        print(f'O arquivo {arquivo} foi apagado com sucesso.')
    except:
        print(f'O arquivo {arquivo} não foi encontrado.')

def lerCodDiagnostico():
    sql_diagnostico = 'SELECT * FROM TB_DIAGNOSTICO'
    print("\n----------------LEITURA DOS DIAGNOSTICOS - BANCO----------------\n")
    infos_tabela = comandoConexaoBD(sql_diagnostico)
    lista_id_diagnostico = []
    
    for info in infos_tabela:
        lista_id_diagnostico.append(info[0])
    return lista_id_diagnostico    

def exibir_tabela(dados, cabecalhos):
    largura_colunas = [len(cab) for cab in cabecalhos]

    for linha in dados:
        for i, valor in enumerate(linha):
            largura_colunas[i] = max(largura_colunas[i], len(str(valor)))

    linha_formatada = '| ' + ' | '.join([f"{{:<{largura}}}" for largura in largura_colunas]) + ' |'

    print(linha_formatada.format(*cabecalhos))
    print('-' * (sum(largura_colunas) + 3 * len(cabecalhos) + 1))

    for linha in dados:
        print(linha_formatada.format(*linha))

def queryIdDiagnostico(consulta_id_usuario):
                    query = f"SELECT id_carro FROM tb_usuario_carro WHERE id_usuario = '{consulta_id_usuario}'"
                    todos_carros  = comandoConexaoBD(query)                    
                    lista_carros = []
                    for carro in todos_carros:
                        lista_carros.append(str(carro[0]))
            
                    if len(lista_carros) >= 2:
                        print("\nVocê possui essses automoveis cadastrados: " , lista_carros)
                        carro_consulta = input("Escolha uma das opções de carro: ")
                        while carro_consulta not in lista_carros:
                            print("\nOpção inválida! \n")
                            carro_consulta = input("Escolha uma das opções de carro: ")                 
                    else:
                        carro_consulta = lista_carros[0]
                    
                    
                    query = f"SELECT id_diagnostico FROM TB_CARRO_DIAGNOSTICO WHERE id_carro = '{carro_consulta}'"
                    todos_id_diagnostico  = comandoConexaoBD(query)                    
                    lista_id_diagnostico = []
                    for id in todos_id_diagnostico:
                        lista_id_diagnostico.append(str(id[0]))
                    
                    if len(lista_id_diagnostico) >= 2:
                        print("\nVocê possui essses id diagnostico cadastrados nesse carro: " , lista_id_diagnostico)
                        diagnostico_consulta = input("Escolha uma das opções de id diagnostico: ")
                        while diagnostico_consulta not in lista_id_diagnostico:
                            print("\nOpção inválida! \n")
                            diagnostico_consulta = input("Escolha uma das opções de id diagnostico: ")                 
                    
                    else:
                        diagnostico_consulta = lista_id_diagnostico[0]  
                    
                    return diagnostico_consulta  

def printRegistro(resultado_diagnostico, cabecalhos):
    print("\n\n")
    exibir_tabela(resultado_diagnostico, cabecalhos)
    print("\n")
     
def getApi(url):
    import requests
    import json
    
    caminho_marcas = "lista_marcas_carros.json"

    while True:
        if os.path.exists(caminho_marcas):
            with open(caminho_marcas, 'r') as arquivo:
                info_lista = json.load(arquivo)
                return info_lista    
        
        else: 
            print("\n----------------REQUISIÇÃO API----------------\n")
            response = requests.get(url)
            
            if response.status_code == 200:
                lista_marca_carros = response.json()
                
            with open ('lista_marcas_carros.json', 'w', encoding='utf-8') as arquivo:
                json.dump(lista_marca_carros, arquivo, ensure_ascii= False, indent=4)
        

#SISTEMA

def funcaoTelaLogin(dict_clientes, lista_id, lista_nomes ):
    
    print("\n***** AUTOCHECK - PORTO SEGURO ***** \n")
    print("╔═════════════════════════════════╗")
    print("║    **Bem-vindo à AutoCheck**    ║")
    print("║                                 ║")
    print("║ 1 - Login                       ║")
    print("║ 2 - Cadastrar conta             ║")
    print("╚═════════════════════════════════╝  \n")
           
    tela_login_menu = str(tryExceptInputMenu("\nDigite um número do menu acima: "))
    tela_login_menu = validacaoMatch(2, tela_login_menu)

    if tela_login_menu == 1: 
        while True:
            user = str(input("Formato padrão : Mínimo de 6 caracteres'\n"+ 
                             "Digite nome do seu usuario: "))
            user = validaMinCaracteres(user, 6,"Formato padrão : 'nome.sobrenome'\nDigite nome do seu usuario: ")
            if user in dict_clientes.keys():
                print("Login realizado com sucesso!")
                return user
            print(f"\nUsuário: {user}. Não cadastrado!\n")
                       
            print("╔═════════════════════════════════╗")
            print("║       **DESEJA CADASTRAR**      ║")
            print("║                                 ║")
            print("║ 1 - Sim                         ║")
            print("║ 2 - Não                         ║")
            print("╚═════════════════════════════════╝  \n")
            
            resposta_cadastrar = input(("Deseja cadastrar? Digite uma das opções acima: "))
            resposta_cadastrar = validacaoMatch(2, resposta_cadastrar)
            if resposta_cadastrar == 1:
                cadastrarCliente((len(lista_id)), user, dict_clientes, lista_id, lista_nomes)               
                print(f"\nRegistrando '{user}' no cadastro....\n")
                return user
    
    else:
        while True:
            user = str(input("Formato padrão : 'nome.sobrenome'\n"+ 
                             "Digite nome do seu usuario: "))
            user = validaMinCaracteres(user, 6,"Formato padrão : 'nome.sobrenome'\nDigite nome do seu usuario: ")    
            
            if user in dict_clientes.keys():
                print("Usuário já possui cadastro!\n")
            else:       
                cadastrarCliente((len(lista_id)), user, dict_clientes, lista_id, lista_nomes)
                return user       
            
def funcaoConsultarServicos():
    '''
    Procedimento de consulta dos serviços disponíveis com uma breve descrição de suas funções.
    '''
    print("\nAtualmente as funcionalidades do aplicativo são: \n")
    print("╔════════════════════════════════════════╗")
    print("║            **INFORMAÇÕES**             ║")
    print("║                                        ║")
    print("║ 1 - Diagnóstico                        ║")
    print("║ 2 - Centro Automotivo mais próxima     ║")
    print("║ 3 - Acompanhar diagnóstico             ║")
    print("║ 4 - Feedback | Fale conosco            ║")     
    print("╚════════════════════════════════════════╝  \n")

    consulta_menu = tryExceptInputMenu("\nDigite o número que você quer mais detalhes: ")
    consulta_menu = validacaoMatch(4, consulta_menu)

    print(dicionario_infos["consulta"][consulta_menu])

def funcaoAdquirirServico(user, lista_id, dict_clientes, lista_cod_diagostico):
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
    
    servico_menu = tryExceptInputMenu("\nDigite uma das opções: ")
    servico_menu = validacaoMatch(3, servico_menu)
    match servico_menu: 
        case 1:
            print("\nEntendo, preciso de mais informações do seu automóvel: \n" +
            "Preencha os seguintes campos: \n")
            
            cadastro_carro = True
        
            automovel_chassi = str(input("Chassi: "))
            
            while len(automovel_chassi) != 17:
                print("\nQUANTIDADE INVALIDA! ")
                print("\nO CHASSI é composto por 17 caracteres exatamente, tente novamente!\n")
                automovel_chassi = str(input("Chassi: "))
            
            automovel_chassi = validaMinCaracteres(automovel_chassi, 17, "Chassi: ")
            
            sql_select_chassi = "SELECT chassi_carro FROM tb_carro"
            print("\n----------------CONSULTANDO CHASSIS----------------")
            todos_chassi  = comandoConexaoBD(sql_select_chassi)                    
            lista_chassis = []
            for chassi in todos_chassi:
                lista_chassis.append(chassi[0])
            
            if automovel_chassi in lista_chassis:
                cadastro_carro = False
                
            url = "https://parallelum.com.br/fipe/api/v1/carros/marcas"
            
            dados_marca_carros = []
            lista_marcas = []
            
            dados_marca_carros = getApi(url)

            for dado in dados_marca_carros: 
                lista_marcas.append(dado['nome'].upper())
                      
            automovel_ano = tryExceptInputMenu("Ano: ")
            automovel_ano = validaAno(automovel_ano)
            
            automovel_marca = str(input("Marca: "))
            
            while automovel_marca not in lista_marcas: 
                print("\nMARCA NÃO REGISTRADA!\n")
                print("Marcas de Carros Disponíveis:")
                print("-" * 30)
                for index, marca in enumerate(lista_marcas, start=1):
                    print(f"{index}. {marca}")
                print("-" * 30)
                automovel_marca = str(input("\nDigite a marca: ")).upper()

            automovel_modelo = str(input("Modelo: "))
            automovel_modelo = validaMinCaracteres(automovel_modelo, 3, "Modelo: ")
            automovel_ano_modelo = tryExceptInputMenu("Ano do modelo: ")
            automovel_ano_modelo = validaAno(automovel_ano_modelo)
            automovel_motor = str(input("Motor: "))
            automovel_motor = validaMinCaracteres(automovel_motor, 7, "Motor: ")
            print("\n\nSobre o código de falha: \n")
            print("╔════════════════════════════════════════╗")
            print("║           **INFORMAÇÕES**              ║")
            print("║                                        ║")
            print("║ 1 - Tenho o Código de Falha            ║")
            print("║ 2 - Não tenho o Código de Falha        ║")     
            print("╚════════════════════════════════════════╝  \n")


            diagnostico_codigo_falha = tryExceptInputMenu("\nDigite uma das opções: ")
            diagnostico_codigo_falha = validacaoMatch(2, diagnostico_codigo_falha)
            match diagnostico_codigo_falha: 
                case 1: 
                    cod_falha_usuario = str(input("Digite o código de falha: "))
                    cod_falha_usuario = validaCodFalha(cod_falha_usuario)
                    sintomas_automovel = str(input("Entendo, descreve o problema do seu automóvel: "))
                    sintomas_automovel = validaMinCaracteres(sintomas_automovel, 10, "Entendo, descreve o problema do seu automóvel: ")
                    print("\nSucesso, seu diagnóstico foi encaminhado para : CENTRO AUTOMOTIVO - BELA VISTA - RUA PEDROSO. Entraremos em contato em breve! \n")
                    print(f"Código de Falha: {cod_falha_usuario}")
                    print("Descrição da falha: Em análise.")
                    print("Orçamento prévio: Em análise")
                    cod_diagnostico = geraCodDiagnostico(lista_cod_diagostico)
                    print(f"Código do Diagnóstico: {cod_diagnostico}\n")
                    categoria_diagnostico = 'N'
                    desc_falha = 'Em análise'
                    orca_previo = 'Em análise'
                    dict_diagnostico =  {
                        'usuario' : {user : dict_clientes[user]},            
                        'automovel_dados' : 
                            {
                            'automovel_chassi': automovel_chassi,
                            'automovel_ano': automovel_ano,
                            'automovel_marca': automovel_marca,
                            'automovel_modelo': automovel_modelo,
                            'automovel_ano_modelo': automovel_ano_modelo,
                            'automovel_motor': automovel_motor            
                            },
                        'sintomas_automovel': sintomas_automovel,
                        'categoria_diagnostico': categoria_diagnostico,
                        'cod_diagnostico' : cod_diagnostico,
                        'cod_falha' : cod_falha_usuario,
                        'desc_falha' : desc_falha,
                        'orca_previo' : orca_previo,
                                    
                        }
                    print("\n-------------INSERINDO DIAGNOSTICO-------------")
                    sql_inserir_diagnostico = f"INSERT INTO TB_DIAGNOSTICO (cod_falha_diagnostico, categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('{cod_falha_usuario}', '{categoria_diagnostico}', '{desc_falha}', '{sintomas_automovel}')"
                    comandoConexaoBD(sql_inserir_diagnostico)
                    if cadastro_carro:    
                        print("\n-------------INSERINDO CARRO-------------")
                        sql_inserir_automovel = f"INSERT INTO tb_carro (chassi_carro, marca_carro, modelo_carro, ano_fabricacao_carro, ano_modelo_carro) VALUES ('{automovel_chassi}', '{automovel_marca}', '{automovel_modelo}', '{automovel_ano}', '{automovel_ano_modelo}')"
                        comandoConexaoBD(sql_inserir_automovel)
                    print("\n-------------BUSCANDO ID CARRO-------------")
                    sql_select_carro = f"SELECT id_carro FROM tb_carro WHERE chassi_carro = '{automovel_chassi}'"
                    id_carro_cadastro = comandoConexaoBD(sql_select_carro)                
                    print("\n-------------ATRELANDO CARRO AO DIAGNOSTICO-------------")
                    sql_inserir_carro_diagnostico = f"INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES ({int(cod_diagnostico)}, {int(id_carro_cadastro[0][0])})"
                    comandoConexaoBD(sql_inserir_carro_diagnostico)
                    print("\n-------------ATRELANDO CARRO AO USUARIO-------------")
                    sql_inserir_usuario_automovel = f"INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES ({int(list(dict_clientes[user].keys())[0])}, {int(id_carro_cadastro[0][0])}, 'S')" 
                    comandoConexaoBD(sql_inserir_usuario_automovel)
                    
                    exportarJson(dict_diagnostico)

                    
                case 2:
                    sintomas_automovel = str(input("Entendo, descreve o problema do seu automóvel: "))
                    sintomas_automovel = validaMinCaracteres(sintomas_automovel, 10, "Entendo, descreve o problema do seu automóvel: ")
                    print("\nConforme seu relato sobre o estado do carro, \n" + 
                    "As possiveis áreas afetadas são: \n")
                    print("╔════════════════════════════════════════╗")
                    print("║           **ÁREA AFETADA**             ║")
                    print("║                                        ║")
                    print("║ 1 - Elétrica                           ║")
                    print("║ 2 - Mecânica                           ║")     
                    print("╚════════════════════════════════════════╝  \n")
                    

                    area_afetada = tryExceptInputMenu("Digite um das opções : ")
                    area_afetada = validacaoMatch(2, area_afetada)
                    
                    print("\nPossui mais detalhes da causa do problema? \n")  
                    print("╔════════════════════════════════════════╗")
                    print("║         **DETALHES DA CAUSA**          ║")
                    print("║                                        ║")
                    print("║ 1 - SIM                                ║")
                    print("║ 2 - NÃO                                ║")     
                    print("╚════════════════════════════════════════╝  \n")

                    conhecimento_causa = tryExceptInputMenu("Digite uma das opções: ")
                    conhecimento_causa = validacaoMatch(2, conhecimento_causa)
                    if(conhecimento_causa == 1):
                        dict_cod_falha = {
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
                        "AAAAA": ("Em análise", 0.00)
                        }
                        
                        match area_afetada:
                            case 1:
                                categoria_diagnostico = 'E'
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
                                
                                
                                falha_eletrica = tryExceptInputMenu("Digite um número do menu: ")
                                falha_eletrica = validacaoMatch(8, falha_eletrica)     
                                match falha_eletrica:
                                    case 1:                                     
                                        cod_falha = "C0800"
                                    case 2:
                                        cod_falha = "P0645"
                                    case 3:
                                        cod_falha = "P0087" 
                                    case 4:
                                        cod_falha = "P0300"
                                    case 5:
                                        cod_falha = "P0418"
                                    case 6:
                                        cod_falha = "P0650"
                                    case 7:
                                        cod_falha = "P0620"
                                    case 8:
                                        cod_falha = "AAAAA"
                    
                                print("\nSucesso, seu diagnóstico foi encaminhado para : CENTRO AUTOMOTIVO - BELA VISTA - RUA PEDROSO. Entraremos em contato em breve! \n") 
                                print(f"Código de Falha: {cod_falha}")
                                print(f"Descrição da falha: {dict_cod_falha[cod_falha][0]}")
                                print("Orçamento prévio: R$: {:.2f}".format(float(dict_cod_falha[cod_falha][1])))
                                cod_diagnostico = geraCodDiagnostico(lista_cod_diagostico)
                                print(f"Código do Diagnóstico: {cod_diagnostico}\n")
                                
                                dict_diagnostico =  {
                                    'usuario' : {user : dict_clientes[user]},
                                    'automovel_dados' : 
                                        {
                                        'automovel_chassi': automovel_chassi,
                                        'automovel_ano': automovel_ano,
                                        'automovel_marca': automovel_marca,
                                        'automovel_modelo': automovel_modelo,
                                        'automovel_ano_modelo': automovel_ano_modelo,
                                        'automovel_motor': automovel_motor  
                                        },
                                    'sintomas_automovel': sintomas_automovel,
                                    'categoria_diagnostico': categoria_diagnostico,
                                    'cod_diagnostico' : cod_diagnostico,
                                    'cod_falha' : cod_falha,
                                    'desc_falha' : dict_cod_falha[cod_falha][0],
                                    'orca_previo' : dict_cod_falha[cod_falha][1],
                                    
                                }
                                print("\n-------------INSERINDO DIAGNOSTICO-------------")
                                sql_inserir_diagnostico = f"INSERT INTO TB_DIAGNOSTICO (cod_falha_diagnostico, categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('{cod_falha}', '{categoria_diagnostico}', '{dict_cod_falha[cod_falha][0]}', '{sintomas_automovel}')"
                                comandoConexaoBD(sql_inserir_diagnostico)
                                if cadastro_carro:    
                                    print("\n-------------INSERINDO CARRO-------------")
                                    sql_inserir_automovel = f"INSERT INTO tb_carro (chassi_carro, marca_carro, modelo_carro, ano_fabricacao_carro, ano_modelo_carro) VALUES ('{automovel_chassi}', '{automovel_marca}', '{automovel_modelo}', '{automovel_ano}', '{automovel_ano_modelo}')"
                                    comandoConexaoBD(sql_inserir_automovel)
                                print("\n-------------BUSCANDO ID CARRO-------------")
                                sql_select_carro = f"SELECT id_carro FROM tb_carro WHERE chassi_carro = '{automovel_chassi}'"
                                id_carro_cadastro = comandoConexaoBD(sql_select_carro)                
                                print("\n-------------ATRELANDO CARRO AO DIAGNOSTICO-------------")
                                sql_inserir_carro_diagnostico = f"INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES ({int(cod_diagnostico)}, {int(id_carro_cadastro[0][0])})"
                                comandoConexaoBD(sql_inserir_carro_diagnostico)
                                print("\n-------------ATRELANDO CARRO AO USUARIO-------------")
                                sql_inserir_usuario_automovel = f"INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES ({int(list(dict_clientes[user].keys())[0])}, {int(id_carro_cadastro[0][0])}, 'S')" 
                                comandoConexaoBD(sql_inserir_usuario_automovel)
                                
                                exportarJson(dict_diagnostico)
                            
                            case 2: 
                                categoria_diagnostico = 'M'
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

                                falha_mecanica = tryExceptInputMenu("O que você quer fazer? Digite um número do menu: ")
                                falha_mecanica = validacaoMatch(7, falha_mecanica)
                
                                match falha_mecanica:
                                    case 1:
                                        cod_falha = "P1712"                              
                                    case 2:
                                        cod_falha = "P0217"
                                    case 3:
                                        cod_falha = "P0263" 
                                    case 4:
                                        cod_falha = "C0238"
                                    case 5:
                                        cod_falha = "P0805"
                                    case 6:
                                        cod_falha = "P0381"
                                    case 7:
                                        cod_falha = "AAAAA"

                                print("\nSucesso, seu diagnóstico foi encaminhado para : CENTRO AUTOMOTIVO - BELA VISTA - RUA PEDROSO. Entraremos em contato em breve! \n")
                                print(f"Código de Falha: {cod_falha}")
                                print(f"Descrição da falha: {dict_cod_falha[cod_falha][0]}")
                                print("Orçamento prévio: R$: {:.2f}".format(float(dict_cod_falha[cod_falha][1])))
                                cod_diagnostico = geraCodDiagnostico(lista_cod_diagostico)
                                print(f"Código do Diagnóstico: {cod_diagnostico}\n")
                                
                                dict_diagnostico =  {
                                    'usuario' : {user : dict_clientes[user]},   
                                    'automovel_dados' : 
                                        {
                                        'automovel_chassi': automovel_chassi,
                                        'automovel_ano': automovel_ano,
                                        'automovel_marca': automovel_marca,
                                        'automovel_modelo': automovel_modelo,
                                        'automovel_ano_modelo': automovel_ano_modelo,
                                        'automovel_motor': automovel_motor 
                                        },
                                    'sintomas_automovel': sintomas_automovel,
                                    'categoria_diagnostico': categoria_diagnostico,
                                    'cod_diagnostico' : cod_diagnostico,
                                    'cod_falha' : cod_falha,
                                    'desc_falha' : dict_cod_falha[cod_falha][0],
                                    'orca_previo' : dict_cod_falha[cod_falha][1],
                                    
                                }
                                print("\n-------------INSERINDO DIAGNOSTICO-------------")
                                sql_inserir_diagnostico = f"INSERT INTO TB_DIAGNOSTICO (cod_falha_diagnostico, categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('{cod_falha}', '{categoria_diagnostico}', '{dict_cod_falha[cod_falha][0]}', '{sintomas_automovel}')"
                                comandoConexaoBD(sql_inserir_diagnostico)
                                if cadastro_carro:    
                                    print("\n-------------INSERINDO CARRO-------------")
                                    sql_inserir_automovel = f"INSERT INTO tb_carro (chassi_carro, marca_carro, modelo_carro, ano_fabricacao_carro, ano_modelo_carro) VALUES ('{automovel_chassi}', '{automovel_marca}', '{automovel_modelo}', '{automovel_ano}', '{automovel_ano_modelo}')"
                                    comandoConexaoBD(sql_inserir_automovel)
                                print("\n-------------BUSCANDO ID CARRO-------------")
                                sql_select_carro = f"SELECT id_carro FROM tb_carro WHERE chassi_carro = '{automovel_chassi}'"
                                id_carro_cadastro = comandoConexaoBD(sql_select_carro)                
                                print("\n-------------ATRELANDO CARRO AO DIAGNOSTICO-------------")
                                sql_inserir_carro_diagnostico = f"INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES ({int(cod_diagnostico)}, {int(id_carro_cadastro[0][0])})"
                                comandoConexaoBD(sql_inserir_carro_diagnostico)
                                print("\n-------------ATRELANDO CARRO AO USUARIO-------------")
                                sql_inserir_usuario_automovel = f"INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES ({int(list(dict_clientes[user].keys())[0])}, {int(id_carro_cadastro[0][0])}, 'S')" 
                                comandoConexaoBD(sql_inserir_usuario_automovel)
                                
                                exportarJson(dict_diagnostico)
                                            
                    else:
                        categoria_diagnostico = 'N'
                        orca_previo = "Em análise"
                        desc_falha = "Em análise"
                        cod_falha_usuario = "AAAAA"
                        print("\nSucesso, seu diagnóstico foi encaminhado para : CENTRO AUTOMOTIVO - BELA VISTA - RUA PEDROSO. Entraremos em contato em breve! \n")                            
                        print("Descrição da falha: Em análise pelo especialista. Aguarde contato!")
                        print(f"Orçamento prévio: Em análise.")
                        cod_diagnostico = geraCodDiagnostico(lista_cod_diagostico)
                        print(f"Código do Diagnóstico: {cod_diagnostico}\n") 

                        dict_diagnostico =  {
                            'usuario' : {user : dict_clientes[user]},            
                            'automovel_dados' : 
                                {
                                'automovel_chassi': automovel_chassi,
                                'automovel_ano': automovel_ano,
                                'automovel_marca': automovel_marca,
                                'automovel_modelo': automovel_modelo,
                                'automovel_ano_modelo': automovel_ano_modelo,
                                'automovel_motor': automovel_motor            
                                },
                            'sintomas_automovel': sintomas_automovel,
                            'categoria_diagnostico': categoria_diagnostico,
                            'cod_diagnostico' : cod_diagnostico,
                            'cod_falha' : cod_falha_usuario,
                            'desc_falha' : desc_falha,
                            'orca_previo' : orca_previo,
                                        
                            }
                        print("\n-------------INSERINDO DIAGNOSTICO-------------")
                        sql_inserir_diagnostico = f"INSERT INTO TB_DIAGNOSTICO (cod_falha_diagnostico, categoria_diagnostico, descricao_diagnostico, descricao_problema_diagnostico) VALUES ('{cod_falha_usuario}', '{categoria_diagnostico}', '{desc_falha}', '{sintomas_automovel}')"
                        comandoConexaoBD(sql_inserir_diagnostico)
                        if cadastro_carro:    
                            print("\n-------------INSERINDO CARRO-------------")
                            sql_inserir_automovel = f"INSERT INTO tb_carro (chassi_carro, marca_carro, modelo_carro, ano_fabricacao_carro, ano_modelo_carro) VALUES ('{automovel_chassi}', '{automovel_marca}', '{automovel_modelo}', '{automovel_ano}', '{automovel_ano_modelo}')"
                            comandoConexaoBD(sql_inserir_automovel)
                        print("\n-------------BUSCANDO ID CARRO-------------")
                        sql_select_carro = f"SELECT id_carro FROM tb_carro WHERE chassi_carro = '{automovel_chassi}'"
                        id_carro_cadastro = comandoConexaoBD(sql_select_carro)                
                        print("\n-------------ATRELANDO CARRO AO DIAGNOSTICO-------------")
                        sql_inserir_carro_diagnostico = f"INSERT INTO tb_carro_diagnostico (id_diagnostico, id_carro) VALUES ({int(cod_diagnostico)}, {int(id_carro_cadastro[0][0])})"
                        comandoConexaoBD(sql_inserir_carro_diagnostico)
                        print("\n-------------ATRELANDO CARRO AO USUARIO-------------")
                        sql_inserir_usuario_automovel = f"INSERT INTO tb_usuario_carro (id_usuario, id_carro, ativo) VALUES ({int(list(dict_clientes[user].keys())[0])}, {int(id_carro_cadastro[0][0])}, 'S')" 
                        comandoConexaoBD(sql_inserir_usuario_automovel)            
                        
                        exportarJson(dict_diagnostico)              

            cadastrarCodDiagnostico(len(lista_id), user, cod_diagnostico, dict_clientes)  
           
        case 2:

            print("\nCentro Automotivo Porto Seguro mais próximo\n")
            localizacao_atual = str(input("Informe a sua localização: "))
            localizacao_atual = validaMinCaracteres(localizacao_atual, 15, "Informe a sua localizacao: ")
            print(f"\nNo endereço {localizacao_atual}, os Centro Automotivo Porto Seguro mais próximos e disponiveis se encontram em: " +
                "\n\n1 - Av. Inocêncio Seráfico, 1070 - Vila Silva Ribeiro, Carapicuíba - SP, 06380-021\n" +
                "\n2 - Alameda Araguaia, 211 - Alphaville Industrial, Barueri - SP, 06455-000\n" +
                "\n3 - Alameda Araguaia, 3600 - Tamboré, Barueri - SP, 06455-000 \n")            
        case 3:
                     
            consulta_id_usuario = int(list(dict_clientes[user].keys())[0])
            
            sql_select_usuarios = "SELECT id_usuario FROM tb_usuario_carro"
            print("\n----------------CONSULTANDO USUARIOS----------------")
            todos_usuarios  = comandoConexaoBD(sql_select_usuarios)                    
            lista_usuarios = []
            for usuario in todos_usuarios:
                lista_usuarios.append(usuario[0])
            
            if consulta_id_usuario in lista_usuarios:
                
                print("\nAcompanhamento de Diagnóstico \n")
                
                print("\nOpções de acompanhamento: \n")  
                print("╔════════════════════════════════════════════╗")
                print("║         **ACOMPANHAR DIAGNOSTICO**         ║")
                print("║                                            ║")
                print("║ 1 - Ver informações                        ║")
                print("║ 2 - Atualizar descrição                    ║")
                print("║ 3 - Deletar descrição                      ║")                     
                print("╚════════════════════════════════════════════╝  \n")
                
                acompanhar_diagnostico = input("Digite uma das opções acima: ")
                acompanhar_diagnostico = validacaoMatch(3, acompanhar_diagnostico)
                
                cabecalhos = ['ID', 'Código de Falha', 'Classe', 'Descrição Curta', 'Descrição Usuário']
                
                match acompanhar_diagnostico:
                    
                    case 1:
                        
                        diagnostico_consulta = queryIdDiagnostico(consulta_id_usuario)
                        
                        query = f"SELECT * FROM TB_DIAGNOSTICO WHERE id_diagnostico = '{diagnostico_consulta}'"
                        resultado_diagnostico  = comandoConexaoBD(query)
                    
                        printRegistro(resultado_diagnostico, cabecalhos)
                        
                    case 2:
                        print("\nATUALIZAR DESCRIÇÃO DO DIAGNOSTICO\n")
                        
                        diagnostico_consulta = queryIdDiagnostico(consulta_id_usuario)
                                            
                        nova_descricao = input("Digite a descrição do problema do veiculo: ")
                        nova_descricao = validaMinCaracteres(nova_descricao, 10, "Entendo, descreve o problema do seu automóvel: ")
                        
                        query = f"UPDATE TB_DIAGNOSTICO set descricao_problema_diagnostico = '{nova_descricao}' WHERE id_diagnostico = '{diagnostico_consulta}'"
                        comandoConexaoBD(query)
                        
                        query = f"SELECT * FROM TB_DIAGNOSTICO WHERE id_diagnostico = '{diagnostico_consulta}'"
                        resultado_diagnostico  = comandoConexaoBD(query)
                        
                        printRegistro(resultado_diagnostico, cabecalhos)
   
                    case 3:
                        print("\nDELETAR DESCRIÇÃO DO DIAGNOSTICO\n")

                        diagnostico_consulta = queryIdDiagnostico(consulta_id_usuario)
                        
                        query = f"UPDATE TB_DIAGNOSTICO set descricao_problema_diagnostico = 'SEM DESCRICAO' WHERE id_diagnostico = '{diagnostico_consulta}'"
                        comandoConexaoBD(query)
                        
                        query = f"SELECT * FROM TB_DIAGNOSTICO WHERE id_diagnostico = '{diagnostico_consulta}'"
                        resultado_diagnostico  = comandoConexaoBD(query)
                        
                        printRegistro(resultado_diagnostico, cabecalhos)
            
            else: 
                print("\nNENHUM DIAGNÓSTICO IDENTIFICADO PARA SEU USUÁRIO! \n")
                print("RETORNANDO AO MENU PRINCIPAL!\n")                
                
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

    fale_conosco = tryExceptInputMenu("Selecione uma das opções: ")
    fale_conosco = validacaoMatch(3, fale_conosco)
    match fale_conosco:
        case 1:
            print("╔════════════════════════════════════════════╗")
            print("║               **OPINIÃO**                  ║")
            print("║                                            ║")
            print("║ 1 - Elogio                                 ║")
            print("║ 2 - Reclamação                             ║")
            print("╚════════════════════════════════════════════╝  \n") 

            fale_conosco_opiniao = tryExceptInputMenu("Digite uma das opções: ")
            fale_conosco_opiniao = validacaoMatch(2, fale_conosco_opiniao)
            match fale_conosco_opiniao:
                case 1:
                    opiniao_usuario_elogio = str(input("\nMuito obrigado pelo contato, escreva seu elogio: "))
                    opiniao_usuario_elogio = validaMinCaracteres(opiniao_usuario_elogio, 5, "\nMuito obrigado pelo contato, escreva seu elogio: ")
                case 2:
                    opiniao_usuario_reclamacao = str(input("\nMuito obrigado pelo contato, escreva sua reclamação: "))
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
                
            problema_aplicativo = tryExceptInputMenu("\nDigite uma das opções: ")
            problema_aplicativo = validacaoMatch(4, problema_aplicativo)
            match problema_aplicativo:
                case 1:
                    problema_aplicativo_atendimento = str(input("\nLamentamos o ocorrido com o atendimento. Por favor, detalhe o problema: "))
                    problema_aplicativo_atendimento = validaMinCaracteres(problema_aplicativo_atendimento, 5, "\nLamentamos o ocorrido com o atendimento. Por favor, detalhe o problema: ")
                case 2:
                    problema_aplicativo_diagnostico = str(input("\nLamentamos o ocorrido com o diagnóstico. Por favor, detalhe o problema: "))
                    problema_aplicativo_diagnostico = validaMinCaracteres(problema_aplicativo_diagnostico, 5, "\nLamentamos o ocorrido com o diagnóstico. Por favor, detalhe o problema: ")
                case 3:
                    problema_aplicativo_funcionalidade = str(input("\nLamentamos o ocorrido com as funcionalidades. Por favor, detalhe o problema: "))
                    problema_aplicativo_funcionalidade = validaMinCaracteres(problema_aplicativo_funcionalidade, 5, "\nLamentamos o ocorrido com as funcionalidades. Por favor, detalhe o problema: ")
                case 4:
                    problema_aplicativo_outros = str(input("\nLamentamos o ocorrido. Por favor, detalhe o problema: "))
                    problema_aplicativo_outros = validaMinCaracteres(problema_aplicativo_outros, 5, "\nLamentamos o ocorrido. Por favor, detalhe o problema: ")

            print("\nAgradecemos pelo contato! Sua opinião foi registrada! Entre no site para consultar sua opinião: " + 
                "\nhttps://centrosautomotivosportoseguro.campanhaporto.com.br\n")
        case 3:
            
            print("\nPara mais informações:")
            print("\nEntre em contato em: https://centrosautomotivosportoseguro.campanhaporto.com.br\n")
