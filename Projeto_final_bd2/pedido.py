from bson.objectid import ObjectId

#Modelo para operações CRUD de pedidos
class PedidoModel:
    def __init__(self, database):
        self.db = database

    def create_pedido(self, cliente_id: int, data_compra: str, produtos: list):
        try:
            res = self.db.collection.insert_one({
                "cliente_id": cliente_id,
                "data_compra": data_compra,
                "produtos": produtos
            })
            print(f"Pedido criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o pedido: {e}")
            return None

    def read_pedido_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Pedido encontrado: {res}")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao buscar o pedido: {e}")
            return None

    def update_pedido(self, id: str, cliente_id: int, data_compra: str, produtos: list):
        try:
            res = self.db.collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": {"cliente_id": cliente_id, "data_compra": data_compra, "produtos": produtos}}
            )
            print(f"Pedido atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o pedido: {e}")
            return None

    def delete_pedido(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Pedido deletado: {res.deleted_count} documento(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o pedido: {e}")
            return None
