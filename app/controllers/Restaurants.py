from system.core.controller import *


class Restaurants(Controller):
    def __init__(self, action):
        super(Restaurants, self).__init__(action)
       
        self.load_model('Restaurant')
        self.db = self._app.db

   
    def index(self):
        locations = self.models['Restaurant'].get_next_ten_restaurants()
        return self.load_view(
            '/restaurants/dashboard.html', 
            locations=locations, 
            nextpage=1)

    def nextTen(self, page_num):
        locations = self.models['Restaurant'].get_next_ten_restaurants(page_num)
        return self.load_view(
            '/restaurants/dashboard.html', 
            locations=locations, 
            nextpage=int(page_num)+1)
