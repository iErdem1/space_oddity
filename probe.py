from universe import *
from star import *
from random import randint
from math import *


class Probe:
    def __init__(self, fuel=2 ** 80, visited_stars=0, explored_planets=0, odometer=0):
        self.universe = Universe()

        self.fuel = fuel
        self.visited_stars = visited_stars
        self.explored_planets = explored_planets
        self.odometer = odometer
        self.livable_planet_id = None

        self.distance = 0

        self.origin_x = self.universe.stars_list[0].x
        self.origin_y = self.universe.stars_list[0].y
        self.origin_z = self.universe.stars_list[0].z

        self.current_x = None
        self.current_y = None
        self.current_z = None

        self.next_x = None
        self.next_y = None
        self.next_z = None

        self.search_stars()
        self.print_result()

    @staticmethod
    def distance_calculator(curr_x, curr_y, curr_z, next_x, next_y, next_z):
        diff = (pow((next_x - curr_x), 2) + pow((next_y - curr_y), 2) + pow((next_z - curr_z), 2))
        return sqrt(diff)

    def search_stars(self):
        counter = 0
        while counter <= len(self.universe.stars_list) - 1:
            self.current_x = self.universe.stars_list[counter].x
            self.current_y = self.universe.stars_list[counter].y
            self.current_z = self.universe.stars_list[counter].z

            self.next_x = self.universe.stars_list[counter + 1].x
            self.next_y = self.universe.stars_list[counter + 1].y
            self.next_z = self.universe.stars_list[counter + 1].z

            self.visited_stars += 1
            self.fuel += self.universe.stars_list[counter].recharge

            for planet in self.universe.stars_list[counter].planet_list:
                self.explored_planets += 1
                if planet.life_exist:
                    self.livable_planet_id = planet.planet_id
                    break
            self.distance = self.distance_calculator(self.current_x, self.current_y,
                                                     self.current_z, self.next_x, self.next_y, self.next_z)

            if self.fuel >= self.distance:
                self.odometer += self.distance
                self.fuel -= self.distance
                continue
            else:
                print("Out of fuel!!!")
                break

    def print_result(self):
        print("The Origin was: {x}.{y}.{z}".format(x=self.origin_x,
                                                   y=self.origin_y,
                                                   z=self.origin_z))
        print("""Travelled {mile}s:
        You have {fuel} fuel remaining.
        Visited {visited} stars.
        Explored {explored} planets.
        Found life on planet {planet_id}""".format(mile=self.odometer,
                                                   fuel=self.fuel,
                                                   visited=self.visited_stars,
                                                   explored=self.explored_planets,
                                                   planet_id=self.livable_planet_id))