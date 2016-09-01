
from system.core.model import Model

class Restaurant(Model):
    def __init__(self):
        super(Restaurant, self).__init__()

    def get_restaurants(self, page_num, score, favorites, user_id):

        if favorites:
            query = "SELECT i.restaurant_id, name, address, city, state, "\
            "postal_code, score, latitude, longitude, MAX(date) as date "\
            "FROM restaurants r JOIN inspections i ON (r.id = i.restaurant_id) "\
            "JOIN favorites f ON (f.restaurant_id = r.id) WHERE score <> '' "\
            "AND score >= :score AND f.user_id = :user_id AND latitude <> '' "\
            "AND longitude <> '' GROUP BY 1 ORDER BY score DESC "\
            "LIMIT :exclude_until, 10 "

        else:
            query = "SELECT restaurant_id, name, address, city, state, "\
            "postal_code, score, latitude, longitude, MAX(date) as date "\
            "FROM restaurants r JOIN inspections i ON (r.id = i.restaurant_id) "\
            "WHERE score <> '' AND score >= :score AND latitude <> '' AND "\
            "longitude <> '' GROUP BY 1 ORDER BY score DESC "\
            "LIMIT :exclude_until, 10 "

        data = {'exclude_until': int(page_num)*10,
                'score': score,
                'user_id': user_id}

        return self.db.query_db(query, data)

    def get_restaurant_count(self):
        pass


