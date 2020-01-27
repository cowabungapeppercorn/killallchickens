import items
import enemies
import actions
import world


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves


class StartingRoom(MapTile):
    def intro_text(self):
        return """\n
        ------------------------------\n
        You find yourself in a small, shit-covered hut. There
        are shitty drawings of chickens on the walls. City chickens.
        Water chickens. Country chickens. Bald chickens. Fuckin
        chickens...\n
        ------------------------------"""

    def modify_player(self, player):
        pass


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.dmg
            print("Enemy does {} damage. You have {} HP remaining."
                  .format(self.enemy.dmg, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class EmptyCavePath(MapTile):
    def intro_text(self):
        return """\n
        ------------------------------\n
        Boring ass cave...\n
        ------------------------------"""

    def modify_player(self, player):
        pass


class CityChickenRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.CityChicken())

    def intro_text(self):
        if self.enemy.is_alive():
            return """\n
            ------------------------------\n
            Oh shit it's a City Chicken!! Fuck me!!\n
            ------------------------------"""
        else:
            return """\n
            ------------------------------\n
            Damn that dead City Chicken smells like dick!\n
            ------------------------------"""


class CountryChickenRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.CountryChicken())

    def intro_text(self):
        if self.enemy.is_alive():
            return """\n
            ------------------------------\n
            Fuckin a boys its a Country Chicken.\n
            ------------------------------"""
        else:
            return """\n
            ------------------------------\n
            This Country Chicken's deader'n a dead deer.\n
            ------------------------------"""


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """\n
        ------------------------------\n
        You see a dope ass rusty dagger and scoop it.\n
        ------------------------------"""


class Find5GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(5))

    def intro_text(self):
        return """\n
        ------------------------------\n
        You find 5 gold whoopdy fuckin doo.\n
        ------------------------------"""


class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """\n
        ---------------VICTORY---------------\n
        Thank fuck, let's get out this ho.\n
        ---------------VICTORY---------------"""

    def modify_player(self, player):
        player.victory = True
