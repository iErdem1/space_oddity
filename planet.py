from random import randint
from uuid import uuid1


class Planet:
    def __init__(self, distance):
        self.distance = distance
        self.planet_id = None
        self.life_exist = False

    @staticmethod
    def id_generator(pl_type=None):
        if isinstance(pl_type, RockyPlanet):
            id_start = "0001"
            uuid_part = uuid1()
            all_id = id_start + str(uuid_part)
            pl_type.planet_id = all_id

        elif isinstance(pl_type, GaseousPlanet):
            id_start = "0002"
            uuid_part = uuid1()
            all_id = id_start + str(uuid_part)
            pl_type.planet_id = all_id

        else:
            id_start = "0003"
            uuid_part = uuid1()
            all_id = id_start + str(uuid_part)
            pl_type.planet_id = all_id


class RockyPlanet(Planet):
    def __init__(self):
        super().__init__(randint(1, 300))


class GaseousPlanet(Planet):
    def __init__(self):
        super().__init__(randint(1, 300))


class HabitablePlanet(Planet):
    def __init__(self):
        super().__init__(randint(1, 300))
