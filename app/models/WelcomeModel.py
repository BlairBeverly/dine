from __future__ import print_function
from system.core.model import Model
import sys

class WelcomeModel(Model):
    def __init__(self):
        super(WelcomeModel, self).__init__()
   
    def add_user(self, user):
        sys.stderr.write('Test5\n')
        query = "INSERT INTO users (email, password, phone, created_at, updated_at) VALUES (:email, :password, :phone, NOW(), NOW())"
        self.db.query_db(query, user)
        sys.stderr.write('Test6\n')
        query = 'SELECT * FROM users WHERE users.email = :email AND users.password = :password'
        return self.db.query_db(query, user)



    def login_user(self, user):

        query ='SELECT * FROM users WHERE users.email = :email AND users.password = :password'
        return self.db.query_db(query, user)


    def get_users(self, user):
        query = 'SELECT * FROM users WHERE id = id'
        data = {'id' : id}
        return self.db.query_db(query)