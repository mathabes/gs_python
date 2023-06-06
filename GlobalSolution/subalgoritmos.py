linha = "=" * 61


def exibir_opcao_invalida() -> None:
    print(f"""
    {linha}
    --> DIGITE UMA OPÇÃO VÁLIDA!!!...
    {linha}    
    """)


def cadastro_parceiros(dados_necessarios) -> str:
    dados_informados = ""
    dados = []
    for i in range(0, len(dados_necessarios), 1):
        if dados_necessarios[i] == "Renda Mensal":
            dados.append(cadastro_dado_float(dados_necessarios[i]))
            dados_informados += f"\n|| {dados_necessarios[i]}: R$ {dados[i]}"
        else:
            dados.append(input(f"{dados_necessarios[i]}: "))
            if dados[i] == "":
                dados[i] = "-"
            dados_informados += f"\n|| {dados_necessarios[i]}: {dados[i]}"
    return dados_informados


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


def menu_ongs(doacao) -> None:
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
    if doacao is float:
        print(f"Doação realizada a {ongs[escolha + 1]} no valor de {doacao} reais.")
    else:
        print(f"Doação de {doacao} realizada a {ongs[escolha + 1]}.")
