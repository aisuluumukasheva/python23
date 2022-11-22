"========CRUD========"
# Create
# Read
# Update
# Delete

from utils import get_products, generate_id, update_products, get_obj_or_404

def read_products():
    products = get_products()
    for product in products:
        print(f"""
        =============================
        
        id =  {product['id']}
        title = {product['title']}
        price = {product['price']}
        
        =============================
        """)

def create_product():
    products = get_products()
    title = input("Введите название продукта: ")
    price = float(input("Введите цену продукта: "))
    products_ids = map(lambda product:product['id'],products)
    id_ = generate_id(products_ids)
    new_product = {"id":id_, "title":title, "price":price}
    products.append(new_product)
    update_products(products)

def delete_product(id_):
    products = get_products()
    product = get_obj_or_404(id_,products)
    products.remove(product)
    update_products(products)