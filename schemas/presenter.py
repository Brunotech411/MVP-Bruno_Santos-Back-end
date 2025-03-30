from schemas.instrumento import InstrumentoOut, InstrumentoListOut

def apresenta_instrumento(instrumento) -> InstrumentoOut:
    """Retorna os dados de um instrumento no formato esperado pelo schema"""
    return InstrumentoOut(
        tag=instrumento.tag,
        lrv=instrumento.lrv,
        urv=instrumento.urv,
        span=instrumento.span,
        data_loop=instrumento.data_loop
    )

def apresenta_instrumentos(lista) -> InstrumentoListOut:
    """Retorna a lista de instrumentos no formato esperado pelo schema"""
    return InstrumentoListOut(instrumentos=[
        apresenta_instrumento(i) for i in lista
    ])
