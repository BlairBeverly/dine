from __future__ import print_function
from system.core.model import Model
import sys
from sqlalchemy.sql import text

class WelcomeModel(Model):
	def __init__(self):
		super(WelcomeModel, self).__init__()
   
	def add_user(self, user_info):
		pw_hash = self.bcrypt.generate_password_hash(user_info['password'])
		errors = []

		sys.stderr.write('Test5\n')
		query = "INSERT INTO users (email, password, phone, created_at, updated_at) VALUES (:email, :password, :phone, NOW(), NOW())"
		user_data = {'email': user_info['email'],
					 'password': pw_hash,
					  'phone': user_info['phone'] 
					  }
		user = self.db.query_db(query, user_data)

		sys.stderr.write('Test6\n')
		query = 'SELECT * FROM users  WHERE users.email = :email AND users.password = :password'
		users = self.db.query_db(query)
		return { "status": True, "user": users[0] }


	def login_user(self, user_info):
		password = user_info['password']
		errors = []
		query ='SELECT * FROM users WHERE users.email = :email AND users.password = :password'
		user_data = {
				'email': user_info['email'],
				'password': user_info['password']
					}
		user = self.db.get_one(query, user_data)
		if user:
			if self.bcrypt.check_password_hash(user.password, password):
				return {"status": True, "user": user}
		else:
			errors.append('Invalid Login information')
		# Whether we did not find the email, or if the password did not match, either way return False
		return {"status": False, "errors": errors}

		# return self.db.query_db(query, user)


 
	   
	def get_users(self, user):
		query = 'SELECT * FROM users WHERE id = id'
		data = {'id' : id}
		return self.db.query_db(query)