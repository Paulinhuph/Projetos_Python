# Importa a função que cria a conexão com o motor do banco de dados
from sqlalchemy import create_engine
# Importa a função para criar a classe base que todos os modelos herdarão
from sqlalchemy.ext.declarative import declarative_base
# Importa a ferramenta que configura a fábrica de sessões (transações)
from sqlalchemy.orm import sessionmaker

# Endereço de conexão: driver://usuário:senha@servidor:porta/nome_do_banco
DATABASE_URL = 'postgresql://'':''/db_escola'

# O motor (engine) que gerencia o fluxo de dados e a comunicação com o PostgreSQL
engine = create_engine(DATABASE_URL)

# Cria uma "fábrica" de sessões. Cada vez que chamarmos SessionLocal(), 
# uma nova conversa com o banco é iniciada usando o engine configurado
SessionLocal = sessionmaker(bind=engine)

# Classe base usada pelos modelos (Estudante, Perfil) para que o SQLAlchemy 
# saiba quais classes representam tabelas no banco de dados
Base = declarative_base()