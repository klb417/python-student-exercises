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


if __name__ == "__main__":
    report = StudentExerciseReports()
    report.all_cohorts()
    report.all_exercises_for_languages()
    report.all_exercises_for_languages("Javascript")
    report.all_exercises_for_languages("Python")
    report.all_exercises_for_languages("C#")
    report.all_people_with_cohort("student")
    report.all_people_with_cohort("instructor")
