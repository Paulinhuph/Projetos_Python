# Importa tipos para definir listas ou campos que podem ser nulos (opcionais)
from typing import List, Optional

# Importa a base para criar modelos de dados e a configuração do Pydantic V2
from pydantic import BaseModel, ConfigDict

# 1. Defina os schemas de Perfil primeiro (necessário porque Estudante depende dele)

# Schema para os dados que o usuário envia ao criar um perfil (Input)
class PerfilCreate(BaseModel):
    idade: int
    endereco: str

# Schema que representa o Perfil como ele sai do banco de dados (Output)
class Perfil(PerfilCreate):
    id: int # O ID só existe após a criação no banco
    
    # Permite que o Pydantic leia dados vindos de objetos do SQLAlchemy (ORMs)
    model_config = ConfigDict(from_attributes=True) 

# 2. Depois defina os schemas de Estudante

# Schema para os dados que o usuário envia ao cadastrar um estudante
class EstudanteCreate(BaseModel):
    nome: str
    email: str
    perfil: PerfilCreate # Define que, ao criar um estudante, os dados do perfil devem vir juntos

# Schema que representa o Estudante completo ao ser consultado (Output)
class Estudante(BaseModel):
    id: int
    nome: str
    email: str 
    # O perfil é opcional e, se existir, segue o formato do schema Perfil (com ID)
    perfil: Optional[Perfil] = None

    # Garante que o Pydantic consiga converter o objeto Estudante do banco para JSON
    model_config = ConfigDict(from_attributes=True)

class DisciplinaCreate(BaseModel):
    nome: str
    descricao: str

class Disciplina(DisciplinaCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)

class MatriculaCreate(BaseModel):
    estudante_id: int
    disciplina_id: int

class Matricula(MatriculaCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)

class ProfessorCreate(BaseModel):
    nome: str

class Professor(ProfessorCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)