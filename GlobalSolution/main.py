# Importando as funções para o funcionamento do programa
import subalgoritmos

# Programa Principal
linha = "=" * 61
escolha_menu = 1
cadastro = ""
tipo_cadastro = ""
dados_necessarios_ong = ["Nome", "Email", "Telefone", "Endereço", "CNPJ", "Razão Social",
                         "Quantidade de pessoas associadas"]
dados_necessarios_empresa = ["Nome Fantasia", "Email", "Telefone", "Endereço", "CNPJ", "Razão Social", "Renda Mensal"]
dados_necessarios_mercado = ["Nome Fantasia", "Email", "Telefone", "Endereço", "CNPJ", "Razão Social", "Renda Mensal"]
dados_necessarios_pessoa_fisica = ["Nome", "Email(opcional)", "Telefone(opcional)", "Endereço", "CPF", "RG",
                                   "Renda Mensal"]
escolha_duvida = 1
duvidas = ["Como posso fazer uma doação para o programa?", "Quais os métodos de pagamento aceitos para doações?",
           "Existe um valor mínimo para as doações?", "Posso fazer uma doação em nome de outra pessoa?"]
valor_doacao = 0
doacao = []
cont_doacao = 0
repetir_doacao = "s"
doacao_realizada = False

# ------ Descrição do Projeto
print(f"""
    {linha}
    || Bem-vindo ao projeto FeedBack, uma rede de doações com  ||
    || o objetivo de ajudar a combater a fome mundial.         ||
    || Você pode se cadastrar como uma empresa ou supermercado ||
    || disposto a doar, ou como uma ONG ou Pessoa física para  ||
    || receber doações através de cartões que funcionarão como ||
    || uma espécie de “vale-alimentação”, os EatCard.          ||
    {linha}
        """)

