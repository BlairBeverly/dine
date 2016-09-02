
from system.core.model import Model

class Restaurant(Model):
    def __init__(self):
        super(Restaurant, self).__init__()

    def get_restaurants(self, page_num, score, favorites, user_id, searchquery):

        if favorites:
            query = "SELECT i.restaurant_id, name, address, city, state, "\
            "postal_code, score, latitude, longitude, True AS favorite, MAX(date) "\
            "AS date FROM restaurants r JOIN inspections i ON (r.id = i.restaurant_id) "\
            "JOIN favorites f ON (f.restaurant_id = r.id) WHERE score <> '' "\
            "AND score >= :score AND f.user_id = :user_id AND latitude <> '' "\
            "AND longitude <> '' GROUP BY 1 LIMIT :exclude_until, 10 "

        elif searchquery:
            query = "SELECT i.restaurant_id, name, address, city, state, "\
            "postal_code, score, latitude, longitude, CASE WHEN f.restaurant_id "\
            "IS NOT NULL THEN True ELSE False END AS favorite, MAX(date) AS date "\
            "FROM restaurants r JOIN inspections i ON (r.id = i.restaurant_id) "\
            "LEFT JOIN (SELECT restaurant_id FROM favorites WHERE user_id = "\
            ":user_id) f ON (f.restaurant_id = r.id) WHERE score <> '' AND "\
            "name LIKE CONCAT('%', :searchquery, '%') AND "\
            "score >= :score AND latitude <> '' AND longitude <> '' GROUP BY 1 "\
            "LIMIT :exclude_until, 10"

        else:
            query = "SELECT i.restaurant_id, name, address, city, state, "\
            "postal_code, score, latitude, longitude, CASE WHEN f.restaurant_id "\
            "IS NOT NULL THEN True ELSE False END AS favorite, MAX(date) AS date "\
            "FROM restaurants r JOIN inspections i ON (r.id = i.restaurant_id) "\
            "LEFT JOIN (SELECT restaurant_id FROM favorites WHERE user_id = "\
            ":user_id) f ON (f.restaurant_id = r.id) WHERE score <> '' AND "\
            "score >= :score AND latitude <> '' AND longitude <> '' GROUP BY 1 "\
            "LIMIT :exclude_until, 10"

        data = {'exclude_until': int(page_num)*10,
                'score': score,
                'user_id': user_id,
                'searchquery': searchquery}

        # print query
        # print data

        return self.db.query_db(query, data)

        #fav_list = [favorite['restaurant_id'] for favorite in self.get_favorites(user_id)]

        # for location in locations:
        #     if location['restaurant_id'] in fav_list:
        #         location['favorite'] = True
        #         print 'yes'

    def add_favorite(self, user_id, restaurant_id):
        query = "INSERT INTO favorites (user_id, restaurant_id, created_at, "\
                "updated_at) VALUES (:user_id, :restaurant_id, NOW(), NOW())"

        data = {'user_id': user_id,
                'restaurant_id': restaurant_id}

        self.db.query_db(query, data)

    def remove_favorite(self, user_id, restaurant_id):
        query = "DELETE FROM favorites WHERE user_id = :user_id AND "\
                "restaurant_id = :restaurant_id"

        data = {'user_id': user_id,
                'restaurant_id': restaurant_id}

        self.db.query_db(query, data)


    def get_favorites(self, user_id):
        query = "SELECT restaurant_id FROM favorites WHERE user_id = :user_id"
        data = {'user_id': user_id}

        return self.db.query_db(query, data)

