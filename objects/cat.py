from objects.animal import Animal


class Cat(Animal):
    def goes_outside(self, time):
        self.food_level = self.food_level - time
        self.liquid_level = self.liquid_level - time

        self.check_food_and_liquid_levels()
