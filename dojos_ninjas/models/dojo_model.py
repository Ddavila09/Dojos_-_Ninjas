from dojos_ninjas.config.mysqlconnection import connectToMySQL
from dojos_ninjas import DATABASE
from dojos_ninjas.models.ninjas_model import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # def __repr__(self):
    #     return f"Dojo: {self.first_name}"    
    
    @classmethod
    def create(self, data):
        
        query = """
        
            INSERT INTO dojos
            (name)
            VALUES (%(name)s)
        
        """
        
        
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        
        query = "SELECT * FROM dojos"
        
        results = connectToMySQL(DATABASE).query_db(query)
        
        dojos = []
        
        if results:
            for r in results:
                dojos.append(cls(r))
                
        return dojos
    
    @classmethod
    def get_one_with_ninjas(cls,id):
        data = {
            "id": id,
        }
        
        query="""
        
        SELECT * FROM dojos
        LEFT JOIN ninjas ON 
        dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(id)s;
        
        """

        results = connectToMySQL(DATABASE).query_db(query,data)
        
        ninjas = []
        
        dojo = cls(results[0])
        if results:
            for row in results:
                
                ninja_data = {
                    "id" : row['ninjas.id'],
                    "first_name" : row['first_name'],
                    "last_name" : row['last_name'],
                    "age" : row['age'],
                    "created_at" : row['created_at'],
                    "updated_at" : row['updated_at'],
                    "dojo_id" : row['dojo_id'],
                }

                ninja =  Ninja(ninja_data)
                
                # dojo.ninja = ninja
                
                ninjas.append(ninja)
                
            dojo.ninjas = ninjas  
              
        return dojo
    
    @classmethod
    def get_one(cls, id):

        data = {
            "id": id,
        }

        query = """
     
            SELECT * FROM dojos
            WHERE id = %(id)s;
     
     
         """
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo = cls(results[0])

        return dojo
