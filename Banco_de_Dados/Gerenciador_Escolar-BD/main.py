# Importa o tipo List para definir que algo retornará uma lista de itens
from typing import List 

# Importa as ferramentas essenciais do FastAPI (a estrutura da API e as Dependências)
from fastapi import FastAPI, Depends, HTTPException 

# Importa o Session para tipar o banco e o joinedload para carregar tabelas relacionadas de uma vez
from sqlalchemy.orm import Session, joinedload 

# Importa seus modelos (banco de dados) e schemas (validação de dados)
import models, schemas 

# Importa a conexão com o banco e a fábrica de sessões do seu arquivo database.py
from database import engine, SessionLocal 

# Cria automaticamente todas as tabelas no banco de dados com base nos seus modelos
models.Base.metadata.create_all(bind=engine) 

# Inicializa a aplicação FastAPI
app = FastAPI() 

# Função "Dependency Injection" que cria uma sessão de banco de dados por requisição
def get_db():
    db = SessionLocal() # Abre a conexão
    try:
        yield db # Entrega a conexão para a rota que a solicitou
    finally:
        db.close() # Garante que a conexão seja fechada após o uso, mesmo se houver erro

# Rota POST para criar um estudante, usando o schema Estudante para o formato da resposta
@app.post('/estudantes/', response_model=schemas.Estudante) 
def criar_estudante(
    estudante: schemas.EstudanteCreate, # Dados que chegam no corpo da requisição (JSON)
    db: Session = Depends(get_db)       # Injeta a sessão do banco de dados aqui
): 
    # Transforma os dados do perfil (que vieram no JSON) em um objeto do modelo SQLAlchemy
    db_perfil = models.Perfil(**estudante.perfil.model_dump()) 

    # Cria o objeto Estudante associando-o ao objeto perfil criado acima (relação 1:1)
    db_estudante = models.Estudante(
        nome=estudante.nome, 
        perfil=db_perfil 
    ) 

    db.add(db_estudante) # Prepara o objeto para ser inserido no banco
    db.commit()          # Salva as alterações definitivamente no banco
    db.refresh(db_estudante) # Atualiza o objeto local com o ID gerado pelo banco
    return db_estudante # Retorna o estudante criado (o FastAPI converterá para JSON)

# Rota GET para listar estudantes, indicando que retornará uma lista (List) de estudantes
@app.get('/estudantes/', response_model=List[schemas.Estudante]) 
def listar_estudantes(db: Session = Depends(get_db)): 
    # Busca todos os estudantes e usa joinedload para trazer o Perfil junto num único comando SQL
    estudantes = db.query(models.Estudante).options(
        joinedload(models.Estudante.perfil) 
    ).all() 
    
    return estudantes # Retorna a lista completa para o cliente

@app.post('/disciplinas/', response_model=schemas.Disciplina)
def criar_disciplina(
    disciplina: schemas.DisciplinaCreate,
    db: Session = Depends(get_db)
):  
    db_perfil = models.Perfil(**disciplina.perfil.model_dump()) 
    

    db_disciplina = models.Disciplina(
        nome=disciplina.nome,
        descricao=disciplina.descricao,
        perfil=db_perfil
    )
    db.add(db_disciplina)
    db.commit()
    db.refresh(db_disciplina)
    return db_disciplina

@app.post('/disciplinas/', response_model=schemas.Disciplina)
def criar_disciplina(disciplina: schemas.DisciplinaCreate, db: Session = Depends(get_db)):  
    db_disciplina = models.Disciplina(**disciplina.model_dump()) # Use model_dump() no Pydantic V2
    db.add(db_disciplina)
    db.commit()
    db.refresh(db_disciplina)
    return db_disciplina

@app.post('/matriculas/', response_model=schemas.Matricula)
def criar_matricula(matricula: schemas.MatriculaCreate, db: Session = Depends(get_db)):
    db_matricula = models.Matricula(**matricula.model_dump())
    db.add(db_matricula)
    db.commit()
    db.refresh(db_matricula)
    return db_matricula

@app.get('/matriculas/', response_model=List[schemas.Matricula])
def listar_matriculas(db: Session = Depends(get_db)):
    return db.query(models.Matricula).all()


@app.post('/professores/', response_model=schemas.Professor)
def criar_professor(
        professor: schemas.ProfessorCreate,
        db: Session = Depends(get_db)
    ):
    db_professor = models.Professor(**professor.dict())
    db.add(db_professor)
    db.commit()
    db.refresh(db_professor)
    return db_professor

@app.get('/professores/', response_model=List[schemas.Professor])
def listar_professores(db: Session = Depends(get_db)):
    return db.query(models.Professor).all()
