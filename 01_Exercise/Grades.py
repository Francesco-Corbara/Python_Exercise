from typing import List


class GradeBook:
    def __init__(self) -> None:
        self.grades: List[float] = []

    def add_grade(self, new_grade: float) -> None:
        if new_grade < 0 or new_grade > 10:
            raise ValueError("Grade must be between 0 and 10")
        self.grades.append(new_grade)

    def average(self) -> float:
        if len(self.grades) == 0:
            return 0.0
        total = 0.0
        for grade in self.grades:
            total += grade
        return total / len(self.grades)

    def outcome(self) -> str:
        if self.average() >= 6.0:
            return "sufficient"
        else:
            return "to be recovered"


if __name__ == "__main__":
    my_grades = GradeBook()

    initial_grades = [7.5, 5.0, 8.0]
    for g in initial_grades:
        my_grades.add_grade(g)

    print(f"Grades list: {my_grades.grades}")
    print(f"Average: {my_grades.average():.2f} - Status: {my_grades.outcome()}")