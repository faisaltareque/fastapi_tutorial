from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# @app.get('/')
# def index():
#     return {'data':{'name':'Faisal'}}


@app.get('/blog')
def index(limit=10, published:bool=True, sort: Optional[str] = None):
    if published:
        return {'data':f'{limit} published blogs from db'}
    else:
        return {'data':f'{limit} blogs from db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    dicttio = {'data': {'id':id, 'comments':{'1','2'}}}
    return dicttio

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    return {'data':f"Blog is created with title as {request.title}"}


# if __name__ == "__main__":
#     uvicorn.run(app, host='0.0.0.0', port=9000)