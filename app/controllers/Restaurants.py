from system.core.controller import *


class Restaurants(Controller):
    def __init__(self, action):
        super(Restaurants, self).__init__(action)
       
        self.load_model('Restaurant')
        self.db = self._app.db

   
    def index(self, page_num):
        min_score = session.get('min_score', 0)
        favorites = session.get('only_favorites', False)

        print min_score
        print session['id']

        locations = self.models['Restaurant'].get_restaurants(
            page_num=page_num,
            score=min_score,
            favorites=favorites,
            user_id=session['id'])

        nextpage = int(page_num) + 1

        return self.load_view(
            '/restaurants/dashboard.html', 
            locations=locations, 
            nextpage=nextpage,
            user_id=session['id'])

    def filter(self):
        session['min_score'] = request.form.get('min_score', 0)
        session['only_favorites'] = True if 'favorites' in request.form else False

        return redirect('/restaurants/0')

    def add_favorite(self, user_id, restaurant_id):
        print '=============', user_id, restaurant_id
        self.models['Restaurant'].add_favorite(user_id, restaurant_id)
        return "it worked"

    def remove_favorite(self, user_id, restaurant_id):
        self.models['Restaurant'].remove_favorite(user_id, restaurant_id)
        return "removed favorite"
