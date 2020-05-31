class Animal:
    died = False

    def __init__(self, food_level, liquid_level):
        self.food_level = food_level
        self.liquid_level = liquid_level

    def feed(self, amount_of_food):
        self.food_level = self.food_level + amount_of_food

    def water(self, amount_liquid):
        self.liquid_level = self.liquid_level + amount_liquid

    def check_food_and_liquid_levels(self):
        if self.food_level < 0:
            self.died = True

        if self.liquid_level < 0:
            self.died = True
