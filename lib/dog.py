#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    APPROVED_BREEDS = ["Pug", "Corgi", "Beagle", "Dalmatian"]

    def __init__(self, name=None, breed="Mutt"):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self.name = name

        if not isinstance(breed, str) or breed not in self.APPROVED_BREEDS + ["Mutt"]:
            print("Breed must be in list of approved breeds.")
        else:
            self.breed = breed

    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")

