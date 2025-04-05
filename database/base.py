from sqlalchemy.ext.declarative import declarative_base  # Base para os modelos ORM
from sqlalchemy.orm import sessionmaker  # Criação de sessões de banco
from sqlalchemy import create_engine  # Criação do motor de conexão com o banco

# Cria o motor de conexão com um banco SQLite local
engine = create_engine('sqlite:///instrumentos.db')

# Cria um gerenciador de sessões vinculado ao engine
Session = sessionmaker(bind=engine)

# Cria uma classe base para os modelos ORM herdarem
Base = declarative_base()
