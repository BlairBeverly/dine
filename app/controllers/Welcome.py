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

        if user_id['status'] == True:
            session['id'] = user_id['user']['id']
            return redirect('/restaurants/0') 

        else:
            for message in user_id['errors']:
                flash(message, 'regis_errors')
            return redirect('/')

	def login(self):
		user_info = {
			"email" : request.form['email'],
			"password" : request.form['password']
		}

		
        user_id = self.models['WelcomeModel'].login_user(user_info)
 
        if user_id['status'] == True:
            session['id'] = user_id['user']['id']
            return redirect('/restaurants/0') 
        
        else:
            for message in user_id['errors']:
                flash(message, 'regis_errors')
            return redirect('/')



	def logout(self):
		session.clear()
		return self.load_view('/welcome/landing.html')

