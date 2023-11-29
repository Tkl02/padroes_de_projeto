#observer
class Observer:
    def update(self, subject):
        pass
class XPObserver(Observer):
    def __init__(self, personagem):
        self.personagem = personagem

    def update(self, subject):
        if subject.xp >= 100:
            subject.vida += 1
            subject.forca += 10
            subject.xp = 0
            print('\033[92m' + f'Você subiu de nível, vida: {subject.vida} força: {subject.forca}\n' + '\033[0m')
            self.personagem.notify_observers()

    @property
    def xp(self):
        return self.xp

    @xp.setter
    def xp(self, value):
        self.xp = value
        self.notify_observers()

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)