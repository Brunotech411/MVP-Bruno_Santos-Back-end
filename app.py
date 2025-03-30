from flask_openapi3 import OpenAPI, Info, Tag, Body
from flask import redirect
from urllib.parse import unquote
from flask_cors import CORS

from sqlalchemy.exc import IntegrityError
from datetime import datetime

from model import Session, Instrumento
from schemas import *

info = Info(title="API de Instrumentação - Loop Teste", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
instrumento_tag = Tag(name="Instrumento", description="Cadastro, listagem e exclusão de instrumentos")

@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')

@app.post('/instrumento', tags=[instrumento_tag],
          responses={"200": InstrumentoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_instrumento(body: InstrumentoSchema = Body(...)):
    try:
        instrumento = Instrumento(
            tag=body.tag,
            lrv=body.lrv,
            urv=body.urv,
            span=body.urv - body.lrv,
            data_loop=body.data_loop
        )
        session = Session()
        session.add(instrumento)
        session.commit()
        return instrumento.__dict__, 200

    except IntegrityError:
        return {"message": "Instrumento com esta TAG já está cadastrado."}, 409
    except Exception as e:
        return {"message": f"Erro ao tentar salvar: {str(e)}"}, 400

@app.get('/instrumentos', tags=[instrumento_tag],
         responses={"200": ListagemInstrumentosSchema, "404": ErrorSchema})
def get_instrumentos():
    session = Session()
    instrumentos = session.query(Instrumento).all()
    if not instrumentos:
        return {"instrumentos": []}, 200
    return {
        "instrumentos": [
            {
                "tag": inst.tag,
                "lrv": inst.lrv,
                "urv": inst.urv,
                "span": inst.span,
                "data_loop": inst.data_loop.isoformat()
            } for inst in instrumentos
        ]
    }, 200

@app.get('/instrumento', tags=[instrumento_tag],
         responses={"200": InstrumentoViewSchema, "404": ErrorSchema})
def get_instrumento(query: InstrumentoBuscaSchema):
    session = Session()
    instrumento = session.query(Instrumento).filter_by(tag=query.tag).first()
    if not instrumento:
        return {"message": "Instrumento não encontrado."}, 404
    return instrumento.__dict__, 200

@app.delete('/instrumento', tags=[instrumento_tag],
            responses={"200": InstrumentoDelSchema, "404": ErrorSchema})
def del_instrumento(query: InstrumentoBuscaSchema):
    tag = unquote(unquote(query.tag))
    session = Session()
    count = session.query(Instrumento).filter_by(tag=tag).delete()
    session.commit()
    if count:
        return {"mensagem": "Instrumento removido", "tag": tag}, 200
    else:
        return {"message": "Instrumento não encontrado."}, 404

if __name__ == "__main__":
    app.run(debug=True)