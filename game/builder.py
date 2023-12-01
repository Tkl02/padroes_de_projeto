#contruindo personagem 
class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.forca = 10
        self.vida = 1
        self.xp = 0
        self._observers = []

# adicionando observadores
    def add_observer(self, observer):
            self._observers.append(observer)

    def remove_observer(self, observer):
            self._observers.remove(observer)

    def notify_observers(self):
            for observer in self._observers:
                observer.update(self)

class MobsBuilder:
    def __init__(self):
        self.mob = Mobs()

    def set_nome(self, nome):
        self.mob.nome = nome
        return self

    def set_forca(self, forca):
        self.mob.forca = forca
        return self

    def set_vida(self, vida):
        self.mob.vida = vida
        return self

    def set_xp(self, xp):
        self.mob.xp = xp
        return self

    def build(self):
        return self.mob

# contrutor de mobs
class Mobs:
    def __init__(self):
        self.nome = ''
        self.forca = 0
        self.vida = 0
        self.xp = 0

    @staticmethod
    def criar_goblin():
        return MobsBuilder().set_nome('goblin').set_forca(9).set_vida(1).set_xp(80).build()

    @staticmethod
    def criar_orc():
        return MobsBuilder().set_nome('orc').set_forca(19).set_vida(2).set_xp(18).build()

    @staticmethod
    def criar_wivern():
        return MobsBuilder().set_nome('wivern').set_forca(29).set_vida(3).set_xp(28).build()

    @staticmethod
    def criar_dragon():
        return MobsBuilder().set_nome('dragon').set_forca(39).set_vida(4).set_xp(38).build()

    @staticmethod
    def criar_demon():
        return MobsBuilder().set_nome('demon').set_forca(49).set_vida(5).set_xp(48).build()

# contrução da torre
class Torre:
    def __init__(self):
        self.andares = {
            1: [Mobs().criar_goblin()],
            2: [Mobs().criar_orc()],
            3: [Mobs().criar_wivern()],
            4: [Mobs().criar_dragon()],
            5: [Mobs().criar_demon()],
        }
    def escolher_andar(self, andar):
        if andar in self.andares:
            return self.andares[andar][0]
        else:
            return 'Andar não encontrado'
    
def proximo_nivel(subject):
    if subject.xp >= 100:
        subject.vida += 1
        subject.forca += 10
        subject.xp = 0
        print('\033[92m' + f'Você subiu de nível, vida: {subject.vida} força: {subject.forca}\n' + '\033[0m')
        subject.notify_observers()
