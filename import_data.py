import sqlite3
import csv
import random


class ImportData:
    def __init__(self):
        self.db_path = (
            "/Users/klb/workspace/python/student-exercises/studentexercises.db"
        )

    def insert_sql(self, sql_command):
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()
            db_cursor.execute(sql_command)
            conn.commit()

    def select_sql(self, sql_command):
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()
            db_cursor.execute(sql_command)
            return db_cursor.fetchall()


import_data = ImportData()


def import_exercises():
    with open(f"data/exercises.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        first_line = True
        for row in csv_reader:
            if first_line == True:
                first_line = False
            else:
                import_data.insert_sql(
                    f"""
                            INSERT INTO Exercise (name, programming_language)
                            VALUES ("{row[0]}", "{row[1]}");
                        """
                )


def import_people(cohort, role):
    with open(f"data/c{cohort}_{role}.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        first_line = True
        for row in csv_reader:
            if first_line == True:
                first_line = False
            else:
                specialty = ""
                if role == "instructor":
                    specialty = f' "{row[4]}",'

                import_data.insert_sql(
                    f"""
                        INSERT INTO {role.capitalize()} 
                            SELECT null, "{row[1]}", "{row[2]}", "{row[3]}",{specialty} c.id
                            FROM Cohort c
                            WHERE c.name = "Cohort {cohort}";
                    """
                )


def import_assigned_exercises():
    student_list = dict()
    for student_id in range(68, 128):
        student_list[student_id] = set()
        for assign in range(1, 7):
            student_list[student_id].add(random.randint(7, 21))
    for student_id, exercises_set in student_list.items():
        for exercise in exercises_set:
            import_data.insert_sql(
                f"""
                INSERT INTO AssignedExercise
                VALUES (null, {exercise}, {student_id})
            """
            )


# import_people("36", "student")
# import_people("37", "student")
# import_people("38", "student")

# import_people("36", "instructor")
# import_people("37", "instructor")
# import_people("38", "instructor")

# import_exercises()
# import_assigned_exercises()
