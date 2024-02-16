class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_major(self):
        return self.major


def calculate_average_grade(grades):
    """
    Calculates the average grade of a list of grades.

    Args:
        grades (list): A list of grades.

    Returns:
        float: The average grade.
    """
    total = sum(grades)
    average = total / len(grades)
    return average
