from __future__ import print_function
from system.core.controller import *
import sys

class Welcome(Controller):
	def __init__(self, action):
		super(Welcome, self).__init__(action)
	   
		self.load_model('WelcomeModel')
		self.db = self._app.db

   
	def index(self):
		
		return self.load_view('/welcome/landing.html')

	def register(self):
		sys.stderr.write('Test1\n')
		user_info = {
			"email" : request.form['email'],
			"password" : request.form['password'],
			"phone" : request.form['phone']
		}
		
		user_id = self.models['WelcomeModel'].add_user(user_info)
		
		session['id'] = user_id['user']['id']

		# users = self.models['WelcomeModel'].get_users(user_id)
		# sys.stderr.write('Test4\n')
		return self.load_view('/restaurants/dashboard.html')


	def login(self):
		user_info = {
			"email" : request.form['email'],
			"password" : request.form['password']
		}

		user_id = self.models['WelcomeModel'].login_user(user_info)

		# session['id'] = user_id[0]['id']

		# users = self.models['WelcomeModel'].get_users(user_id)

		return self.load_view('/restaurants/dashboard.html')

	

	def logout(self):
		session.clear()
		return self.load_view('/welcome/landing.html')

