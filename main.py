from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
app = FastAPI()


class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType


class Timestamp(BaseModel):
    id: int
    timestamp: int


dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]


@app.get('/')
def root():
    return 'Polyakov Egor'

@app.post('/post')
def Get_post():
    return post_db[0]

@app.get('/dog/{kind}')
def Get_dogs_kind(value: str):
    l = list()
    for i in dogs_db.keys():
        if dogs_db[i].kind == value:
            l.append(dogs_db[i])
    return l


@app.get('/dog_pk/{i_k}')
async def dogs_pk(i_k: int):
    l = list()
    for i in dogs_db.values():
        if i.pk == i_k:
            l.append(i)
    return l

@app.post('/post')
def Get_post():





