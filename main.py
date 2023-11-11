from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone

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
# Реализован путь /
@app.get('/')
def root():
    return 'Polyakov Egor'

# Реализовано получение списка собак
# Реализовано получение собак по типу
@app.get('/dog/{type}')
def Get_dogs_kind(type: str):
    l = list()
    if type not in [dog.kind for dog in dogs_db.values()]:
        l.append(dogs_db)
    else:
        for i in dogs_db.keys():
            if dogs_db[i].kind == type:
                l.append(dogs_db[i])
    return l

# Реализовано получение собак по id
@app.get('/dog_pk/{i_d}')
async def dogs_pk(i_d: int):
    l = list()
    for i in dogs_db.values():
        if i.pk == i_d:
            l.append(i)
    return l


# Реализован путь /post
@app.post('/post', response_model= Timestamp)
def Get_post():
    tec_id = post_db[-1].id + 1
    delta = timedelta(hours=3)
    date_cur = datetime.now(timezone.utc) + delta
    int_date = int(date_cur.timestamp())
    l = Timestamp(id = tec_id, timestamp = int_date)
    return l


# Реализована запись собак
@app.post('/dog', response_model=Dog)
def create_dog(dog :Dog):
    if dogs_db.get(dog.pk) == True:
        return 'pk is already exists'
    else:
        new_dog = dog
        dogs_db[dog.pk]= new_dog
        print("Собака успешно добавлена")
    return new_dog

# Реализовано обновление собаки по id
@app.patch('/dog/{pk}')
async def update_info_dog(pk: int, dog: Dog):
    if pk in dogs_db:
        dogs_db[pk] = dog
        return dogs_db[pk]
    else:
        return 'update is failed'






