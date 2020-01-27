class Enemy:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def is_alive(self):
        return self.hp > 0


class CityChicken(Enemy):
    def __init__(self):
        super().__init__(name="City Chicken", hp=10, dmg=2)


class CountryChicken(Enemy):
    def __init__(self):
        super().__init__(name="Country Chicken", hp=20, dmg=5)


class WaterChicken(Enemy):
    def __init__(self):
        super().__init__(name="Water Chicken", hp=45, dmg=10)
