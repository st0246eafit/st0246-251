#from bson.objectid import ObjectId

def get_producto_model(mongo):
    return mongo.db.productos


def listar_productos(mongo):
    productos = mongo.db.productos.find()
    resultado = []
    for p in productos:
        p['_id'] = str(p['_id'])
        resultado.append(p)
    return resultado