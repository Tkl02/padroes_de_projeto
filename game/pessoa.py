class Pessoa:
    def __init__(self, name, years, meat=False, speaking=False):
        self.name = name
        self.years = years
        self.meat = meat
        self.speaking = speaking

    def eat(self, alimento):
        if self.meat:
            print(f'{self.name} ja esta comendo')
            return

        print(f'{self.name} começou a comer')
        self.meat = True

    def para_comer(self):
        if self.meat == True:
            print(f'{self.name} parou de comer')
            self.meat = False
            return
        if self.meat == False:
            print(f'{self.name} não esta comendo')
            return