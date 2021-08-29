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

    def calculate_score(self, points):
        self.points = points
        koresponerande_poang = {
            "F": 0,
            "E": 10,
            "D": 12.5,
            "C": 15,
            "B": 17.5,
            "A": 20
        }
        print(koresponerande_poang)
    

Eng7 = Kurs("Engelska 7", 100, "A")
Eng7.print_info(Eng7.name, Eng7.points, Eng7.grade)
Eng7.calculate_score(Eng7.points)