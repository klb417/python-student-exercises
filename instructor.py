from nss_person import NSSPerson


class Instructor(NSSPerson):
    def __init__(self, first_name, last_name, slack_handle, cohort, specialty):
        super().__init__(first_name, last_name, slack_handle, cohort)
        self.specialty = specialty

    def assign_exercise(self, exercise, student):
        student.current_exercises.append(exercise)
