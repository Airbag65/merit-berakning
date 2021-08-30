from Kurs import Kurs

kurser = []

def add_course():
    global kurser
    print("\nLägg till kurs:")
    name = input("Namn: ")
    points = int(input("Poäng: "))
    grade = input("Betyg: ")
    kurs = Kurs(name, points, grade)
    kurser.append(kurs)
    


for kurs in kurser:
    print(kurs.name)