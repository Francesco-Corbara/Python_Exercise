## salve Prof , questa scheda non è importante , la ho usata solo per provare roba o segnarmi cose

class track:



    
    def __init__(self, title:str , artist:str , duration:int) -> None: 
        self.title = title
        self.artist = artist
        self.duration = duration

    @property
    def ChangeTitle(self) -> int:
        self.title

    @ChangeTitle.setter
    def ChangeTitle (self , value:str) -> None:
        if not value:
            raise ValueError("the title cannot be empty")

class GradeBook:
    def __init__(self) -> None:
        self.grades = []

    def add_grade(self, grade: float) -> None:
        if not 0 <= grade <= 10:
            raise ValueError("Grade must be between 0 and 10")
        self.grades.append(grade)

    def average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def status(self) -> str:
        if self.average() >= 6:
            return "passed"
        return "failed"


if __name__ == "__main__":
    gradebook = GradeBook()
    for g in (7, 5, 8):
        gradebook.add_grade(g)

    print(f"Grades: {gradebook.grades}")
    print(f"Average: {gradebook.average():.2f} ({gradebook.status()})")  