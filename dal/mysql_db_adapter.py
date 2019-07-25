from .base_database_adapter import BaseDatabaseAdapter
import pymysql


class MySqlDBAdapter(BaseDatabaseAdapter):
    def __init__(self):
        self._connection = pymysql.connect(host="localhost",
                                           user="root",
                                           password="liora",
                                           db="store")
    def add_category(self, category):
        try:
            with self._connection.cursor() as cursor:
                sql = f"INSERT INTO categories VALUES('{category.id}','{category.name}')"
                cursor.execute(sql)
                cursor.commit()
        except: Exception
            # print(f"Exception occured when trying to add category {e}")
     
    def add_product(self, product):
        try:
            with self._connection.cursor() as cursor:
                sql = f"INSERT INTO product VALUES('{product.id}','{product.category}','{product.description}','{product.price}','{product.title}','{product.favorite}','{product.img_url}')"
                cursor.execute(sql)
                cursor.commit()
        except: Exception 
            # print(f"Exception occured when trying to add category {e}")        

    def get_category(self, category_id):
        try:
            with self._connection.cursor()as cursor:
                sql = f"select * from categories where id = '{category_id}'"
                cursor.execute(sql)
                return json.dumps(cursor.fetchone())
        except: Exception  
            # print(f"Exception occured when trying to get category {e}")        

    def get_all_categories(self):
        try:
            with self._connection.cursor()as cursor:
                sql = "select * from categories"
                cursor.execute(sql)
                return json.dumps(cursor.fetchall())
        except: Exception  
            # print(f"Exception occured when trying to get categories {e}"        

    def update_category(self, category_id, category_to_update):
        return super().update_category(self,category_id, category_to_update)

    def delete_category(self, category_id):
        return super().delete_category(self,category_id)
