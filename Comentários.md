
# Devolutiva formativa — Atividade 02 da SA

**Estudante:** Yohana Müller Theis  
**Turma:** Rio Negrinho — Manhã  
**Unidade Curricular:** Programação de Aplicativos  
**Projeto:** Sistema de Recursos Humanos  
**Atividade:** Interface funcional  
**Arquivos analisados:** `codigo/app.py`, `interface/index.html` e `interface/style.css`

## O que você já conseguiu desenvolver

Yohana, você criou uma interface web para um sistema de Recursos Humanos com login demonstrativo, navegação entre setores e diferentes formulários.

O código apresenta comentários explicativos e organização visual por áreas.

Pontos positivos identificados:

- Criou uma página com estrutura HTML organizada.
- Desenvolveu CSS para a apresentação das telas.
- Criou login demonstrativo com JavaScript.
- Implementou mensagens de erro para entradas inválidas no login.
- Utilizou `sessionStorage` para controlar o estado da interface.
- Desenvolveu navegação entre as áreas do RH.
- Criou formulários para empresas, funcionários, candidatos, vagas e departamentos.
- Aplicou campos obrigatórios e tipos de entrada específicos.
- Organizou o Python em funções de cadastro e consulta.
- Implementou operações SQL para trabalhar com PostgreSQL.
- Incluiu comentários explicando o comportamento de diversos componentes.

## O que foi ajustado desde a última devolutiva

### 1. Cadastro de funcionários — ATENDIDO NO PYTHON

Na avaliação anterior, a opção destinada aos funcionários repetia o cadastro de empresas.

A versão atual possui uma função específica, `inserir_funcionario()`, além de `ver_funcionarios()`.

**Correção identificada:** os registros de funcionários agora possuem operações próprias no Python.

### 2. Separação das informações — ATENDIDO NO PYTHON

A implementação anterior utilizava um arquivo de texto para registrar informações.

Agora existem operações SQL específicas para empresas, funcionários, candidatos, vagas e departamentos.

**Evolução positiva:** as informações passaram a ser organizadas por entidades.

### 3. Organização da interface — ATENDIDO

A nova entrega apresenta telas e formulários relacionados às diferentes áreas do sistema de RH.

A navegação e o login demonstrativo são implementados por JavaScript.

### 4. Validações — PARCIALMENTE ATENDIDO

A interface utiliza campos obrigatórios e alguns tipos de entrada apropriados.

Entretanto, ainda é necessário implementar verificações completas para os dados que serão armazenados.

## O que precisa ser corrigido

### 5. Integrar os formulários HTML ao Python

Os formulários de cadastro utilizam `action="#"`, e o JavaScript disponível não apresenta chamadas às funções Python responsáveis pelas operações SQL.

**Como melhorar:** criar uma aplicação Flask com rotas para receber os formulários e chamar as funções de cadastro. Exibir mensagens de sucesso ou erro após cada operação.

O próximo passo não é refazer o HTML, mas conectar a interface existente à lógica do sistema.

### 6. Corrigir a primeira linha do arquivo Python

O arquivo `codigo/app.py` começa com a expressão isolada `interface`, que não corresponde a uma variável definida.

**Como melhorar:** remover essa linha para permitir que o programa prossiga normalmente para as importações e a conexão com o banco.

### 7. Proteger as credenciais

O código Python contém uma credencial de banco diretamente no arquivo, e o login da interface utiliza credenciais fixas em JavaScript.

**Como melhorar:** substituir a credencial do banco já publicada, não armazenar novas senhas no código e utilizar configurações de ambiente. Para uma autenticação real, a verificação deverá ocorrer no servidor.

### 8. Corrigir a localização dos scripts SQL

O Python procura arquivos SQL em uma pasta relativa ao diretório `codigo`, enquanto os arquivos SQL do repositório estão em `banco_de_dados`, na raiz.

Além disso, os arquivos SQL publicados estão vazios.

**Como melhorar:** ajustar o caminho, disponibilizar os comandos SQL necessários e conferir sua execução.

## Oportunidades de melhoria

### 9. Melhorar a modularização

**Como melhorar:** separar funções de banco de dados, rotas da aplicação e validações, mantendo a interface responsável pela apresentação.

### 10. Melhorar as validações numéricas

A leitura do salário no Python utiliza `float()` diretamente.

**Como melhorar:** tratar entradas inválidas com `try/except` e impedir valores incompatíveis com as regras do cadastro.

### 11. Ampliar a documentação

**Como melhorar:** atualizar o README com instruções para configurar o PostgreSQL, executar a aplicação e utilizar os formulários.

## Testes recomendados

1. Abrir a interface HTML e conferir o CSS.
2. Testar o login demonstrativo com entradas válidas e inválidas.
3. Navegar pelas cinco áreas do RH.
4. Atualizar a página e conferir a área selecionada.
5. Executar o código Python sem a linha inicial incorreta.
6. Verificar a conexão com o PostgreSQL.
7. Cadastrar uma empresa com dados fictícios.
8. Cadastrar e consultar um funcionário.
9. Verificar os caminhos dos scripts SQL.
10. Após a integração, cadastrar informações diretamente pela interface web.

## Prioridades para a próxima versão

1. **Corrigir a inicialização do Python.**
2. **Retirar e substituir as credenciais publicadas.**
3. **Conectar os formulários HTML às operações Python.**
4. **Corrigir os caminhos e o conteúdo dos scripts SQL.**
5. **Ampliar as validações e os testes de integração.**

## Mensagem final

Yohana, você apresentou evolução na organização das informações e na construção de uma interface para diferentes áreas do RH.

O desenvolvimento de formulários, navegação e operações SQL demonstra conhecimentos importantes.

Seu próximo desafio é unir esses componentes em uma aplicação integrada, garantindo que as ações realizadas no navegador sejam processadas corretamente pelo Python.
