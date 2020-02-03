import sqlite3
from student import Student


class StudentExerciseReports:
    def __init__(self):
        self.db_path = (
            "/Users/klb/workspace/python/student-exercises/studentexercises.db"
        )

    def create_student(self, cursor, row):
        return Student(row[1], row[2], row[3], row[4])

    def all_students(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = self.create_student
            db_cursor = conn.cursor()

            db_cursor.execute(
                """
                SELECT s.id,
                    s.first_name,
                    s.last_name,
                    s.slack_handle,
                    c.name
                    FROM Student s
                    JOIN Cohort c
                    ON s.cohort_id = c.id
                """
            )

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(
                    f"{student.first_name} {student.last_name} is in {student.cohort}"
                )


report = StudentExerciseReports()
report.all_students()
