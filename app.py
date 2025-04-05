# Importa recursos principais do flask_openapi3 para construir a API com documentação
from flask_openapi3 import OpenAPI, Info, Tag

# Importa função para redirecionamento de rota
from flask import redirect

# Importa suporte a CORS (liberação de requisições entre diferentes domínios)
from flask_cors import CORS

# (opcional) Importação de rotas separadas, caso use organização modular
from routes.instrumento import routes

# Importa função para decodificar URLs (ex: espaços e caracteres especiais)
from urllib.parse import unquote

# Modelo ORM do instrumento (mapeamento objeto-relacional)
from model.instrumento import Instrumento

# Conexão com o banco de dados (cria sessões SQLAlchemy)
from database.base import Session

# Schemas para validação e documentação de entrada e saída (via Pydantic)
from schemas.instrumento import (
    InstrumentoIn,         # Schema de entrada (formulário)
    InstrumentoOut,        # Schema de saída
    InstrumentoBusca,      # Schema para busca por TAG
    InstrumentoDel,        # Schema de retorno para remoção
    InstrumentoListOut     # Schema de listagem
)

# Schema para mensagens de erro padronizadas
from schemas.error import ErrorSchema

# Funções para formatar os dados antes de responder
from schemas.presenter import apresenta_instrumento, apresenta_instrumentos

# Define título e versão da API na interface Swagger
info = Info(title="API de Instrumentação - Loop Teste", version="1.0.0")

# Inicializa a aplicação Flask integrada ao OpenAPI
app = OpenAPI(__name__, info=info)

# Libera requisições de outros domínios (CORS) — útil para o front end local
CORS(app)

# Define tags utilizadas na documentação Swagger
home_tag = Tag(name="Documentação", description="Documentação Swagger")
instrumento_tag = Tag(name="Instrumento", description="Operações com instrumentos")

# Rota inicial que redireciona para a documentação Swagger
@app.get("/", tags=[home_tag])
def home():
    """Redireciona para documentação Swagger"""
    return redirect("/openapi")

# Rota para criar um novo instrumento na base (POST)
@app.post("/instrumento", tags=[instrumento_tag],
          responses={"200": InstrumentoOut, "400": ErrorSchema, "409": ErrorSchema})
def add_instrumento(form: InstrumentoIn):
    """Adiciona novo instrumento"""
    try:
        session = Session()  # Cria conexão com o banco
        instrumento = Instrumento(
            tag=form.tag,
            lrv=form.lrv,
            urv=form.urv,
            span=form.urv - form.lrv,      # Calcula o SPAN automaticamente
            data_loop=form.data_loop
        )
        session.add(instrumento)   # Adiciona o objeto à sessão
        session.commit()           # Salva no banco
        return apresenta_instrumento(instrumento), 200  # Retorna a resposta formatada
    except Exception as e:
        return {"message": f"Erro ao salvar instrumento: {str(e)}"}, 400

# Rota para listar todos os instrumentos cadastrados (GET)
@app.get("/instrumentos", tags=[instrumento_tag],
         responses={"200": InstrumentoListOut, "404": ErrorSchema})
def list_instrumentos():
    """Lista todos os instrumentos"""
    session = Session()
    instrumentos = session.query(Instrumento).all()
    return apresenta_instrumentos(instrumentos), 200

# Rota para buscar um instrumento específico por TAG (GET com query param)
@app.get("/instrumento", tags=[instrumento_tag],
         responses={"200": InstrumentoOut, "404": ErrorSchema})
def get_instrumento(query: InstrumentoBusca):
    """Busca um instrumento pelo tag"""
    session = Session()
    instrumento = session.query(Instrumento).filter_by(tag=query.tag).first()
    if not instrumento:
        return {"message": "Instrumento não encontrado"}, 404
    return apresenta_instrumento(instrumento), 200

# Rota para deletar um instrumento via TAG (DELETE com query param)
@app.delete("/instrumento", tags=[instrumento_tag],
            responses={"200": InstrumentoDel, "404": ErrorSchema})
def delete_instrumento(query: InstrumentoBusca):
    """Remove um instrumento pelo tag"""
    tag = unquote(unquote(query.tag))  # Decodifica a URL caso contenha espaços ou símbolos
    session = Session()
    count = session.query(Instrumento).filter_by(tag=tag).delete()
    session.commit()
    if count:
        return {"message": "Instrumento removido", "tag": tag}
    return {"message": "Instrumento não encontrado"}, 404

# Inicializa a aplicação quando executado diretamente (modo debug ativado)
if __name__ == "__main__":
    app.run(debug=True)
