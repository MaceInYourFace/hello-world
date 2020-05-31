from objects.cat import Cat
from objects.dog import Dog

class AnimalWelfareCenter:
    def __init__(self, dogs, cats):
        self.dogs = dogs
        self.cats = cats

    def feed_all_animals(self):
        for dog in self.dogs:
            dog.feed(2)

        for cat in self.cats:
            cat.feed(1)

    def excercise_all_animals(self, time):
        for dog in self.dogs:
            dog.go_for_walk(time)

        for cat in self.cats:
            cat.goes_outside(time)

    def add_animal(self, animal):
        if type(animal) == Cat:
            self.cats.append(animal)

        if type(animal) == Dog:
            self.dogs.append(animal)

    def check_for_dead_animals(self):
        for dog in self.dogs:
            dog.check_food_and_liquid_levels()
            if dog.died:
                print(dog)
                self.dogs.remove(dog)
                self.check_for_dead_animals()
                return

        for cat in self.cats:
            cat.check_food_and_liquid_levels()
            if cat.died:
                print(cat)
                self.cats.remove(cat)
                self.check_for_dead_animals()
                return