class KiloMan:
    def __init__(self):
        self.level = list(map(int, input().split()))
        self.actions = [action for action in input()]
        self.damage = 0
    
    def damage_amount(self, amount):
        self.damage = 0
        for i in range(amount):
            if self.one_or_two(self.level[i],self.actions[i]):
                self.damage += 1
            elif self.three_or_higher(self.level[i], self.actions[i]):
                self.damage += 1
        return self.damage
    
    def one_or_two(self, lv, act):
        return lv in (1,2) and act == "S"

    def three_or_higher(self, lv, act):
        return lv >= 3 and act == "J"


def main():
    count = int(input())

    for i in range(count):
        amount = int(input())
        Hero = KiloMan()
        print(Hero.damage_amount(amount))


if __name__ == "__main__":
    main()