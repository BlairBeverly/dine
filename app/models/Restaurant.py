
from system.core.model import Model

class Restaurant(Model):
    def __init__(self):
        super(Restaurant, self).__init__()

    def get_next_ten_restaurants(self, exclude=None):
        query = "SELECT * FROM restaurants LIMIT 10"

        return self.db.query_db(query)

