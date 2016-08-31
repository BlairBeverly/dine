from __future__ import print_function
from system.core.model import Model
import re
import sys
from sqlalchemy.sql import text

class WelcomeModel(Model):
	def __init__(self):
		super(WelcomeModel, self).__init__()
   

    def add_user(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []

        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid')
        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password']) < 6:
            errors.append('Password must be at least 8 characters long')
        if not info['phone']:
            errors.append('Please enter phone number')
        elif len(info['phone']) < 10:
            errors.append('Please enter complete phone number')

        if errors:
            return {"status": False, "errors": errors}
        else:
            sys.stderr.write('Test5\n')

            query = "INSERT INTO users (email, password, phone, created_at, updated_at) VALUES (:email, :password, :phone, NOW(), NOW())"
            self.db.query_db(query, info)

            sys.stderr.write('Test6\n')
            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)
            return { "status": True, "user": users[0] }
            # query = 'SELECT * FROM users WHERE users.email = :email AND users.password = :password'
            # return self.db.query_db(query, user)



    def login_user(self, info):

        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []

        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid')
        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password']) < 6:
            errors.append('Password must be at least 8 characters long')
       
        if errors:
            return {"status": False, "errors": errors}
        else:

            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)
            return { "status": True, "user": users[0] }

        # query ='SELECT * FROM users WHERE users.email = :email AND users.password = :password'
        # return self.db.query_db(query, user)


		# return self.db.query_db(query, user)


 
	   
	def get_users(self, user):
		query = 'SELECT * FROM users WHERE id = id'
		data = {'id' : id}
		return self.db.query_db(query)