# ------ Menu geral de ações
while escolha_menu != 0:
    print(f"""
    {linha}
    ||                         M E N U                         ||
    {linha}
    || Cadastre-se como:                                       ||
    || 1...................................: ONG para Caridade ||
    || 2....................................: Empresa Parceira ||
    || 3...............................: Supermercado parceiro ||
    || 4.......................................: Pessoa Física ||
    -------------------------------------------------------------
    || Outras ações:                                           ||
    || 5..................................: Dúvidas frequentes ||
    || 6.....................................: Realizar doação ||
    || 0...................................: Fechar o programa ||
    {linha}
    """)
    while True:
        try:
            escolha_menu = int(input("---> Escolha uma opção: "))
            break
        except ValueError:
            subalgoritmos.exibir_opcao_invalida()
            continue
    match escolha_menu:
        case 0:
            break
        case 1:
            # Cadastro como ONG

            if cadastro != "":
                print(f"""
    {linha}
    --> Você já está cadastrado!!!
    {linha}
                """)
            else:
                print(f"\n{linha}\n--> CADASTRO ONG:")
                cadastro = subalgoritmos.cadastro_parceiros(dados_necessarios_ong)
                tipo_cadastro = "ONG"
                print(f"{linha}\n--> Cadastro realizado com sucesso!!!\n{linha}")
        case 2:
            # Cadastro como Empresa

            if cadastro != "":
                print(f"""
    {linha}
    --> Você já está cadastrado!!!
    {linha}
                """)
            else:
                print(f"\n{linha}\n--> CADASTRO EMPRESA:")
                cadastro = subalgoritmos.cadastro_parceiros(dados_necessarios_empresa)
                tipo_cadastro = "Empresa"
                print(f"{linha}\n--> Cadastro realizado com sucesso!!!\n{linha}")
        case 3:
            # Cadastro como Supermercado

            if cadastro != "":
                print(f"""
    {linha}
    --> Você já está cadastrado!!!
    {linha}
                """)
            else:
                print(f"\n{linha}\n--> CADASTRO SUPERMERCADO:")
                cadastro = subalgoritmos.cadastro_parceiros(dados_necessarios_mercado)
                tipo_cadastro = "Supermercado"
                print(f"{linha}\n--> Cadastro realizado com sucesso!!!\n{linha}")
        case 4:
            # Cadastro como Pessao Física

            if cadastro != "":
                print(f"""
    {linha}
    --> Você já está cadastrado!!!
    {linha}
                """)
            else:
                print(f"\n{linha}\n--> CADASTRO PESSOA FÍSICA:\n(apenas digite ENTER para dados opcionais)")
                cadastro = subalgoritmos.cadastro_parceiros(dados_necessarios_pessoa_fisica)
                tipo_cadastro = "Pessoa Física"
                print(f"{linha}\n--> Cadastro realizado com sucesso!!!\n{linha}")
        case 5:
            # Menu de Dúvidas Frequentes

            while escolha_duvida != 0:
                escolha_duvida = subalgoritmos.exibir_menu_duvidas(duvidas)
                match escolha_duvida:

                    # Respostas
                    case 0:
                        print(f"""
    {linha}
    ---> Voltando...
    {linha}    
                        """)
                    case 1:
                        print(f"""
    {linha}
    ---> Você pode fazer uma doação para o programa por meio 
    do nosso website oficial(em produção), preenchendo o  
    formulário de doação online. 
    {linha}    
                        """)
                    case 2:
                        print(f"""
    {linha}
    ---> Aceitamos diversos métodos de pagamento, incluindo
    cartões de crédito/débito, Pix, transferência bancária
    e serviços de pagamento online, como PayPal. 
    {linha}    
                    """)
                    case 3:
                        print(f"""
    {linha}
    ---> Aceitamos qualquer contribuição, desde pequenos até
    grandes valores. Portanto não há valor mínimo ou máximo 
    para doação.
    {linha}    
                        """)
                    case 4:
                        print(f"""
    {linha}
    ---> Sim, você pode fazer uma doação em nome de outra 
    pessoa. Ao preencher o formulário de doação, voçê terá a
    opção de especificar o nome do doador.
    {linha}    
                        """)
                    case _:
                        subalgoritmos.exibir_opcao_invalida()
        case 6:
            # Menu de doações

            if tipo_cadastro == "Supermercado" or tipo_cadastro == "Empresa":
                doacao_realizada = True
                while repetir_doacao == "s" or repetir_doacao == "S":
                    print(f"""
        {linha}
        ||                         DOAÇÕES                         ||
        {linha}
        || 1 --> Alimento                                          ||
        || 2 --> Dinheiro                                          ||
        {linha}
                    """)
                    escolha_doacao = int(input("---> Como Supermercado/Empresa, deseja realizar a doação de: "))
                    match escolha_doacao:
                        case 1:

                            # Doação de Alimento
                            print("Doação de alimento selecionada!\n(Este tipo de doação não faz parte do nosso "
                                  "benefício EatCard)")
                            tipo_alimento = input("Digite o alimento que deseja doar: ")
                            marca_alimento = input("Marca: ")
                            quant_alimento = input("Quantidade: ")
                            doacao.append(subalgoritmos.menu_ongs_doacao(escolha_doacao, tipo_alimento, quant_alimento))
                            repetir_doacao = input("\nDeseja realizar outra doação ? [S/N]: ").upper()
                        case 2:

                            # Doação em Dinheiro
                            print("Doação de dinheiro selecionada!")
                            while True:
                                try:
                                    valor_doacao = float(input("Valor: R$ "))
                                    break
                                except ValueError:
                                    subalgoritmos.exibir_opcao_invalida()
                                    continue
                            doacao.append(subalgoritmos.menu_ongs_doacao(escolha_doacao, valor_doacao, "R$"))
                            repetir_doacao = input("\nDeseja realizar outra doação ? [S/N]: ")
                        case _:
                            subalgoritmos.exibir_opcao_invalida()

            # Mensagem caso o usuário tenha se cadastrado como ONG ou PF e tente realizar doações
            elif tipo_cadastro == "ONG" or tipo_cadastro == "Pessoa Física":
                print(f"{linha}\nNão é possível realizar doações sendo ONG ou Pessoa física...\n{linha}")
            else:

                # Exigindo cadastro case o usuário tente realizar doações
                print(f"""
    {linha}
    ---> Para ir à área de doação, primeiro deve-se 
    realizar o cadastro!!!...
    {linha}""")
            print(f"""
    {linha}
    ---> Voltando...
    {linha}    
                                    """)
        case _:
            subalgoritmos.exibir_opcao_invalida()

# Exibindo todas as ações realizadas antes de finalizar o programa
if cadastro != "":
    print(f"{linha}\n--> Dados Cadastrados {tipo_cadastro}{cadastro}\n{linha}")
if doacao_realizada:
    for i in range(0, len(doacao), 1):
        print(f"\n{linha}===={doacao[i]}\n{linha}====")
print(f"""
    {linha}
    ---> Fechando o programa!!!...
    {linha}""")
