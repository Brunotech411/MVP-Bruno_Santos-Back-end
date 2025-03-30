# create_db.py
from model.base import Base, engine
from model.instrumento import Instrumento

# Cria as tabelas no banco SQLite
Base.metadata.create_all(engine)

print("✅ Banco de dados e tabela 'instrumentos' criados com sucesso!")
