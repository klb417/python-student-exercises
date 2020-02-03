import sqlite3


class StudentExerciseReports:
    def __init__(self):
        self.db_path = (
            "/Users/klb/workspace/python/student-exercises/studentexercises.db"
        )

    def all_students(self):
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute(
                """
                SELECT s.first_name,
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
                print(f"{student[0]} {student[1]} is in {student[3]}")


report = StudentExerciseReports()
report.all_students()
