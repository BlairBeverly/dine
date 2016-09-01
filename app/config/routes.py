
from system.core.router import routes


routes['default_controller'] = 'Welcome'
routes['POST']['/register'] = 'Welcome#register'
routes['POST']['/login'] = 'Welcome#login'
routes['POST']['/logout'] = 'Welcome#logout'
routes['GET']['/restaurants/<page_num>'] = 'Restaurants#index'
routes['POST']['/restaurants/filter'] = 'Restaurants#filter'
routes['POST']['/restaurants/add_favorite/<user_id>/<restaurant_id>'] = 'Restaurants#add_favorite'
routes['POST']['/restaurants/remove_favorite/<user_id>/<restaurant_id>'] = 'Restaurants#remove_favorite'

