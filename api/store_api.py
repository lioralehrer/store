from bottle import run, get, post, delete, put, request
import json


class StoreAPI:
    def __init__(self, db_adapter):
        self._db_adapter = db_adapter

    def run(self):
        run(host="localhost", port="7000" ,debug=True,reloader=True)

    @get("/categories")
    def get_all_categories(self):
        categories_list = self._db_adapter.get_all_categorie()
        return json.dumps(categories_list)

    @get("/categoriss/<category_id>")
    def get_single_category(self, category_id):
        pass

    @post("/categories")
    def create_category(self):
        pass

    @delete("/categories")
    def delete_category(self):
        pass

    @put("/categories")
    def update_category(self):
        pass 