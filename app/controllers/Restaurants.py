from system.core.controller import *


class Restaurants(Controller):
    def __init__(self, action):
        super(Restaurants, self).__init__(action)
       
        self.load_model('Restaurant')
        self.db = self._app.db

   
    def index(self):
        
        return self.load_view('landing.html')

 

