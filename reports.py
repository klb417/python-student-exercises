import sqlite3
from student import Student
from cohort import Cohort
from exercise import Exercise
from instructor import Instructor


class StudentExerciseReports:
    def __init__(self):
        self.db_path = (
            "/Users/klb/workspace/python/student-exercises/studentexercises.db"
        )

    def all_people_with_cohort(self, role):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = (
                lambda cursor, row: Student(row[1], row[2], row[3], row[4])
                if role == "student"
                else Instructor(row[1], row[2], row[3], row[5], row[4])
            )
            db_cursor = conn.cursor()
            specialty = ""
            if role == "instructor":
                specialty = f"r.specialty, "
            db_cursor.execute(
                f"""
                SELECT r.id,
                    r.first_name,
                    r.last_name,
                    r.slack_handle, {specialty}
                    c.name
                    FROM {role.capitalize()} r
                    JOIN Cohort c
                    ON r.cohort_id = c.id
                """
            )

            all_people_with_cohort = db_cursor.fetchall()
            print(f"\nAll {role}s")
            [print(f" {person}") for person in all_people_with_cohort]

    def all_cohorts(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[1])
            db_cursor = conn.cursor()

            db_cursor.execute(
                """
                    SELECT c.id, c.name
                    FROM Cohort c
                """
            )

            all_cohorts = db_cursor.fetchall()

            print(f"\nAll cohorts")
            [print(f" {cohort}") for cohort in all_cohorts]

    def all_exercises_for_languages(self, exercise_language="All"):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[0], row[1])
            db_cursor = conn.cursor()

            append_language = (
                f'WHERE e.programming_language LIKE "%{exercise_language}%"'
                if exercise_language != "All"
                else ""
            )
            db_cursor.execute(
                f"""
                SELECT e.name, e.programming_language 
                FROM Exercise e {append_language};
            """
            )

            all_exercises_for_languages = db_cursor.fetchall()

            print(f"\n{exercise_language} exercises")
            [print(f" {exercise.name}") for exercise in all_exercises_for_languages]

    def list_exercises_for_students(self):
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute(
                """
                    SELECT s.id, s.first_name, s.last_name, s.slack_handle, c.name, e.name
                    FROM Student s
                    JOIN AssignedExercise ae
                    ON s.id = ae.student_id 
                    JOIN Exercise e
                    ON ae.exercise_id = e.id
                    JOIN Cohort c
                    ON s.cohort_id = c.id;
            """
            )

            student_results = db_cursor.fetchall()
            student_dict = dict()

            for student in student_results:
                student_id = student[0]
                first_name = student[1]
                last_name = student[2]
                slack_handle = student[3]
                cohort = student[4]
                exercise = student[5]

                if student_id not in student_dict:
                    student_dict[student_id] = Student(
                        first_name, last_name, slack_handle, cohort, [exercise]
                    )
                else:
                    student_dict[student_id].current_exercises.append(exercise)

            for student_id, student in student_dict.items():
                print(f"{student.first_name} {student.last_name} is working on:")
                [print(f"  * {exercise}") for exercise in student.current_exercises]

    def list_students_for_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute(
                """
                    SELECT e.id, e.name, e.programming_language, s.first_name, s.last_name
                    FROM Student s
                    JOIN AssignedExercise ae
                    ON s.id = ae.student_id 
                    JOIN Exercise e
                    ON ae.exercise_id = e.id;
            """
            )

            exercise_results = db_cursor.fetchall()
            exercise_dict = dict()

            for exercise in exercise_results:
                exercise_id = exercise[0]
                exercise_name = exercise[1]
                programming_language = exercise[2]
                first_name = exercise[3]
                last_name = exercise[4]

                if exercise_id not in exercise_dict:
                    exercise_dict[exercise_id] = {
                        "name": exercise_name,
                        "language": programming_language,
                        "students": [f"{first_name} {last_name}"],
                    }
                else:
                    exercise_dict[exercise_id]["students"].append(
                        f"{first_name} {last_name}"
                    )

            for exercise_id, exercise in exercise_dict.items():
                print(f"{exercise['name']} is being worked on by:")
                [print(f"  * {student}") for student in exercise["students"]]


if __name__ == "__main__":
    # exercise 4
    report = StudentExerciseReports()
    report.all_cohorts()
    report.all_exercises_for_languages()
    report.all_exercises_for_languages("Javascript")
    report.all_exercises_for_languages("Python")
    report.all_exercises_for_languages("C#")
    report.all_people_with_cohort("student")
    report.all_people_with_cohort("instructor")

    # exercise 5
    # report.list_exercises_for_students()
    report.list_students_for_exercises()
