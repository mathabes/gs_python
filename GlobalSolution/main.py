import subalgoritmos

linha = "=" * 61
escolha_menu = 1
ong = ""
empresa = ""
mercado = ""
pessoa_fisica = ""
dados_necessarios_ong = ["Nome", "Email", "Telefone", "Endereço", "CNPJ", "Razão Social"]
dados_necessarios_empresa = ["Nome Fantasia", "Email", "Telefone", "Endereço", "CNPJ", "Razão Social", "Renda Mensal"]
dados_necessarios_mercado = ["Nome Fantasia", "Email", "Telefone", "Endereço", "CNPJ", "Razão Social", "Renda Mensal"]
dados_necessarios_pessoa_fisica = ["Nome", "Email(opcional)", "Telefone(opcional)", "Endereço", "CPF", "RG",
                                   "Renda Mensal"]
escolha_duvida = 1
duvidas = ["Como posso fazer uma doação para o programa?", "Quais os métodos de pagamento aceitos para doações?",
           "Existe um valor mínimo para as doações?", "Posso fazer uma doação em nome de outra pessoa?"]
print(f"""
    {linha}
    {linha}
        """)
while escolha_menu != 0:
    print(f"""
    {linha}
    ||                         M E N U                         ||
    {linha}
    || Cadastre-se como:                                       ||
    || 1...................................: ONG para Caridade ||
    || 2............................: Empresa Parceira Doadora ||
    || 3...............................: Supermercado parceiro ||
    || 4..............: Família em necessidade (Pessoa Física) ||
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
            print(f"\n{linha}\n--> CADASTRO ONG:")
            ong = subalgoritmos.cadastro_parceiros(dados_necessarios_ong)
            print(linha)
        case 2:
            print(f"\n{linha}\n--> CADASTRO EMPRESA:")
            empresa = subalgoritmos.cadastro_parceiros(dados_necessarios_empresa)
            print(linha)
        case 3:
            print(f"\n{linha}\n--> CADASTRO SUPERMERCADO:")
            mercado = subalgoritmos.cadastro_parceiros(dados_necessarios_mercado)
            print(linha)
        case 4:
            print(f"\n{linha}\n--> CADASTRO PESSOA FÍSICA:\n(apenas digite ENTER para dados opcionais)")
            pessoa_fisica = subalgoritmos.cadastro_parceiros(dados_necessarios_pessoa_fisica)
            print(linha)
        case 5:
            while escolha_duvida != 0:
                escolha_duvida = subalgoritmos.exibir_menu_duvidas(duvidas)
                match escolha_duvida:
                    case 0:
                        break
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
        case _:
            subalgoritmos.exibir_opcao_invalida()
if ong != "":
    print(f"{linha}\n--> Dados Cadastrados ONG{ong}\n{linha}")
if empresa != "":
    print(f"{linha}\n--> Dados Cadastrados Empresa{empresa}\n{linha}")
if mercado != "":
    print(f"{linha}\n--> Dados Cadastrados Supermercado{mercado}\n{linha}")
if pessoa_fisica != "":
    print(f"{linha}\n--> Dados Cadastrados Pessoa Física{pessoa_fisica}\n{linha}")
print(f"""
    {linha}
    ---> Fechando o programa!!!...
    {linha}""")
