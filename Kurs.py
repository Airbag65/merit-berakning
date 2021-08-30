class Kurs:

    def __init__(self, name, points, grade):
        self.name = name
        self.points = points
        self.grade = grade


    def print_info(self, name, points, grade):
        self.name = name
        self.points = points
        self.grade = grade
        info_to_print = f"Kursens namn: {self.name}, Poäng: {self.points}, Betyg: {self.grade}"
        print (info_to_print)


    def calculate_score(self, points, grade):
        self.points = points
        self.grade = grade
        koresponerande_poang = {
            "F": 0,
            "E": 10,
            "D": 12.5,
            "C": 15,
            "B": 17.5,
            "A": 20
        }
        total = points * koresponerande_poang[grade]
        print (total)
        return total

'''
kurser = []    

Eng7 = Kurs("Engelska 7", 100, "A")
Mat4 = Kurs("Matematik 4", 100, "C")
kurser.append(Eng7)
kurser.append(Mat4)

for kurs in kurser:
    kurs.print_info(kurs.name, kurs.points, kurs.grade)
    kurs.calculate_score(kurs.points, kurs.grade)
'''
