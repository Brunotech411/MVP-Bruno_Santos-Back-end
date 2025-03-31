from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from flask_cors import CORS
from routes.instrumento import routes
from urllib.parse import unquote

from model.instrumento import Instrumento
from database.base import Session

from schemas.instrumento import (
    InstrumentoIn,
    InstrumentoOut,
    InstrumentoBusca,
    InstrumentoDel,
    InstrumentoListOut,
)
from schemas.error import ErrorSchema
from schemas.presenter import apresenta_instrumento, apresenta_instrumentos

info = Info(title="API de Instrumentação - Loop Teste", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentação", description="Documentação Swagger")
instrumento_tag = Tag(name="Instrumento", description="Operações com instrumentos")


@app.get("/", tags=[home_tag])
def home():
    """Redireciona para documentação Swagger"""
    return redirect("/openapi")


@app.post("/instrumento", tags=[instrumento_tag],
          responses={"200": InstrumentoOut, "400": ErrorSchema, "409": ErrorSchema})
def add_instrumento(form: InstrumentoIn):
    """Adiciona novo instrumento"""
    try:
        session = Session()
        instrumento = Instrumento(
            tag=form.tag,
            lrv=form.lrv,
            urv=form.urv,
            span=form.urv - form.lrv,
            data_loop=form.data_loop
        )
        session.add(instrumento)
        session.commit()
        return apresenta_instrumento(instrumento), 200
    except Exception as e:
        return {"message": f"Erro ao salvar instrumento: {str(e)}"}, 400


@app.get("/instrumentos", tags=[instrumento_tag],
         responses={"200": InstrumentoListOut, "404": ErrorSchema})
def list_instrumentos():
    """Lista todos os instrumentos"""
    session = Session()
    instrumentos = session.query(Instrumento).all()
    return apresenta_instrumentos(instrumentos), 200


@app.get("/instrumento", tags=[instrumento_tag],
         responses={"200": InstrumentoOut, "404": ErrorSchema})
def get_instrumento(query: InstrumentoBusca):
    """Busca um instrumento pelo tag"""
    session = Session()
    instrumento = session.query(Instrumento).filter_by(tag=query.tag).first()
    if not instrumento:
        return {"message": "Instrumento não encontrado"}, 404
    return apresenta_instrumento(instrumento), 200


@app.delete("/instrumento", tags=[instrumento_tag],
            responses={"200": InstrumentoDel, "404": ErrorSchema})
def delete_instrumento(query: InstrumentoBusca):
    """Remove um instrumento pelo tag"""
    tag = unquote(unquote(query.tag))
    session = Session()
    count = session.query(Instrumento).filter_by(tag=tag).delete()
    session.commit()
    if count:
        return {"message": "Instrumento removido", "tag": tag}
    return {"message": "Instrumento não encontrado"}, 404


if __name__ == "__main__":
    app.run(debug=True)
