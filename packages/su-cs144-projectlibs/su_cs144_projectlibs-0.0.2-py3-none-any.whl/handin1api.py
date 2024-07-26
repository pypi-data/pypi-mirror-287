from typing import Any

class Map:
    def __init__(self, size: int):
        pass


class Pollen:
    def __init__(self, information: Any):
        pass


class Flower:
    def __init__(self, row: int, col: int, pollen_type: str):
        pass

    def add_pollen(self, pollen: Pollen):
        pass


class Bee:
    def __init__(self, row: int, col: int, speed: int, perception: int):
        pass


class BeeHive:
    def __init__(self, row: int, col: int, num_bees: int):
        pass

    def add_bee(self, bee: Bee):
        pass


class DesertBee:
    def __init__(self, row: int, col: int, speed: int, perception: int):
        pass


class DesertBeeHive:
    def __init__(self, row: int, col: int, num_bees: int):
        pass

    def add_bee(self, bee: DesertBee):
        pass


class HoneyBee:
    def __init__(self, row: int, col: int, speed: int, perception: int):
        pass


class HoneyBeeHive:
    def __init__(self, row: int, col: int, num_bees: int):
        pass

    def add_bee(self, bee: HoneyBee):
        pass


class Wasp:
    def __init__(self, row: int, col: int, speed: int):
        pass


class WaspHive:
    def __init__(self, row: int, col: int, num_wasps: int):
        pass

    def add_wasp(self, wasp: Wasp):
        pass
