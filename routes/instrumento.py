from flask_openapi3 import Tag  # Tag usada na documentação Swagger
from flask import Blueprint  # Organização de rotas
from model.instrumento import Instrumento
from database.base import Session
from schemas.instrumento import (
    InstrumentoIn, InstrumentoOut, InstrumentoBusca,
    InstrumentoDel, InstrumentoListOut
)
from schemas.presenter import apresenta_instrumento, apresenta_instrumentos

# Tag usada na interface Swagger
instrumento_tag = Tag(name="Instrumento", description="Operações com instrumentos")

# Blueprint para modularização das rotas
routes = Blueprint('routes', __name__)

# Criação de um instrumento (POST)
@routes.post("/instrumento", tags=[instrumento_tag],
             responses={"200": InstrumentoOut, "400": {"message": str}})
def add_instrumento(form: InstrumentoIn):
    try:
        session = Session()
        instrumento = Instrumento(
            tag=form.tag,
            lrv=form.lrv,
            urv=form.urv,
            data_loop=form.data_loop
        )
        session.add(instrumento)
        session.commit()
        return apresenta_instrumento(instrumento), 200
    except Exception as e:
        return {"message": f"Erro ao salvar instrumento: {str(e)}"}, 400

# Listagem de todos os instrumentos (GET)
@routes.get("/instrumentos", tags=[instrumento_tag],
            responses={"200": InstrumentoListOut})
def list_instrumentos():
    session = Session()
    instrumentos = session.query(Instrumento).all()
    return apresenta_instrumentos(instrumentos), 200

# Busca de instrumento por TAG (GET com query param)
@routes.get("/instrumento", tags=[instrumento_tag],
            responses={"200": InstrumentoOut, "404": {"message": str}})
def get_instrumento(query: InstrumentoBusca):
    session = Session()
    instrumento = session.query(Instrumento).filter_by(tag=query.tag).first()
    if not instrumento:
        return {"message": "Instrumento não encontrado"}, 404
    return apresenta_instrumento(instrumento), 200

# Remoção de instrumento por TAG (DELETE com query param)
@routes.delete("/instrumento", tags=[instrumento_tag],
               responses={"200": InstrumentoDel, "404": {"message": str}})
def delete_instrumento(query: InstrumentoBusca):
    session = Session()
    count = session.query(Instrumento).filter_by(tag=query.tag).delete()
    session.commit()
    if count:
        return {"message": "Instrumento removido", "tag": query.tag}
    return {"message": "Instrumento não encontrado"}, 404
