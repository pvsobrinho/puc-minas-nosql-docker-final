from db_connection import get_database
from pymongo.collection import Collection

db = get_database()
##Paulo Victor
def create_branch(branch_name):
    db.create_collection(branch_name)

def add_product(branch_name, sku, name, price, stock):
    product = {
        "sku": sku,
        "name": name,
        "price": price,
        "stock": stock
    }
    collection: Collection = db[branch_name]
    collection.insert_one(product)

def query_product(branch_name, sku):
    collection: Collection = db[branch_name]
    return collection.find_one({"sku": sku})

def update_stock(branch_name, sku, new_stock):
    collection: Collection = db[branch_name]
    collection.update_one({"sku": sku}, {"$set": {"stock": new_stock}})

# carga de dados  - exemplo - para uma operação para uma quantidade de produtos em larga escala
# as chaamdas via aplicação seriam desta forma em um ambiente onde pode executar uma grande quantidade de chamadas simultaneas
# não havera gargalos de desempenho por conta dos shareds do mongo db

create_branch("Filial_1")
add_product("Filial_1", "1234", "Teclado Mecânico", 150.00, 30)
print(query_product("Filial_1", "1234"))
update_stock("Filial_1", "1234", 25)
