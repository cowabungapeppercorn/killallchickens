class Item():
    def __init__(self, name, desc, value, weight):
        self.name = name
        self.desc = desc
        self.value = value
        self.weight = weight

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nWeight: {}".format(self.name,
                                                             self.desc,
                                                             self.value,
                                                             self.weight)


class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         desc="A gold coin worth {} dogshits."
                         .format(str(self.amt)),
                         value=self.amt,
                         weight=0)

    def __str__(self):
        return "A gold coin worth {} dogshits".format(str(self.amt))


class Weapon(Item):
    def __init__(self, name, desc, value, weight, dmg):
        self.dmg = dmg
        super().__init__(name, desc, value, weight)

    def __str__(self):
        return """{}\n=====\n{}\nValue: {}\nWeight: {}\n
               Damage: {}""".format(self.name, self.desc,
                                    self.value, self.weight, self.dmg)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock", desc="A decent smashin' rock.",
                         value=1, weight=2, dmg=5)

    def __str__(self):
        return self.name


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger", desc="A small rusty dagger.",
                         value=5, weight=1, dmg=10)

    def __str__(self):
        return self.name
