from bottle import route, run, template, static_file, get, post, delete, request
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
            return json.dumps(cursor.fetchall())
@get("/category/<categoryID>/products")
def get_all_products_of_category(categoryID):
       with connection.cursor()as cursor:
            query = f'select * from products where category_id = "{categoryID}"'
            cursor.execute(query)
            return json.dumps(cursor.fetchall())


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
        
# from api.store_api import StoreAPI
# from dal.mysql_db_adapter import MySqlDBAdapter

# if __name__ == "__main__":
#       run(host='localhost', port=7008 , reloader=True, debug=True)  
#       api = StoreAPI(MySqlDBAdapter())
#     api.run()
