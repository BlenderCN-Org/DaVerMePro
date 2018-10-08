class Person:
    # pass
    def __init__(self, name, nummer):
        self.Name = name
        self.Nummer = nummer

nePerson = Person("Horst", 42)

# nePerson = Person()
# nePerson.Name = "Horst"
# nePerson.Nummer = 42

print("Hier ist " +nePerson.Name + " mit der Nummer " + str(nePerson.Nummer))
