from fastapi import FastAPI
# pydantic é utilizado como validador de dados, já que a classe criada o herda 
from pydantic import BaseModel

app = FastAPI()

# Rota Raiz
@app.get("/")
def raiz():
    return {"Ola": "Mundo"}

# Criar model
class Usuario(BaseModel):
    id : int
    email: str
    senha: str

# Criar base de dados
base_de_dados = [
    Usuario(id=1, email="limao@limao.com.br", senha="limao123"),
    Usuario(id=2, email="serjao@serjao.com.br", senha="serjao123")
]

# Rota Get All
@app.get("/usuarios")
async def get_todos_os_usuarios():
    return base_de_dados

# Rota Get Id
@app.get("/usuarios/{id_usuario}")
async def get_usuario_usando_id(id_usuario: int):
    for usuario in base_de_dados:
        if(usuario.id == id_usuario):
            return usuario
    
    return {"Status": 404, "Mensagem": "Não encontrou o usuario"}

# Rota Insere
@app.post("/usuarios")
async def insere_usuario(usuario: Usuario):
    #criar regras de negocio
    base_de_dados.append(usuario)
    return usuario