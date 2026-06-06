💰 Gerenciador de Gastos Pessoais

Projeto desenvolvido para a disciplina de DevOps, com o objetivo de aplicar conceitos de conteinerização utilizando Docker, integração entre frontend e backend, persistência de dados e desenvolvimento de APIs REST.



📋 Descrição

O Gerenciador de Gastos Pessoais é uma aplicação web que permite ao usuário registrar receitas e despesas, acompanhar seu saldo financeiro e visualizar relatórios de movimentação mensal.



A aplicação foi construída utilizando:



Frontend em HTML, CSS e JavaScript

Backend em Python com Flask

Banco de dados SQLite

Docker e Docker Compose para conteinerização

🚀 Funcionalidades

Lançamentos Financeiros

Cadastro de receitas

Cadastro de gastos

Definição de categoria

Registro automático da data

Exclusão individual de lançamentos

Exclusão completa dos lançamentos

Dashboard Financeiro

Saldo atual

Total de receitas

Total de gastos

Saldo mensal

Atualização automática dos indicadores

Relatórios

Resumo financeiro por mês

Receitas por período

Gastos por período

Saldo mensal

Maior gasto registrado em cada mês

🏗️ Arquitetura

Frontend (Nginx)

&#x20;       │

&#x20;       ▼

Backend (Flask API)

&#x20;       │

&#x20;       ▼

Banco SQLite

📂 Estrutura do Projeto

projeto/

│

├── frontend/

│   ├── index.html

│   ├── relatorios.html

│   └── Dockerfile

│

├── backend/

│   ├── app.py

│   ├── database.py

│   ├── requirements.txt

│   └── Dockerfile

│

├── docker-compose.yml

│

└── README.md

🐳 Executando com Docker

Clonar o repositório

git clone <url-do-repositorio>

cd projeto

Construir e iniciar os containers

docker compose up

Ou em segundo plano:



docker compose up -d

🌐 Acesso

Após a inicialização:



Frontend:



http://localhost:8080

Backend:



http://localhost:5000

📦 Dependências do Backend

Arquivo requirements.txt:



flask==3.0.3

flask-cors==4.0.1

Instalação manual:



pip install -r requirements.txt

🔗 Endpoints da API

Verificar Status

GET /

Resposta:



{

&#x20; "mensagem": "API funcionando",

&#x20; "status": "ok"

}

Listar Lançamentos

GET /lancamentos

Adicionar Lançamento

POST /lancamentos

Exemplo:



{

&#x20; "descricao": "Salário",

&#x20; "valor": 2500,

&#x20; "tipo": "receita",

&#x20; "categoria": "Outros"

}

Excluir Lançamento

DELETE /lancamentos/{id}

Excluir Todos os Lançamentos

DELETE /lancamentos

Resumo Financeiro

GET /resumo

Retorna:



{

&#x20; "saldo\_atual": 1500,

&#x20; "receitas\_mes": 2500,

&#x20; "gastos\_mes": 1000,

&#x20; "saldo\_mes": 1500

}

Relatórios Mensais

GET /relatorios

💾 Persistência de Dados

A aplicação utiliza SQLite para armazenamento local dos lançamentos financeiros.



Os dados são persistidos através de volume Docker, permitindo que as informações permaneçam salvas mesmo após a reinicialização dos containers.



👨‍💻 Equipe

Maria Eduarda Trevizane

Maria Clara Trevizane

Luís Fernando Andrade

João Vitor Rodrigues

📚 Tecnologias Utilizadas

HTML5

CSS3

JavaScript

Python 3.11

Flask

Flask-CORS

SQLite

Docker

Docker Compose

Nginx

🎯 Objetivo Acadêmico

Este projeto foi desenvolvido para demonstrar a aplicação prática dos conceitos de DevOps, incluindo:



Conteinerização de aplicações

Gerenciamento de dependências

Comunicação entre serviços

Persistência de dados

Automação de ambiente de execução

Padronização de deploy

