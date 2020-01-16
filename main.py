import csv
import random
from student import Student
from instructor import Instructor
from cohort import Cohort
from exercise import Exercise

exercises = [
    Exercise("Advanced Divs", "HTML"),
    Exercise("Setting the Lists: The Python Dictionary", "Python"),
    Exercise("Getting a Date()", "Javascript"),
    Exercise("Props to the Component", "Javascript"),
    Exercise("Snake Case for Dummies", "Python"),
    Exercise("Varied Variables", "Javascript"),
    Exercise("Apple Pie vs. Apple.py", "Python"),
    Exercise("Pip Pip Hooray", "Python"),
    Exercise("Oh No What Have I Done", "Javascript"),
    Exercise("Making Ugly Less Ugly", "CSS"),
    Exercise("Imports/Exports: Tariffs Explained", "C#"),
    Exercise("Tuplepocalypse", "Python"),
    Exercise("Stop Creating Data", "Python"),
    Exercise("Mocking Students", "C#"),
    Exercise("Comprehending Comprehensions", "Python"),
]


def import_people(cohort, role):
    people = []

    with open(f"data/c{cohort}_{role}.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        first_line = True
        for row in csv_reader:
            if first_line == True:
                first_line = False
            else:
                if role == "student":
                    people.append(Student(row[1], row[2], row[3], f"Cohort {cohort}"))
                else:
                    people.append(
                        Instructor(row[1], row[2], row[3], f"Cohort {cohort}", row[4])
                    )
        return people


c36 = Cohort("Cohort 36")
c36.add_students(import_people("36", "student"))
c36.add_instructors(import_people("36", "instructor"))

c37 = Cohort("Cohort 37")
c37.add_students(import_people("37", "student"))
c37.add_instructors(import_people("37", "instructor"))

c38 = Cohort("Cohort 38")
c38.add_students(import_people("38", "student"))
c38.add_instructors(import_people("38", "instructor"))

cohorts = [c36, c37, c38]

for cohort in cohorts:
    for instructor in cohort.instructors:
        for student in cohort.students:
            for assign in range(2):
                instructor.assign_exercise(random.choice(exercises).name, student)
            student.current_exercises = list(set(student.current_exercises))

for cohort in cohorts:
    for student in cohort.students:
        print(
            f"{student.first_name} {student.last_name} is working on {len(student.current_exercises)} exercises: \n\t"
            + "\n\t".join(student.current_exercises),
            "\n",
        )
