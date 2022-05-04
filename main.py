import classes


class Cage(classes.Cage):

    def __init__(self, spase):
        super().__init__(spase)
        self.animals_list = []

    def add_animal(self, animal: classes.Animal) -> bool:
        if self.space - animal.space >= 0:

            self.space = self.space - animal.space
            self.animals_list.append(animal)

            return True
        else:
            return False

    def get_animals(self) -> list:

        return self.animals_list

    def free_space(self) -> int:

        return self.space


def main():

    cage1 = Cage(300)
    cage2 = Cage(200)

    lion = classes.Animal("Alex", 150)
    pinguin1 = classes.Animal("Gunter", 20)
    pinguin2 = classes.Animal("Ganter", 15)
    pinguin3 = classes.Animal("Ginter", 25)
    begemoth = classes.Animal("Gloria", 200)
    giraffe = classes.Animal("Melvin", 110)
    zebra = classes.Animal("Martin", 70)

    print(cage1.add_animal(lion))      # True
    print(cage2.add_animal(pinguin1))  # True
    print(cage1.add_animal(pinguin2))  # True
    print(cage2.add_animal(pinguin3))  # True
    print(cage1.add_animal(begemoth))  # False
    print(cage2.add_animal(giraffe))   # True
    print(cage1.add_animal(zebra))     # True
    print(cage1.free_space())          # 65
    print(cage2.free_space())          # 45
    print(cage1.get_animals())         # ['Alex', 'Ganter', 'Martin']
    print(cage2.get_animals())         # ['Gunter', 'Ginter', 'Melvin']


if __name__ == '__main__':
    main()
