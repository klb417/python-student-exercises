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


# arguments are starting index for instructors and students. This is a quick and ugly way to not mix up the cohort assignments
def import_assigned_exercises(starting_instructor_id, starting_student_id):
    student_dict = dict()
    for instructor in range(starting_instructor_id, starting_instructor_id + 3):
        for student_id in range(starting_student_id, starting_student_id + 20):
            if student_id not in student_dict:
                student_dict[student_id] = set()
            for num in range(1, 3):
                new_exercise = random.randint(7, 21)
                if new_exercise not in [
                    assigned_exercise[0]
                    for assigned_exercise in student_dict[student_id]
                ]:
                    student_dict[student_id].add((new_exercise, instructor))
    for student_id, exercises_set in student_dict.items():
        for exercise in exercises_set:
            import_data.insert_sql(
                f"""
                INSERT INTO AssignedExercise
                VALUES (null, {exercise[0]}, {student_id}, {exercise[1]})
            """
            )


# import_people("36", "student")
# import_people("37", "student")
# import_people("38", "student")

# import_people("36", "instructor")
# import_people("37", "instructor")
# import_people("38", "instructor")

# import_exercises()
# import_assigned_exercises(1, 1)
