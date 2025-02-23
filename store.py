from bottle import route, run, template, static_file, get, post, delete, request,put
from sys import argv
import json
import pymysql
import cgi
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
      try:
            with connection.cursor()as cursor:
                  query = 'select * from categories'
                  cursor.execute(query)
                  result = {'CATEGORIES': cursor.fetchall(),'STATUS': 'SUCCESS', 'MSG':'all the categories given','CODE':200 }
                  return json.dumps(result)
      except:
            result = {'STATUS': 'ERROR', 'MSG':"couldn't get the categories",'CODE':404}
            return result                                  
        
@get("/category/<categoryID>/products")
def get_all_products_of_category(categoryID):
      try:
            with connection.cursor()as cursor:
                  query = 'select * from products where category = %s'
                  cursor.execute(query,categoryID)
                  result = {'PRODUCTS': cursor.fetchall(),'STATUS': 'SUCCESS', 'MSG': 'all the products from category given','CODE':200 }
                  return json.dumps(result)
      except Exception as e:
            print (e)
            result = {'STATUS': 'ERROR', 'MSG':"couldn't get the products from categories",'CODE':404}
            return result

@post('/category')
def add_category():
      name = request.forms.get("name")
      print (name)
      try:
            with connection.cursor() as cursor:
                  query = """insert into categories (name) values (%s)"""
                  cursor.execute(query,name)
                  connection.commit()
                  result = {'STATUS': 'SUCCESS', 'MSG': 'new category named: {name} added','CODE':200 }
                  return json.dumps(result)
      except Exception as e:
            print (e)
            result = {'STATUS': 'ERROR', 'MSG':"couldn't add category {name}",'CODE':500}
            return json.dumps(result)           
                  
@put('categories')  
def update_category(category_id, category_to_update):
      name = request.json.get("name")
      category_id = request.json.get("id")
      try:
            with connection.cursor() as cursor:
                  query = "select * from categories where id = %s"
                  cursor.execute(query, category_id)
                  old_name= json.dumps(cursor.fetchone())
                  query = "UPDATE students SET name= %s WHERE id = %s"
                  cursor.execute(query,category_id)
                  result = {'STATUS': 'SUCCESS', 'MSG': 'new producted named: {title} have been changed','CODE':200 }
                  connection.commit()
      except:
            result = {'STATUS': 'ERROR', 'MSG':"couldn't add product {title}",'CODE':500}
            return json.dumps(result)
@delete('categories')
def delete_category(category_id):
      try:
            with connection.cursor() as cursor:
                  query = "delete from categories  where id = %s"
                  cursor.execute(query, (category_id))
                  result = {'STATUS': 'SUCCESS', 'MSG':"delete category with id {category_id} from repository",'CODE':200}
                  return result
      except: 
            result = {'STATUS': 'ERROR', 'MSG':"something went wrong with deleting the category with id {category_id}",'CODE':500}            
@get('/products')
def get_all_products():
      try:
            with connection.cursor()as cursor:
                  query = 'select * from products'
                  cursor.execute(query)
                  result = {'PRODUCTS': cursor.fetchall(),'STATUS': 'SUCCESS', 'MSG':'get all the products','CODE':200}
                  return json.dumps(result)
      except Exception as e:
            print (e)
            result = {'STATUS': 'ERROR', 'MSG':"couldn't get the products ",'CODE':404}
            return result

@get('/products/<product_id')
def get_product(product_id):
      try:
            with connection.cursor()as cursor:
                  query = 'select * from products where id = %s'
                  cursor.execute(query,(product_id))
                  result = {'PRODUCTS': cursor.fetchone(),'STATUS': 'SUCCESS', 'MSG':'get the product with id: {product_id}','CODE':200 }
                  return json.dumps(result)
      except Exception as e:
            print (e)
            result = {'STATUS': 'ERROR', 'MSG':"couldn't get the product with id : {product_id}",'CODE':404}
            return result
            
@post('/product')
def add_prodact():
      category = request.forms.get("category")
      description = request.forms.get("desc")
      price = request.forms.get("price")
      title = request.forms.get("title")
      img_url = request.forms.get("img_url")
      favorite = request.forms.get("favorite")
      if favorite == 'on':
            favorite = 1
      else:
            favorite = 0      
      try:
            with connection.cursor() as cursor:
                  query = """insert into products (category, description,price,title,favorite,img_url)values (%s,%s,%s,%s,%s,%s)"""
                  insert = (category ,description, price,title,favorite,"../images/"+img_url)
                  cursor.execute(query, insert)
                  result = {'STATUS': 'SUCCESS', 'MSG': 'new producted named: {title} added','CODE':200 }
                  connection.commit()
                  return json.dumps(result)
      except Exception as e:
            print (e)
            result = {'STATUS': 'ERROR', 'MSG':"couldn't add product {title}",'CODE':405}
            return json.dumps(result) 
@put('product')  
def update_product():
      product_id = request.json.get("id")
      category = request.json.get("category")
      description = request.json.get("description")
      price = request.json.get("price")
      title = request.json.get("title")
      favorite = request.json.get("favorite")
      img_url = request.json.get("img_url")
      try:
        with connection.cursor() as cursor:
            query = "select * from products where id= %s"
            cursor.execute(query, product_id)
            old_name= json.dumps(cursor.fetchone())
            query = "UPDATE products SET category= %s,description=%s,price=%s,title=%s,favorite = %s,img_url = %s WHERE studentId = %s"
            insert = (category ,description, price,title,favorite,img_url)
            cursor.execute(query,insert)
            result = {'STATUS': 'SUCCESS', 'MSG': 'new producted named: {title} have been changed','CODE':200 }
            connection.commit()
      except:
            result = {'STATUS': 'ERROR', 'MSG':"couldn't add product {title}",'CODE':500}
            return json.dumps(result)   
@delete('products')
def delete_product(product_id):
      try:
            with connection.cursor() as cursor:
                  query = "delete from products  where id = %s"
                  cursor.execute(query, (product_id))
                  result = {'STATUS': 'SUCCESS', 'MSG':"delete product with id {product_id} from repository",'CODE':200}
                  return result
      except: 
            result = {'STATUS': 'ERROR', 'MSG':"something went wrong with deleting the product with id {product_id}",'CODE':500}      
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

      
