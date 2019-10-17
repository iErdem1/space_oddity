from star import *
from planet import *
from random import randint


class Universe:
    def __init__(self):
        self.num_of_stars = 2 ** 10
        self.dwarf_counter = 0
        self.medium_counter = 0
        self.giant_counter = 0

        self.dwarf_rocky_counter = 0
        self.dwarf_gaseous_counter = 0
        self.dwarf_habitable_counter = 0

        self.medium_rocky_counter = 0
        self.medium_gaseous_counter = 0
        self.medium_habitable_counter = 0

        self.giant_rocky_counter = 0
        self.giant_gaseous_counter = 0
        self.giant_habitable_counter = 0

        self.dwarf_intel_life_counter = 0
        self.medium_intel_life_counter = 0
        self.giant_intel_life_counter = 0

        self.stars_list = []

        self.generate_star()
        self.define_universe()
        self.print_universe()

    def generate_star(self):
        for i in range(self.num_of_stars):
            star_range = randint(0, 2)
            if star_range == 0:
                new_star = DwarfStar()
                new_star.create_coordinate_log(new_star.x, new_star.y, new_star.z)
                while not new_star.create_coordinate_log(new_star.x, new_star.y, new_star.z):
                    new_star = DwarfStar()
                self.dwarf_counter += 1
                self.stars_list.append(new_star)
            elif star_range == 1:
                new_star = MediumStar()
                new_star.create_coordinate_log(new_star.x, new_star.y, new_star.z)
                while not new_star.create_coordinate_log(new_star.x, new_star.y, new_star.z):
                    new_star = MediumStar()
                self.medium_counter += 1
                self.stars_list.append(new_star)
            else:
                new_star = GiantStar()
                new_star.create_coordinate_log(new_star.x, new_star.y, new_star.z)
                while not new_star.create_coordinate_log(new_star.x, new_star.y, new_star.z):
                    new_star = GiantStar()
                self.giant_counter += 1
                self.stars_list.append(new_star)

    def define_universe(self):
        for star in self.stars_list:
            if isinstance(star, DwarfStar):
                for planet in star.planet_list:
                    if isinstance(planet, RockyPlanet):
                        self.dwarf_rocky_counter += 1
                    elif isinstance(planet, GaseousPlanet):
                        self.dwarf_gaseous_counter += 1
                    else:
                        self.dwarf_habitable_counter += 1
                        if planet.life_exist:
                            self.dwarf_intel_life_counter += 1

            if isinstance(star, MediumStar):
                for planet in star.planet_list:
                    if isinstance(planet, RockyPlanet):
                        self.medium_rocky_counter += 1
                    elif isinstance(planet, GaseousPlanet):
                        self.medium_gaseous_counter += 1
                    else:
                        self.medium_habitable_counter += 1
                        if planet.life_exist:
                            self.medium_intel_life_counter += 1

            if isinstance(star, GiantStar):
                for planet in star.planet_list:
                    if isinstance(planet, RockyPlanet):
                        self.giant_rocky_counter += 1
                    elif isinstance(planet, GaseousPlanet):
                        self.giant_gaseous_counter += 1
                    else:
                        self.giant_habitable_counter += 1
                        if planet.life_exist:
                            self.giant_intel_life_counter += 1

    def print_universe(self):
        print("Total number of stars in my universe: {}".format(self.num_of_stars))
        print("""There are {giant_star} Giant Star with:
    {giant_gaseous_num} Gaseous Planets
    {giant_rocky_num} Rocky Planets
    {giant_habitable_num} Habitable Planets.
    {giant_intel_num} Planets with Intelligent Life.""".format(giant_star=self.giant_counter,
                                                               giant_gaseous_num=self.giant_gaseous_counter,
                                                               giant_rocky_num=self.giant_rocky_counter,
                                                               giant_habitable_num=self.giant_habitable_counter,
                                                               giant_intel_num=self.giant_intel_life_counter))

        print("""There are {dwarf_star} Dwarf Stars with: 
    {dwarf_gaseous_num} Gaseous Planets
    {dwarf_rocky_num} Rocky Planets
    {dwarf_habitable_num} Habitable Planets
    {dwarf_intel_num} Planets with Intelligent Life""".format(dwarf_star=self.dwarf_counter,
                                                              dwarf_gaseous_num=self.dwarf_gaseous_counter,
                                                              dwarf_rocky_num=self.dwarf_rocky_counter,
                                                              dwarf_habitable_num=self.dwarf_habitable_counter,
                                                              dwarf_intel_num=self.dwarf_intel_life_counter))

        print("""There are {medium_star} Medium Stars with:
    {medium_gaseous_num} Gaseous Planets
    {medium_rocky_num} Rocky Planets
    {medium_habitable_num} Habitable Planets
    {medium_intel_num} Planets with Intelligent Life""".format(medium_star=self.medium_counter,
                                                               medium_gaseous_num=self.medium_gaseous_counter,
                                                               medium_habitable_num=self.medium_habitable_counter,
                                                               medium_rocky_num=self.medium_rocky_counter,
                                                               medium_intel_num=self.medium_intel_life_counter))
