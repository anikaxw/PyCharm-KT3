import random


class Fighter:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        self.weight = random.randint(50, 100)
        self.height = random.randint(150, 200)
        self.power = (self.height + self.weight) / 2
        self.show_info()

    def attack(self, fighter) -> bool:
        damage = random.randint(1, 20)
        evade = random.randint(1, 10)

        if evade !=1:
            fighter.power = fighter.power - damage
            print(f"{fighter.name}: отхватил {damage}, здоровья {fighter.power}")
            if fighter.power<=0:
                fighter.is_alive=False
            else:
                fighter.is_alive=True

        else:
            print(f"{fighter.name} Удар заблокировал")

    def show_info(self):
        print(f"{self.name}:рост{self.height}, вес{self.weight}здоровьe{self.power}")


class Contest:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def fight(self):
        l=[self.first, self.second]
        current = random.choice(l)
        print(current.name + "атакует первым")
        if current == self.first:
            destination = self.second
        else:
            destination = self.first
        while (current.is_alive and destination.is_alive):
            current.attack(destination)
            if (current.is_alive == False):
                winner = destination
            else:
                winner = current
            current, destination = destination, current

        return winner


contest = Contest(Fighter("Вася"), Fighter("Петя"))
winner = contest.fight()
print("Победил боец", winner.name)