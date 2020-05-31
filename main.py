from animal_welfare_center import AnimalWelfareCenter
from objects.cat import Cat
from objects.dog import Dog


class Main:
    def __init__(self):
        self.animal_welfare_center = AnimalWelfareCenter([], [])

    def run(self):
        cats = [Cat(1, 3), Cat(2, 3), Cat(3, 3), Cat(5, 5), Cat(2, 1), Cat(6, 2), Cat(7, 4)]
        dogs = [Dog(1, 3), Dog(2, 3), Dog(3, 3), Dog(5, 5), Dog(2, 1), Dog(5, 2), Dog(3, 4)]

        for dog in dogs:
            self.animal_welfare_center.add_animal(dog)

        for cat in cats:
            self.animal_welfare_center.add_animal(cat)
            
        self.animal_welfare_center.feed_all_animals(4)
        self.animal_welfare_center.hydrate_all_animals(4)


        self.animal_welfare_center.excercise_all_animals(8)
        self.animal_welfare_center.check_for_dead_animals()
        self.output_food_levels()
        self.output_liquid_levels()

    def output_food_levels(self):
        print("Cats food levels:")
        cat_number = 1
        for cat in self.animal_welfare_center.cats:
            print("Ref " + str(cat_number) + ": " + str(cat.food_level))
            cat_number = cat_number + 1

        dog_number = 1
        print("Dogs food levels:")
        for dog in self.animal_welfare_center.dogs:
            print("Ref " + str(dog_number) + ": " + str(dog.food_level))
            dog_number = dog_number + 1

    def output_liquid_levels(self):
        print("Cats liquid levels:")
        cat_number = 1
        for cat in self.animal_welfare_center.cats:
            print("Ref " + str(cat_number) + ": " + str(cat.liquid_level))
            cat_number = cat_number + 1

        dog_number = 1
        print("Dogs liquid levels:")
        for dog in self.animal_welfare_center.dogs:
            print("Ref " + str(dog_number) + ": " + str(dog.liquid_level))
            dog_number = dog_number + 1

    def output_counts(self):
        print("Number of cats: " + str(len(self.animal_welfare_center.cats)))
        print("Number of dogs: " + str(len(self.animal_welfare_center.dogs)))
