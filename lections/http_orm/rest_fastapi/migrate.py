from settings import Base,engine
from app.models import Product

# создаем таблицы в бд


print("CREATING TABLE product")
Base.metadata.create_all(bind=engine)
print("DONE")