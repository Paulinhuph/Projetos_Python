# Importa os tipos de colunas e a ferramenta de Chave Estrangeira do SQLAlchemy
from sqlalchemy import Column, String, Integer, ForeignKey
# Importa o recurso que cria a conexão lógica (não física) entre tabelas
from sqlalchemy.orm import relationship
# Importa a classe base que registra seus modelos para o banco de dados
from database import Base

class Estudante(Base):
    __tablename__ = 'estudantes' # Define o nome real da tabela no banco de dados
    
    # Define as colunas da tabela: ID (chave primária), nome e email
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    
    # Relacionamento 1:1 com a classe Perfil
    perfil = relationship(
        "Perfil", 
        back_populates="estudante", # Indica que na classe Perfil existe um atributo chamado 'estudante'
        uselist=False,               # Garante que retorne apenas UM objeto, não uma lista (1:1)
        cascade="all, delete-orphan" # Se o estudante for deletado, o perfil dele também será excluído
    )

class Perfil(Base):
    __tablename__ = 'perfis' # Define o nome da tabela de perfis no banco
    
    id = Column(Integer, primary_key=True, index=True)
    idade = Column(Integer)
    endereco = Column(String)
    
    # Cria a coluna de ligação física: armazena o ID do estudante
    # unique=True reforça que cada estudante só pode ter um único perfil
    estudante_id = Column(Integer, ForeignKey("estudantes.id"), unique=True)
    
    # Relacionamento reverso para permitir acessar perfil.estudante
    estudante = relationship("Estudante", back_populates="perfil")


class Disciplina(Base):
    __tablename__ = 'disciplinas' 
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String)
    matriculas = relationship("Matricula", back_populates="disciplina")

class Matricula(Base):
    __tablename__ = 'matriculas'
    id = Column(Integer, primary_key=True, index=True)
    estudante_id = Column(Integer, ForeignKey('estudantes.id'))
    disciplina_id = Column(Integer, ForeignKey("disciplinas.id"))
    
    estudante = relationship("Estudante", back_populates="matriculas")
    disciplina = relationship("Disciplina", back_populates="matriculas")

class Professor(Base):
    __tablename__='professores'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
