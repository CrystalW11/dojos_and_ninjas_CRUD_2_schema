from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
from pprint import pprint


class Dojo:
    DB = "dojos_and_ninjas_schema2"

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    # this gets all the dojos on the dojos table
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        pprint(query)
        results = connectToMySQL(cls.DB).query_db(query)
        pprint(results)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"

        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        pprint(results)
        dojo = cls(results[0])
        for i in results:
            if i["ninjas.id"] is not None:

                row = {
                    "id": i["ninjas.id"],
                    "first_name": i["first_name"],
                    "last_name": i["last_name"],
                    "age": i["age"],
                    "created_at": i["ninjas.created_at"],
                    "updated_at": i["ninjas.updated_at"],
                }
                dojo.ninjas.append(Ninja(row))
        return dojo


