import unittest

class StudentManager:
    def _init_(self):

        def add_student(self, name: str, grades: list):
            if name in self.students:
                raise ValueError(f"Student {name} already exists.")
                if not all(isinstance(grade, (int,float)) for grade in grades):
                    raise ValueError("Grades must be a list of numbers.")
                    self.students[name] = grades

        def get_average(self, name: str) -> float:
            if name not in self.students:
                raise ValueError(f"Student {name} does not exist.")
                return sum(self.students[name]/len(self.students[name]))

        def is_passed(self, name: str, passing_grade: float = 6.0) -> bool:
            average = self.get_average(name)
            return average >= passing_grade

# class TestStudentManager(unittest.TestCase):
#     def test_add_student(self):
#         self.assertEqual(_init_(add_student("Gabriel", 8), get_average("Gabriel"), 
#         is_passed("Gabriel")), True)

class TestStudentManager(unittest.TestCase):
    def setUp(self):
    #configuração inicial para cada teste.
    self.manager = StudentManager()

    def test_add_student(self):
        self.manager.add_student("Gabriel", [8.0, 7.5, 6.3, 7.0])
        self.assertIn("Aline", self.manager.students)

    def test_add_student_existing(self):
        self.manager.add_student("Alice", [8.0, 7.5, 6.3, 7.0])
        with self.assertRaises(ValueError):
            self.manager.add_student("Alice", [6.0, 7.0])
                            