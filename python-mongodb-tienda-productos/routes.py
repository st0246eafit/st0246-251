from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from models import get_producto_model

producto_blueprint = Blueprint('producto', __name__)

@producto_blueprint.route('/', methods=['GET'])
def obtener_productos():
    productos = get_producto_model(producto_blueprint.app.mongo).find()
    resultado = []
    for p in productos:
        p['_id'] = str(p['_id'])
        resultado.append(p)
    return jsonify(resultado)

@producto_blueprint.route('/insertar', methods=['POST'])
def insertar_producto():
    data = request.json
    producto = get_producto_model(producto_blueprint.app.mongo).insert_one(data)
    data['_id'] = str(producto.inserted_id)
    return jsonify(data), 201

@producto_blueprint.route('/actualizar/<id>', methods=['PATCH'])
def actualizar_producto(id):
    data = request.json
    get_producto_model(producto_blueprint.app.mongo).update_one(
        {"_id": ObjectId(id)},
        {"$set": data}
    )
    return jsonify({"mensaje": "Producto actualizado"}), 200

@producto_blueprint.route('/eliminar/<id>', methods=['DELETE'])
def eliminar_producto(id):
    resultado = get_producto_model(producto_blueprint.app.mongo).delete_one({"_id": ObjectId(id)})
    if resultado.deleted_count == 0:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify({"mensaje": "Producto eliminado"}), 200