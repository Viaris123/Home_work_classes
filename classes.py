class Animal:
    def __init__(self, name, space):
        self.name = name
        self.space = space

    def __str__(self):
        return self.name


class Cage:
    def __init__(self, space):
        self.space = space

    def add_animal(self, animal: Animal) -> bool:
        raise NotImplementedError

    def get_animals(self) -> list:
        raise NotImplementedError

    def free_space(self) -> int:
        raise NotImplementedError
