
class Buyer:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def get_rating(self):
        return self.rating
    

    def set_rating(self, x):
        self.rating = x