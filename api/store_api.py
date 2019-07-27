from bottle import run, get, post, delete, put, request,template, route,static_file
import json


class StoreAPI:
    def __init__(self, db_adapter):
        self._db_adapter = db_adapter

    def run(self):
        run(host="localhost", port="7000" ,debug=True,reloader=True)
        
    # @get("/admin")
    def admin_portal(self):
        return template("pages/admin.html")

    # @get("/")
    def index(self):
        return template("index.html")
    # @get("/categories")
    def get_all_categories(self):
        categories_list = self._db_adapter.get_all_categories()
        result = {'CATEGORIES': categories_list,'STATUS': 'SUCCESS', 'MSG':'all the categories given','CODE':200 }
        return json.dumps(result)

    # @get("/category/<category_id>/products")
    def get_all_products_of_category(self, category_id):
        category = self._db_adapter.get_single_category(category_id)
        return json.dumps(category)

    @post("/categories")
    def create_category(self):
        pass

    @delete("/categories")
    def delete_category(self):
        pass

    @put("/categories")
    def update_category(self):
        pass 

    # @get('/js/<filename:re:.*\.js>')
    def javascripts(self,filename):
        return static_file(filename, root='js')


    # @get('/css/<filename:re:.*\.css>')
    def stylesheets(self,filename):
        return static_file(filename, root='css')


    # @get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
    def images(self,filename):
        return static_file(filename, root='images')   

       