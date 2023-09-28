


class human:
    
    def __init__(self, skill, strength, speed, attack):
        self.skill = skill
        self.strength = strength
        self.speed = speed
        self.attack = attack
        
        
    def run(self):
        self.speed = self.speed + 10
        print("speed increased to {}".format(self.speed))
        
    def fight(self, enemy):
        
        print("Human fights ",enemy)
        
    def practice(self):
        self.skill = self.skill + 3
        print("skill increased to {} after training session".format(self.skill))
        
        
Brutus = human(10, 25, 30, 13)

Brutus.run()

Brutus.fight("Percy")

Brutus.practice()

