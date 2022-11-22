import json

def get_db() -> dict:
    with open('db.json') as f:
        db = json.load(f)
    return db

def get_products_by_category(category:str, page=1) -> list:
    db = get_db()
    if category in db:
        if str(page) in db[category]:
            return db[category][str(page)]

def get_total_pages_by_category(category:str) -> int:
    db = get_db()
    if category in db:
        return len(db[category])