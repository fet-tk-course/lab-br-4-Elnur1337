#Ime: Elnur
#Prezime: BJelić
#Lab 4 - Python za FastAPI

student = {"ime": "Elnur", "godina": "3", "email": "elnur.bjelic@fet.ba", "status": "Redovan"}
print(student)
print(student["ime"])
student["aktivan"] = True

studenti = [
    {"ime": "Elnur", "godina": "3", "email": "elnur.bjelic@fet.ba", "aktivan": True},
    {"ime": "Amer", "godina": "4", "email": "amer.imamovic@fet.ba", "aktivan": True},
    {"ime": "Tarik", "godina": "3", "email": "tarik.jukan@fet.ba", "aktivan": False}
]

def get_student_info(name: str,year: int, email: str) -> dict:
    for student in studenti:
        if student["ime"] == name and student["godina"] == str(year) and student["email"] == email:
            student["greeting"] = f"Zdravo {name}, vi ste {str(year)}. godine studija."
            return student
    return {"greska": "Student nije pronađen."}

# def get_student_info(studentInput: dict) -> dict:
#     for student in studenti:
#         if student["ime"] == studentInput["ime"] and student["godina"] == str(studentInput["godina"]) and student["email"] == studentInput["email"]:
#             student["greeting"] = f"Zdravo {studentInput['ime']}, vi ste {str(studentInput['godina'])}. godine studija."
#             return student
#     return {"greska": "Student nije pronađen."}

print(get_student_info("Elnur", 3, "elnur.bjelic@fet.ba"))
# print(get_student_info({"ime": "Elnur", "godina": 3, "email": "elnur.bjelic@fet.ba", "aktivan": True}))

def ispisi_poziv(func):
    def wrapper(*args, **kwargs):
        print(f"Pozivam: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@ispisi_poziv
def info_o_studentu(name: str, year: int, email: str) -> dict:
    pass 
    for student in studenti:
        if student["ime"] == name and student["godina"] == str(year) and student["email"] == email:
            student["greeting"] = f"Zdravo {name}, vi ste {str(year)}. godine studija."
            return student
    return {"greska": "Student nije pronađen."}

print(info_o_studentu("Elnur", 3, "elnur.bjelic@fet.ba"))

class Course:
    def __init__(self, name: str, code: str, credits: int, professor: str):
        self.name = name
        self.code = code
        self.credits = credits
        self.professor = professor

    def description(self) -> str:
        return f"{self.code} - {self.name} ({self.credits} kredita) - Profesor: {self.professor}"

kurs1 = Course("Programiranje 1", "PR1", 6, "Dr. Smith")
kurs2 = Course("Matematika 1", "MT1", 5, "Dr. Johnson")
print(kurs1.description())
print(kurs2.description())

students = [
    {"ime": "Elnur", "godina": "3", "email": "elnur.bjelic@fet.ba", "aktivan": True},
    {"ime": "Amer", "godina": "4", "email": "amer.imamovic@fet.ba", "aktivan": True},
    {"ime": "Tarik", "godina": "3", "email": "tarik.jukan@fet.ba", "aktivan": False},
    {"ime": "Sara", "godina": "2", "email": "sara.sarovic@fet.ba", "aktivan": True}
]

def filter_by_year(students: list, year: int) -> list:
    filtered_students = []
    for student in students:
        if student["godina"] == str(year):
            filtered_students.append(student)
    return filtered_students

def filter_by_year_comprehension(students: list, year: int) -> list:
    return [student for student in students if student["godina"] == str(year)]

def print_registry(students: list) -> None:
    for student in students:
        print(f"{student["ime"]} - {student["email"]}\n")

print("--------------------")
print(filter_by_year(students, 3))
print_registry(students)

def sort_students_by_year(students: list) -> list:
    return sorted(students, key=lambda x: x["godina"])

print(sort_students_by_year(students))

print(filter_by_year_comprehension(students, 3))

def get_students_by_name_first_letter(students: list, letter: str) -> list:
    return [student for student in students if student["ime"].startswith(letter)]

print(get_students_by_name_first_letter(students, "E"))