from Database import Database


class MotoristaDAO:
    def __init__(self, database: Database):
        self.db = database

    def create(self, motorista):
        self.db.collection.insert_one(motorista.__dict__)

    def read(self, index):
        return self.db.collection.find_one({"_id": index})

    def update(self, index, motorista):
        self.db.collection.replace_one({"_id": index}, motorista.__dict__)

    def delete(self, index):
        self.db.collection.delete_one({"_id": index})
