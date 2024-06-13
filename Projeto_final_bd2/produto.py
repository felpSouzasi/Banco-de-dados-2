from bson.objectid import ObjectId

class ProdutoModel:
    def __init__(self, database):
        self.db = database

    def create_produto(self, nome: str, descricao: str, preco: float, estoque: int):
        try:
            res = self.db.collection.insert_one({
                "nome": nome,
                "descricao": descricao,
                "preco": preco,
                "estoque": estoque
            })
            print(f"Produto criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o produto: {e}")
            return None

    def read_produto_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Produto encontrado: {res}")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao buscar o produto: {e}")
            return None

    def update_produto(self, id: str, nome: str, descricao: str, preco: float, estoque: int):
        try:
            res = self.db.collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": {"nome": nome, "descricao": descricao, "preco": preco, "estoque": estoque}}
            )
            print(f"Produto atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o produto: {e}")
            return None

    def delete_produto(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Produto deletado: {res.deleted_count} documento(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o produto: {e}")
            return None