import subalgoritmos
linha = "=" * 61
duvida = ["Como posso fazer uma doação para o programa?", "Quais os métodos de pagamento aceitos para doações?",
           "Existe um valor mínimo para as doações?", "Posso fazer uma doação em nome de outra pessoa?"]
resposta = ["Você pode fazer uma doação para o programa por meio do nosso website oficial(em produção), preenchendo o formulário de doação online.",
            "Aceitamos diversos métodos de pagamento, incluindo cartões de crédito / débito, Pix, transferência bancária e serviços de pagamento online, como PayPal.",
            "Aceitamos qualquer contribuição, desde pequenos até grandes valores. Portanto não há valor mínimo ou máximo para doação.",
            "Sim, você pode fazer uma doação em nome de outra pessoa. Ao preencher o formulário de doação, voçê terá a opção de especificar o nome do doador."]

def exec_duvidas (duvidas, respostas) -> None:
    escolha = 1
    while escolha != 0:
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
                subalgoritmos.exibir_opcao_invalida()
                continue
        match escolha:
            case 0:
                break
            case 1:
                print(f"""
    {linha}
    ---> {respostas[0]} 
    {linha}    
                """)
            case 2:
                print(f"""
    {linha}
    ---> {respostas[1]} 
    {linha}    
                """)
            case 3:
                print(f"""
    {linha}
    ---> {respostas[2]}
    {linha}    
                """)
            case 4:
                print(f"""
    {linha}
    ---> {respostas[3]}
    {linha}
                """)
            case _:
                subalgoritmos.exibir_opcao_invalida()




exec_duvidas(duvida, resposta)