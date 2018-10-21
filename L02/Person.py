class Person(object):
    # pass
    def __init__(self, firstName, lastName, Number):
        self.FirstName = firstName
        self.LastName = lastName
        self.Number = Number


programmRunning = True
# nePerson = Person("Horst", 42)

# # nePerson = Person()
# # nePerson.Name = "Horst"
# # nePerson.Nummer = 42

# print("Hier ist " +nePerson.Name + " mit der Nummer " + str(nePerson.Nummer))

personList = []
personList.append(Person("Max", "Herre", "1"))
personList.append(Person("Benedikt", "Grether", "2"))
personList.append(Person("Tobi", "Test", "3"))
personList.append(Person("Mark", "Foster", "4"))
personList.append(Person("Smudo", "Irgendwas", "5"))


while programmRunning == True:
    print()
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("Drücke A um alle Personen anzuzeigen")
    print("Drücke B um eine eine neue Person anzulegen")
    print("Drücke C um eine Person zu ändern")
    print("Drücke D um eine Person zu löschen")
    print("Drücke E um das Programm zu beenden")
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print()
    inputCases = input("Ihre Eingabe > ")
        
    if inputCases == "A":
        for person in personList:
            print(person.FirstName, person.LastName, person.Number)
    
    elif inputCases == "B":
        firstNameInput = input("Bitte Vorname eingeben > ")
        lastNameInput = input("Bitte Nachname eingeben > ")
        numberInput = input("Bitte Personalnummer eingeben > ")
        personList.append(Person(firstNameInput, lastNameInput, numberInput))
        print()

    elif inputCases == "C":
        changePersonInput = input("Welche Person möchten sie verändern? > ")
        personList.index(Person (changePersonInput))
        # for person in personList:
        #     if changePersonInput in person.FirstName:
        #         firstNameInput = input("Bitte Vorname eingeben >")
        #         lastNameInput = input("Bitte Nachname eingeben >")
        #         numberInput = input("Bitte Personalnummer eingeben >")
                #personList.index(changePersonInput)
    elif inputCases == "D":
        deletePersonInput = input("Welche Person soll entfernt werden > ")

    elif inputCases == "E":
        print("Das Programm wird nun Beendet")
        programmRunning = False