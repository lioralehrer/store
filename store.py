from bottle import route, run, template, static_file, get, post, delete, request,put
from sys import argv
import json
import pymysql
connection = pymysql.connect(user='root', password='liora', db='store',
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

@get("/admin")
def admin_portal():
	return template("pages/admin.html")

@get("/")
def index():
    return template("index.html")
@get("/categories")
def get_all_categories():
      with connection.cursor()as cursor:
            query = 'select * from categories'
            cursor.execute(query)
            result = {'CATEGORIES': cursor.fetchall(),'STATUS': 'SUCCESS', 'MSG':'all the categories given','CODE':200 }
            return json.dumps(result)
        
@get("/category/<categoryID>/products")
def get_all_products_of_category(categoryID):
      with connection.cursor()as cursor:
            query = 'select * from products where category_id = %s'
            cursor.execute(query,categoryID)
            result = {'PRODUCTS': cursor.fetchall(),'STATUS': 'SUCCESS', 'MSG': 'all the products from category given','CODE':200 }
            return json.dumps(result)
@post('categories')
def update_category():
      pass            
@put('categories')  
def update_category(category_id, category_to_update):
      pass 
@delete('categories')
def delete_category(category_id):
      pass
@get('/product/<product_id')
def get_product(product_id):
      pass      
@post('/product')
def add_prodact():
      pass
@put('product')  
def update_product(product_id, product_to_update):
      pass 
@delete('product')
def delete_product(product_id):
      pass      
@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')

if __name__ == "__main__":
      run(host='localhost', port=7008 , reloader=True, debug=True)


# import bottle        
# from api.store_api import StoreAPI
# from dal.mysql_db_adapter import MySqlDBAdapter

# if __name__ == "__main__":
#       api = StoreAPI(MySqlDBAdapter())
#       bottle.route("/")(api.index)
#       bottle.route('/images/<filename:re:.*\.(jpg|png|gif|ico)>')(api.images)
#       bottle.route('/css/<filename:re:.*\.css>')(api.stylesheets) 
#       bottle.route('/js/<filename:re:.*\.js>')(api.javascripts)
#       bottle.route('/categories')(api.get_all_categories)
#       bottle.route('/category/<category_id>/products')(api.get_all_products_of_category)
#       bottle.route('/admin')(api.admin_portal)                
#       api.run()

      
