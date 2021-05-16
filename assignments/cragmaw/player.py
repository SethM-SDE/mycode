import dice


class Player:
    def __init__(self):
        self.inventory = []
        self.damage = '1d12'
        self.health = 25

        def attack(self):
            return dice.roll(self.damage)

        def add_item(item):
            self.inventory.append(item)

        def remove_item(item):
            self.inventory.remove(item)

        def get_inv(self):
            return self.inventory
