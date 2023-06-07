linha = "=" * 61


# Função utilizada sempre que é necessário exibir uma mensagem de opção inválida
def exibir_opcao_invalida() -> None:
    print(f"""
    {linha}
    --> DIGITE UMA OPÇÃO VÁLIDA!!!...
    {linha}    
    """)


# Função para o cadastro do usuário em qualquer tipo de conta, recebendo os dados necessários por parâmetro
def cadastro_parceiros(dados_necessarios) -> str:
    dados_informados = ""
    dados = []
    for i in range(0, len(dados_necessarios), 1):
        if dados_necessarios[i] == "Renda Mensal" or dados_necessarios[i] == "Quantidade de pessoas associadas":
            dados.append(cadastro_dado_float(dados_necessarios[i]))
            dados_informados += f"\n|| {dados_necessarios[i]}: R$ {dados[i]}"
        else:
            dados.append(input(f"{dados_necessarios[i]}: "))
            if dados[i] == "":
                dados[i] = "-"
            dados_informados += f"\n|| {dados_necessarios[i]}: {dados[i]}"
    return dados_informados


# Função para o cadastro especificamente de dados float, completando a função acima
def cadastro_dado_float(dado) -> float:
    valor_digitado = 0
    while True:
        try:
            valor_digitado = float(input(f"{dado}: "))
            break
        except ValueError:
            exibir_opcao_invalida()
            continue
    return valor_digitado


# Função para exibir um menu de duvidas, recebendo as questões por parâmetro
def exibir_menu_duvidas(duvidas) -> int:
    escolha = 1
    print(f"""
    {linha}
    ||                   Dúvidas Frequentes                    ||
    {linha}""")
    for i in range(0, len(duvidas), 1):
        print(f"     {i + 1} -> {duvidas[i]:50}")
    print("     0 -> Voltar\n   ", linha, "\n")
    while True:
        try:
            escolha = int(input("Digite a opção que pode corresponder a sua dúvida: "))
            break
        except ValueError:
            exibir_opcao_invalida()
            continue
    return escolha


# Função que finaliza a área de doaçao, exibindo as ongs pré-cadastradas
# e recebendo tanto o tipo da doação, quanto seu contéudo
def menu_ongs_doacao(escolha_doacao, conteudo_doacao, medida) -> str:
    escolha = 0
    ongs = ["Caça-Fome", "Esperança Global", "Resgate da Dignidade", "Luz da Esperança"]
    print(f"""
    {linha}
    ||                          ONGS                           ||
    {linha}
    || 1...........................................: Caça-Fome ||
    || 2....................................: Esperança Global ||
    || 3................................: Resgate da Dignidade ||
    || 4....................................: Luz da Esperança ||
    {linha}
    """)
    while True:
        try:
            escolha = int(input("Digite a qual ONG irá doar: "))
            break
        except ValueError:
            exibir_opcao_invalida()
            continue
    if escolha_doacao == 1:
        print(f"\n--> Doação de {medida} de {conteudo_doacao} cadastrada para a ONG {ongs[escolha - 1]}.")
        resp_doacao = f"\n--> Doação de {medida} de {conteudo_doacao} cadastrada para a ONG {ongs[escolha - 1]}."
    else:
        print(f"\n--> Doação cadastrada a {ongs[escolha - 1]} no valor de {medida} {conteudo_doacao}.")
        resp_doacao = f"\n--> Doação cadastrada a {ongs[escolha - 1]} no valor de {medida} {conteudo_doacao}."
    return resp_doacao
