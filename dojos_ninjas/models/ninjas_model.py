from dojos_ninjas.config.mysqlconnection import connectToMySQL
from dojos_ninjas import DATABASE


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    def __repr__(self):
        return f"Ninja: {self.first_name}"

    @classmethod
    def get_all(cls):

        query = "SELECT * FROM ninjas"

        results = connectToMySQL(DATABASE).query_db(query)

        ninjas = []

        if results:
            for dict in results:
                new_user = cls(dict)
                ninjas.append(new_user)

        return ninjas

    @classmethod
    def get_one(cls, id):

        data = {
            "id": id,
        }

        query = """
     
            SELECT * FROM ninjas
            WHERE id = %(id)s;
     
     
         """
        results = connectToMySQL(DATABASE).query_db(query, data)
        person = cls(results[0])

        return person

    @classmethod
    def save(cls, data):
     
        query = """
        
        UPDATE ninjas
        SET
        first_name = %(first_name)s,
        last_name = %(last_name)s,
        age = %(age)s
        WHERE
        id = %(id)s;
        
        """

        connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def create(cls, data):
        print('hello')
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age) VALUES(%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s)"

        return connectToMySQL(DATABASE).query_db(query, data)
    
    
    
    @classmethod
    def delete(cls, id):
        
        data = {
            "id": id,
        }
    
        query = """
        
        DELETE FROM ninjas
        WHERE id = %(id)s;
        
        """
        connectToMySQL(DATABASE).query_db(query, data)