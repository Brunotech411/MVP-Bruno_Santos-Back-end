from schemas.instrumento import InstrumentoOut

def apresenta_instrumento(inst):
    return InstrumentoOut(
        tag=inst.tag,
        lrv=inst.lrv,
        urv=inst.urv,
        span=inst.urv - inst.lrv,
        data_loop=inst.data_loop
    )

def apresenta_instrumentos(lista):
    return {"instrumentos": [apresenta_instrumento(i) for i in lista]}
