from objects.animal import Animal

class Dog(Animal):
    def go_for_walk(self, time):
        self.food_level = self.food_level - (time * 2)
        self.liquid_level = self.liquid_level - (time * 2)
        self.check_food_and_liquid_levels()