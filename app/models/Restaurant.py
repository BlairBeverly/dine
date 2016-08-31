
from system.core.model import Model

class Restaurant(Model):
    def __init__(self):
        super(Restaurant, self).__init__()

    def get_restaurants(self, page_num, score, favorites, user_id):
   
        query = "SELECT restaurant_id, name, address, city, state, "\
        "postal_code, score, latitude, longitude, MAX(date) as date "\
        "FROM restaurants r JOIN inspections i ON (r.id = i.restaurant_id) "\
        "WHERE score <> '' AND score >= :score GROUP BY 1 "\
        "LIMIT :exclude_until, 10 "

        data = {'exclude_until': int(page_num)*10,
                'score': score}

        return self.db.query_db(query, data)

    def get_fav_restaurants(self, user_id):
        query = "SELECT restaurant_id FROM favorites WHERE user_id = :user_id"

        data = {'user_id': user_id}

        return self.db.query_db(query, data)

