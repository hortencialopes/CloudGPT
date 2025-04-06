from fastapi import FastAPI
from fastapi import Body
from core import genAnswer
# Importing the fastapi module - a web framework that simplifies the creation of APIs ensuring the follow of the OpenAPI standards for RESTAPIs - baseado em https://blog.postman.com/how-to-build-an-api-in-python/ 

app = FastAPI()
#starting an instance of the FastApi() class - which will be used to create the API, using the variable app

# @app.get especifica que este endpoint responderá a GET requests de http 
@app.get("/get-message") #route decorator - cria um endpoint p o metodo HTTP GET na url de caminho/path /get-message - que será acessivel em http://host:8000/get-message
async def hello(name: str): #funcao async 
    return {"message": "Hello " + name + ', welcome to CloudBot'} #return dictionary, converted to a JSON response - in a curl os web request, the return will be "Hello World" - "message" is just the id of the dictionary 
    #in this case, the url will be something like http://127.0.0.1:8000/get-message?name=Horts 


@app.post("/ask")
async def pergunta(pergunta: str = Body(...,embed = True)):
    return genAnswer(pergunta)