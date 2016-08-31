
from system.core.model import Model

class Restaurant(Model):
    def __init__(self):
        super(Restaurant, self).__init__()

    def get_next_ten_restaurants(self, page_num=0):
        query = "SELECT restaurant_id, name, address, city, state, "\
        "postal_code, score, latitude, longitude, MAX(date) as date "\
        "FROM restaurants r JOIN inspections i ON (r.id = i.restaurant_id) "\
        "WHERE score <> '' GROUP BY 1 LIMIT :exclude_until, 10"

        data = {'exclude_until': int(page_num)*10}

        return self.db.query_db(query, data)

