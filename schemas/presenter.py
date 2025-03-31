def apresenta_instrumento(inst):
    """Retorna os dados de um instrumento como dicionário"""
    return {
        "tag": inst.tag,
        "lrv": inst.lrv,
        "urv": inst.urv,
        "span": inst.urv - inst.lrv,
        "data_loop": inst.data_loop
    }

def apresenta_instrumentos(lista):
    """Retorna a lista de instrumentos como dicionário"""
    return {
        "instrumentos": [apresenta_instrumento(i) for i in lista]
    }
