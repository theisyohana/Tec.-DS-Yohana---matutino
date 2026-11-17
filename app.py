
import psycopg2
import os

#conectar ao banco de dados
import psycopg2

conexao = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="rh",
    user="postgres",
    password="2412",
    )

#faz oque o código pedir dentro do banco de dados
cursor = conexao.cursor()

#descobrir a pasta e fazer a lista dos arquivos
pasta = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "banco_de_dados"
)

arquivos = [
    "empresa.sql",
    "funcionarios.sql",
    "candidatos.sql",
    "departamentos.sql",
    "vagas.sql"
]

#ve cada arquivo da lista e manda para o cursor (conexao.cursor)
for arquivo in arquivos:
    caminho = os.path.join(pasta, arquivo)

    with open(caminho, "r", encoding="utf-8") as sql:
        comando = sql.read()

    cursor.execute(comando)
    conexao.commit()

#cadastro de empresa
def inserir_empresa(nome_empresa, cnpj, endereco, telefone_empresa):

    sql = """
    INSERT INTO empresa (nome, cnpj, endereco, telefone)
    VALUES (%s, %s, %s, %s) 
    """
    #(%s, %s, %s, %s) -> espaços vazios para preencher
    cursor.execute(
            sql,
            (nome_empresa, cnpj, endereco, telefone_empresa)
        )

    conexao.commit() #"botão salvar"
    print("Empresa registrada com sucesso!")

#mostrar as empresa
def ver_empresas():
    cursor.execute("SELECT * FROM empresa") #seleciona tudo oque tem dentro da "empresa" e mostra
    empresas = cursor.fetchall() #tras tudo oque selecionou

    if not empresas:
        print("Nenhuma empresa cadastrada.")
        return

    for empresa in empresas:
        print(f"""
ID: {empresa[0]}
Nome: {empresa[1]}
CNPJ: {empresa[2]}
Endereço: {empresa[3]}
Telefone: {empresa[4]}""")


#cadastrar funcionários
def inserir_funcionario(nome, cpf, telefone):

    sql = """
    INSERT INTO funcionarios (nome, cpf, telefone)
    VALUES (%s, %s, %s)
    """
    cursor.execute(sql, (nome, cpf, telefone))
    conexao.commit()

    print("Funcionário registrado com sucesso!")

#ver funcionários
def ver_funcionarios():
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()

    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return

    for funcionario in funcionarios:
        print(f"""
ID: {funcionario[0]}
Nome: {funcionario[1]}
CPF: {funcionario[2]}
Telefone: {funcionario[3]}
""")

#cadastrar candidatos
def cadastrar_candidatos(nome, cpf, telefone, vaga):
    sql = """
        INSERT INTO candidatos (nome, cpf, telefone, vaga)
        VALUES (%s, %s, %s, %s)
        """
    cursor.execute(sql, (nome, cpf, telefone, vaga))
    conexao.commit()
    
    print("Candidato registrado com sucesso!")

#ver candidatos
def ver_candidatos():
    cursor.execute("SELECT * FROM candidatos")
    candidatos = cursor.fetchall()

    if not candidatos:
        print("Nenhum candidato cadastrado.")
        return

    for candidato in candidatos:
        print(f"""
ID: {candidato[0]}
Nome: {candidato[1]}
CPF: {candidato[2]}
Telefone: {candidato[3]}
Vaga: {candidato[4]}
""")

#cadastrar vagas
def cadastrar_vagas(vagas, cargo_vagas, salario_vagas):
    sql = """
        INSERT INTO vagas (cargo, salario, vagas)
        VALUES (%s, %s, %s)
        """
    cursor.execute(sql, (vagas, cargo_vagas, salario_vagas))
    conexao.commit()
    
    print("Vaga registrado com sucesso!")

#ver vagas
def ver_vagas():
    cursor.execute("SELECT * FROM vagas")
    vagas = cursor.fetchall()

    if not vagas:
        print("Nenhuma vaga cadastrada.")
        return

    for vagas in vagas:
        print(f"""
ID: {vagas[0]}
Cargo: {vagas[1]}
Salario: {vagas[2]}
Vaga: {vagas[3]}
""")

#cadastrar departamento
def cadastrar_departamento(nome_departamento, responsavel):
    sql = """
        INSERT INTO departamentos (nome, responsavel)
        VALUES (%s, %s)
        """
    cursor.execute(sql, (nome_departamento, responsavel))
    conexao.commit()
    
    print("Departamento registrado com sucesso!")

