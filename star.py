from random import randint
from planet import *


class Star:
    def __init__(self, x, y, z, chance_of_life=None, range_of_planets=None, goldilocs_zone=None, recharge=None):
        self.x = x
        self.y = y
        self.z = z

        self.chance_of_life = chance_of_life
        self.range_of_planets = range_of_planets
        self.goldilocs_zone = goldilocs_zone
        self.recharge = recharge

        self.isVisited = False

        self.rocky_counter = 0
        self.gaseous_counter = 0
        self.habitable_counter = 0

        self.planet_list = []

        self.generate_planet()

    @staticmethod
    def create_coordinate_log(x, y, z):
        all_coordinates = []
        coordinates = [x, y, z]

        if coordinates not in all_coordinates:
            all_coordinates.append(coordinates)
            return True
        else:
            return False

    def generate_planet(self):
        for i in range(self.range_of_planets):
            planet_range = randint(0, 2)

            if planet_range == 0:
                new_planet = RockyPlanet()
                new_planet.id_generator(new_planet)
                self.planet_list.append(new_planet)
                self.rocky_counter += 1

            elif planet_range == 1:
                new_planet = GaseousPlanet()
                new_planet.id_generator(new_planet)
                self.planet_list.append(new_planet)
                self.gaseous_counter += 1

            else:
                new_planet = HabitablePlanet()
                new_planet.id_generator(new_planet)
                self.planet_list.append(new_planet)
                self.habitable_counter += 1
                if self.goldilocs_zone >= new_planet.distance and (self.chance_of_life * 10000) > randint(1, 10000):
                    new_planet.life_exist = True


class DwarfStar(Star):
    def __init__(self):
        super().__init__(randint(2 ** 3, 2 ** 64) - 1, randint(2 ** 3, 2 ** 64) - 1, randint(2 ** 3, 2 ** 64) - 1,
                         0.0006, randint(8, 15), randint(30, 90), 2 ** 20)


class GiantStar(Star):
    def __init__(self):
        super().__init__(randint(2 ** 3, 2 ** 64) - 1, randint(2 ** 3, 2 ** 64) - 1, randint(2 ** 3, 2 ** 64) - 1,
                         0.0005, randint(5, 10), randint(150, 250), 2 ** 30)


class MediumStar(Star):
    def __init__(self):
        super().__init__(randint(2 ** 3, 2 ** 64) - 1, randint(2 ** 3, 2 ** 64) - 1, randint(2 ** 3, 2 ** 64) - 1,
                         0.0009, randint(2, 9), randint(60, 140), 2 ** 25)
