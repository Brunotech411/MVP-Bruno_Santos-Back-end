# Script para criação do banco SQLite e tabela de instrumentos
from database.base import Base, engine
from model.instrumento import Instrumento

# Cria a estrutura de tabelas com base nos modelos definidos
Base.metadata.create_all(engine)

print("✅ Banco de dados e tabela 'instrumentos' criados com sucesso!")