#mostrar departamento
def ver_departamento():
    cursor.execute("SELECT * FROM departamentos")
    departamentos = cursor.fetchall()

    if not departamentos:
        print("Nenhum departamento cadastrado.")
        return

    for departamentos in departamentos:
        print(f"""
ID: {departamentos[0]}
Nome do departamento: {departamentos[1]}
responsável do departamento: {departamentos[2]}
""")

#painel
while True:
    print("1 - Empresas")
    print("2 - Funcionários")
    print("3 - Candidatos")
    print("4 - Vagas")
    print("5 - Departamentos")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        print("\n1 - Registrar empresa")
        print("2 - Ver empresas")
        opcao_empresa = input("Digite a opção: ")

        #se a pessoa escolher 1, irá registrar empresa
        if opcao_empresa == "1":

                nome_empresa = input("Digite o nome da empresa: ")
                cnpj = input("Digite o CNPJ da empresa: ")
                endereco = input("Digite o endereço da empresa: ")
                telefone_empresa = input("Digite o telefone da empresa: ")

                inserir_empresa(nome_empresa,cnpj,endereco,telefone_empresa)

        #se a pessoa escolher 2, irá ver as empresas cadastradas
        elif opcao_empresa == "2":
            ver_empresas()

        else:
            print("Opção inválida!")

    elif opcao == "2":
        print("\n1 - Registrar funcionário")
        print("2 - Ver funcionários")
        opcao_funcionario = input("Digite a opção: ")

        #se a pessoa escolher 1, irá registrar funcionário
        if opcao_funcionario == "1":

            nome_funcionario = input("Digite o nome do funcionário: ")
            cpf_funcionario = input("Digite o CPF do funcionário: ")
            telefone_funcionario = input("Digite o telefone do funcionário: ")

            inserir_funcionario(nome_funcionario,cpf_funcionario,telefone_funcionario)

        #se a pessoa escolher 1, irá mostrar os funcionários registrados
        elif opcao_funcionario == "2":
            ver_funcionarios()

        else:
            print("Opção inválida!")

    elif opcao == "3":
        print("\n1 - Registrar candidato")
        print("2 - Ver candidatos")
        opcao_candidatos = input("Digite a opção: ")

        #se a pessoa escolher 1, irá registrar candidato
        if opcao_candidatos == "1":
            nome_candidato = input("Digite o nome do candidato: ")
            cpf_candidato = input("Digite o CPF do candidato: ")
            telefone_candidato = input("Digite o telefone do candidato: ")
            vaga_candidato = input("Digite a vaga que o candidato deseja: ")

            cadastrar_candidatos(nome_candidato, cpf_candidato, telefone_candidato, vaga_candidato)

        #se a pessoa escolher 2, irá monstrar candidatos cadastrados
        elif opcao_candidatos == "2":
            ver_candidatos()

        else:
            print("Opção inválida!")

    elif opcao == "4":
        print("\n1 - Registrar vaga")
        print("2 - Ver vagas")
        opcao_vagas = input("Digite a opção: ")
        
        #se a pessoa escolher 1, irá registrar vagas
        if opcao_vagas == "1":
            vagas = input("Digite a vaga: ")
            cargo_vagas = input("Digite o cargo da vaga: ")
            salario_vagas = float(input("Digite o salário da vaga: "))

            cadastrar_vagas(vagas, cargo_vagas, salario_vagas)

        #se a pessoa escolher 2, irá monstrar vagas cadastrados
        elif opcao_vagas == "2":
            ver_vagas()

        else: 
            print("Opção inválida!")

    elif opcao == "5":
        print("\n1 - Registrar departamento")
        print("2 - Ver departamentos")
        opcao_departamentos = input("Digite a opção: ")

        #se a pessoa escolher 1, irá registrar departamentos
        if opcao_departamentos == "1":
            nome_departamento = input("Digite o nome do departamento: ")
            responsavel_departamento = input("Digite o nome do responsável do departamento: ")
            cadastrar_departamento(nome_departamento, responsavel_departamento)

        elif opcao_departamentos == "2":
            ver_departamento()

        else:
            print("Opção inválida!")

    elif opcao == "6":
        print("Laço quebrado")
        break

    else:
        print("Opção inválida!")

conexao.close()
