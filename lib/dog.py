class Dog:
    APPROVED_BREEDS = [
        "Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle",
        "French Bulldog", "Pug", "Pointer"
    ]

    def __init__(self, name="Unknown", breed="Unknown"):
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name

    def set_name(self, name):
        if not isinstance(name, str):
            print("Name must be between 1 and 25 characters.")
        elif not name:
            print("Name must be between 1 and 25 characters.")
        elif not (1 <= len(name) <= 25):
            print("Name must be between 1 and 25 characters.")
        else:
            self._name = name

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in self.APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in the list of approved breeds.")

    breed = property(get_breed, set_breed)


