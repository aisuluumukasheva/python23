"---Файл с дополнительными функциями---"
import json

def generate_id(ids:list) -> int:
    """
    Принимает список из существующих id, 
    Возвращает новый id
    """

    import random
    new_id = random.randint(100,1000)
    print(new_id)

# generate_id([])
# generate_id([])
    while new_id in ids:
        new_id = random.randint(100,1000)
    return new_id

def validate_passwords(p1:str,p2:str):
    """
    Принимает 2 пароля, если пароли не совпадают - вызывается ошибка
    """
    if p1 != p2:
        raise Exception ("Пароли не совпадают")

def get_users() -> list:
    """
    Возвращает список с юзерами из базы данных
    """
    with open('db.json') as file:
        db = json.load(file)
    return db["users"]

def get_products() -> list:
    """
    Возвращает список с продуктами из бд
    """
    with open('db.json') as file:
        db = json.load(file)
    return db["products"]

def update_users(users:list):
    """
    Принимает список с юзерами и обновляет бд
    """
    with open('db.json') as file:
        db = json.load(file)
    db['users'] = users

    with open('db.json','w') as file:
        json.dump(db,file)

def update_products(products:list):
    """
    Принимает список с  продуктами и обновляет бд
    """
    with open('db.json') as file:
        db = json.load(file)
    db['products'] = products

    with open('db.json','w') as file:
        json.dump(db,file)

def get_obj_or_404(id_:int,objects:list) -> dict:
    for obj in objects:
        print(obj)
        if obj['id'] == id_:
            return obj
    raise Exception('404: Not found')