
# Devolutiva formativa — Atividade 01 da SA

**Estudante:** Yohana  
**Turma:** Rio Negrinho — Manhã  
**Unidade Curricular:** Programação de Aplicativos  
**Projeto:** Empresa de Recursos Humanos  
**Código analisado:** `codigo/app.py`  
**Referência:** Situação de Aprendizagem nº 1 — *Da Ideia ao Código*

## O que você já conseguiu desenvolver

Yohana, você iniciou um sistema relacionado a uma empresa de Recursos Humanos. Seu projeto utiliza Python para registrar e consultar informações por meio de um arquivo de texto, demonstrando o uso de funções e operações com arquivos.

Pontos positivos identificados:

- Criou uma função `registrar_log()` para gravar informações em arquivo.
- Utilizou `datetime` para registrar a data e o horário das operações.
- Implementou uma função `ler_logs()` para consultar registros anteriores.
- Criou a função `limpar_logs()` para apagar o conteúdo do arquivo.
- Utilizou `os.path` para localizar o arquivo de registros em relação ao local do programa.
- Aplicou **funções, condicionais, repetição e manipulação de arquivos**.
- Criou um menu inicial para organizar as operações.

## O que precisa ser corrigido

### 1. Corrigir a opção de cadastro de funcionários

O menu principal apresenta a opção **"Registrar um funcionário"**, mas esse caminho repete o formulário de cadastro de empresa.

Atualmente, não existe um cadastro específico com dados de funcionário.

**Como melhorar:** criar uma função `cadastrar_funcionario()` com campos adequados para um cadastro fictício, como nome, cargo e empresa vinculada. A opção 2 deve chamar essa função, sem repetir o cadastro de empresas.

### 2. Diferenciar os registros de empresas e funcionários

O programa grava todas as informações como linhas de texto. No estado atual, a consulta mostra o conteúdo do arquivo sem separar registros por tipo.

**Como melhorar:** identificar claramente cada tipo de registro e criar funções de consulta específicas. Para evoluir o projeto, considere utilizar dicionários ou uma estrutura de dados que facilite pesquisas e alterações.

### 3. Validar as informações dos cadastros

Nome, CNPJ, endereço e telefone são recebidos sem verificações.

**Como melhorar:** impedir campos obrigatórios vazios, remover espaços desnecessários e conferir os formatos utilizados. Durante os testes, utilizar somente dados fictícios.

### 4. Proteger a operação de apagar registros

A opção `limpar_logs()` substitui todo o conteúdo do arquivo por uma string vazia, apagando os registros existentes sem solicitar confirmação.

**Como melhorar:** apresentar um aviso e exigir confirmação antes de apagar o arquivo. Em uma versão futura, diferenciar exclusão de registros e limpeza de logs técnicos.

## Oportunidades de melhoria

### 5. Evitar a duplicação de código

O formulário de cadastro de empresa aparece duas vezes no menu principal.

**Como melhorar:** criar uma função `cadastrar_empresa()` e chamá-la somente na opção correspondente. Isso facilitará a manutenção.

### 6. Separar os dados de negócio dos registros de eventos

O arquivo `log.txt` está sendo utilizado como armazenamento principal das informações cadastradas.

**Como melhorar:** diferenciar dados de empresas e funcionários de logs do sistema. Os dados podem ser mantidos inicialmente em estruturas próprias e futuramente integrados a um banco.

### 7. Melhorar o tratamento de erros de arquivo

As funções de leitura e gravação utilizam `open()`, mas não tratam situações em que o arquivo não pode ser acessado ou gravado.

**Como melhorar:** tratar erros esperados de entrada e saída, informando ao usuário quando uma operação não puder ser concluída.

### 8. Complementar a documentação

O README apresenta o tema, mas ainda precisa explicar as funcionalidades específicas do projeto.

**Como melhorar:** acrescentar o objetivo do sistema de RH, instruções de execução, estrutura das informações e exemplos de testes.

## Testes recomendados

1. Cadastrar uma empresa com dados fictícios.
2. Tentar cadastrar uma empresa com campos vazios.
3. Cadastrar um funcionário após implementar sua função.
4. Consultar separadamente empresas e funcionários.
5. Encerrar e reiniciar o programa, verificando a permanência dos dados.
6. Tentar apagar os registros e cancelar a confirmação.
7. Testar o comportamento quando o arquivo de registros não existir.
8. Informar uma opção inexistente no menu.

## Prioridades para a próxima versão

1. **Corrigir a opção de cadastro de funcionários.**
2. **Separar os registros de empresas e funcionários.**
3. **Eliminar a duplicação do formulário.**
4. **Validar os campos e proteger a exclusão de dados.**
5. **Organizar o armazenamento e documentar os testes.**

## Mensagem final

Yohana, você já aplicou conceitos importantes de **funções, entrada de dados, condições, repetição e manipulação de arquivos**. O registro de informações com data e horário é uma funcionalidade que poderá ser aproveitada na evolução do projeto.

Seu principal desafio agora é garantir que cada opção do menu execute a tarefa anunciada e que as informações sejam organizadas de forma adequada. Continue construindo o sistema por etapas, testando cada funcionalidade antes de avançar para a próxima.
