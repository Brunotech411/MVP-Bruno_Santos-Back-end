🔧 API de Instrumentação - Loop Teste

Este é o back-end do MVP da sprint desenvolvimento Full Stack básico (PUC-Rio). A API permite o cadastro, listagem, busca e remoção de instrumentos com loop test concluído, incluindo o cálculo automático do SPAN (URV - LRV). 
OBS: o foco do loop test são instrumentos de medição das grandezas nível(LIT), pressão(PIT), vazão(FIT) e temperatura(TIT) de uma planta de processo qualquer.
A atividade loop teste consiste na verificação de indicação correta em uma sala de controle o que confirma o funcionamento do instrumento e conclui o comissionamento, liberando o mesmo para a operação.



✅ Funcionalidades
📥 Cadastrar novos instrumentos
📃 Listar todos os instrumentos
🔍 Buscar instrumento por TAG
🗑️ Remover instrumento por TAG
📐 Calcular e armazenar automaticamente o campo span


⚙️ Tecnologias utilizadas
Python 3.11+
Flask 2.1.3
flask-openapi3 2.1.0
Flask-CORS
SQLAlchemy
SQLite


📁 Estrutura do projeto
MVP-Bruno_Santos-Back-end/
│
├── app.py                  # Aplicação principal Flask
├── create_db.py           # Criação da base de dados
├── instrumentos.db        # Banco SQLite (gerado automaticamente)
├── requirements.txt       # Dependências do projeto
├── .gitignore             # Arquivos ignorados no versionamento
│
├── database/
│   └── base.py            # Configuração do SQLAlchemy (engine, session)
│
├── model/
│   └── instrumento.py     # Modelo da tabela de instrumentos
│
├── schemas/
│   ├── instrumento.py     # Schemas Pydantic para entrada e saída
│   ├── presenter.py       # Funções que formatam as respostas
│   └── error.py           # Schema de erro padrão
│
├── routes/
│   └── instrumento.py     # Rotas organizadas por blueprint
│
├── v_env1_api/            # Ambiente virtual (não versionado)


🧪 Como rodar o projeto

1. Clone o repositório
git clone https://github.com/Brunotech411/MVP-Bruno_Santos-Back-end

2. Crie e ative o ambiente virtual
python -m venv v_env1_api
._env1_api\Scriptsctivate

3. Instale as dependências
pip install -r requirements.txt

4. Crie a base de dados
python create_db.py

5. Rode a aplicação
python app.py

📚 Documentação Swagger
Após iniciar o servidor, acesse:

👉 http://localhost:5000/openapi

Você poderá testar todas as rotas diretamente no navegador.

🔄 Rotas disponíveis
POST /instrumento
Cadastrar um novo instrumento.

GET /instrumentos
Listar todos os instrumentos cadastrados.

GET /instrumento
Buscar um instrumento por TAG.

DELETE /instrumento
Remover um instrumento por TAG.

🧠 Observações técnicas
A coluna span é calculada automaticamente (urv - lrv) e armazenada no banco de dados.

🙌 Autor
Bruno Leonardo Ramos dos Santos
LinkedIn: https://www.linkedin.com/in/bruno-leonardo-ramos-dos-santos-31734b3a/