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
        sys.stderr.write('Test2\n')
        user_id = self.models['WelcomeModel'].add_user(user_info)
        sys.stderr.write('Test3\n')
        session['id'] = user_id[0]['id']

        sys.stderr.write('Test4\n')
        return redirect('/restaurants/0') 


    def login(self):
        user_info = {
            "email" : request.form['email'],
            "password" : request.form['password']
        }

        user_id = self.models['WelcomeModel'].login_user(user_info)

        session['id'] = user_id[0]['id']
        session['email'] = user_id[0]['email']

        return redirect('/restaurants/0') 


    def logout(self):
        session.clear()
        return self.load_view('/welcome/landing.html')

