from system.core.controller import *


class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
       
        self.load_model('WelcomeModel')
        self.db = self._app.db

   
    def index(self):
        
        return self.load_view('landing.html')

    def register(self):
        user_info = {
            "email" : request.form['email'],
            "password" : request.form['password'],
            "phone" : request.form['phone']
        }

        user_id = self.models['WelcomeModel'].add_user(user_info)

        session['id'] = user_id[0]['id']
        session['email'] = user_id[0]['email']
        session['phone'] = user_id[0]['phone']

        users = self.models['WelcomeModel'].get_users(user_id)

        return self.load_view('dashboard.html', users=users)


    def login(self):
        user_info = {
            "email" : request.form['email'],
            "password" : request.form['password']
        }

        user_id = self.models['WelcomeModel'].login_user(user_info)

        session['id'] = user_id[0]['id']
        session['email'] = user_id[0]['email']

        users = self.models['WelcomeModel'].get_users(user_id)

        return self.load_view('dashboard.html', users=users)



    def logout(self):
        session.clear()
        return self.load_view('landing.html')

