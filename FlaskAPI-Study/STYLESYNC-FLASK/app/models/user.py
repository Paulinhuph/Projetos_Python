from pydantic import BaseModel, Field, EmailStr

# -------------------------------------------------------------------------
# Modelo para o Payload de Login 
# -------------------------------------------------------------------------
class LoginPayload(BaseModel):
    username: str
    password: str


# -------------------------------------------------------------------------
# Modelo para a Criação de Usuário (POST /usuarios)
# -------------------------------------------------------------------------
class UserCreate(BaseModel):
    username: str
    email: EmailStr  # Valida automaticamente se o formato é um e-mail real
    password: str    # Recebe a senha em texto simples conforme o desafio


# -------------------------------------------------------------------------
# Modelo para a Resposta de Usuário (GET /usuarios) - Sem a Senha!
# -------------------------------------------------------------------------
class UserResponse(BaseModel):
    # O Field mapeia o '_id' do MongoDB para a propriedade 'id' do Python.
    # O 'by_alias=True' na rota garante que o JSON final exiba '_id'.
    id: str = Field(..., alias='_id')
    username: str
    email: EmailStr

    # Esta configuração interna é fundamental para o Pydantic v2.
    # Ela permite que o modelo leia dados mesmo se o ID vier como string do banco.
    model_config = {
        "populate_by_name": True
    }