from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request, Form

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def calculate_cube(x):
    return x ** 3

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/cube/{number}")
def cube_endpoint(number: int):
    return {"result": calculate_cube(number)}

@app.get("/login", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    #Иммитация авторизации, фиктивный логин и пароль
    if username == 'admin' and password == 'root':
        return 'authorized'
    else:
        return 404
