from abc import ABC, abstractmethod

class BaseDatabaseAdapter(ABC):
    # Create
    # @abstractmethod
    def add_product(self, product):
        pass
    # @abstractmethod
    def add_category(self, product):
        pass    
    
    # Read
    # @abstractmethod
    def get_product(self, product_id):
        pass

    # @abstractmethod
    def get_all_productss(self):
        pass
    # @abstractmethod
    def get_all_productss(self, category_id):
        pass    
    # @abstractmethod
    def get_category(self, category_id):
        pass

    # @abstractmethod
    def get_all_categories(self):
        pass    

    # Update
    # @abstractmethod
    def update_product(self, product_id, product_to_update):
        pass
    # @abstractmethod
    def update_category(self, category_id, category_to_update):
        pass    

    # Delete
    # @abstractmethod
    def delete_product(self, product_id):
        pass
    # @abstractmethod
    def delete_category(self, category_id):
        pass    