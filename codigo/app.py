import os
from datetime import datetime

# Pega o diretório exato onde este arquivo (app.py) está salvo
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_LOG = os.path.join(DIRETORIO_ATUAL, "log.txt")

def registrar_log(mensagem):
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open(CAMINHO_LOG, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{data}] {mensagem}\n")

def ler_logs():
    # Verifica se o arquivo existe antes de tentar ler para evitar erros
    if not os.path.exists(CAMINHO_LOG):
        print("Nenhum registro encontrado.")
        return

    with open(CAMINHO_LOG, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    if conteudo:
        print(conteudo)
    else:
        print("Nenhum registro encontrado.")

def limpar_logs():
    with open(CAMINHO_LOG, "w", encoding="utf-8") as arquivo:
        arquivo.write("")

    print("Logs apagados com sucesso!")

print("Os registros ficam na pasta:", DIRETORIO_ATUAL)

while True:
    print("\n1 - Empresas")
    print("2 - Registrar um funcionário")
    print("3 - Limpar registros")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n 1 - Registrar empresa")
        print("2 - Ver empresa")

        opcao_empresa = input("Digite a opção: ")
        if opcao_empresa == "1":
            nome_empresa = input("Digite o nome da empresa: ")
            cnpj = input("Digite o CNPJ da empresa: ")
            endereco_empresa = input("Digite o endereço da empresa: ")
            telefone_empresa = input("Digite o telefone da empresa: ")
            registrar_log(
                f"EMPRESA | Nome: {nome_empresa} | CNPJ: {cnpj} | "
                f"Endereço: {endereco_empresa} | Telefone: {telefone_empresa}"
            )
            print("Empresa registrada!")

        if opcao_empresa == "2":
            ler_logs()

    elif opcao == "2":
        print("\n 1 - Registrar empresa")
        print("2 - Ver empresa")
        
        opcao_empresa = input("Digite a opção: ")
        if opcao_empresa == "1":
            nome_empresa = input("Digite o nome da empresa: ")
            cnpj = input("Digite o CNPJ da empresa: ")
            endereco_empresa = input("Digite o endereço da empresa: ")
            telefone_empresa = input("Digite o telefone da empresa: ")
            registrar_log(
            f"EMPRESA | Nome: {nome_empresa} | CNPJ: {cnpj} | "
            f"Endereço: {endereco_empresa} | Telefone: {telefone_empresa}"
            )
            print("Empresa registrada!")

    elif opcao == "3":
        limpar_logs()

    elif opcao == "4":
        break

    else:
        print("Opção inválida!")