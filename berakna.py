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
    

def calc_merit():
    global kurser
    total_points = 0
    total_merit = 0
    for kurs in kurser:
        total_points += kurs.points
        total_merit += kurs.calculate_score(kurs.points, kurs.grade)
    average_score = total_merit/total_points
    average_score = round(average_score, 2)
    return average_score

antal_kurser = int(input("Ange antal kurser att lägga till: "))

for i in range(antal_kurser - 1):
    add_course()

print("\n")

for kurs in kurser:
    print(kurs.name)
print("\n" + str(calc_merit()))
