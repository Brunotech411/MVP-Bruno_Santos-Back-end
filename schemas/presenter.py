def apresenta_instrumento(inst):
    # Apresenta um único instrumento como dicionário JSON
    return {
        "tag": inst.tag,
        "lrv": inst.lrv,
        "urv": inst.urv,
        "span": inst.urv - inst.lrv,
        "data_loop": inst.data_loop
    }

# Apresenta uma lista de instrumentos
def apresenta_instrumentos(lista):
    return {
        "instrumentos": [apresenta_instrumento(i) for i in lista]
    }
