from nss_person import NSSPerson


class Instructor(NSSPerson):
    def __init__(self, first_name, last_name, slack_handle, cohort, specialty):
        super().__init__(first_name, last_name, slack_handle, cohort)
        self.specialty = specialty
        self.assigned_exercises = []

    def assign_exercise(self, exercise, student):
        student.current_exercises.append(exercise)

    def __repr__(self):
        return f"{self.first_name} {self.last_name} instructs {self.cohort} and specializes in {self.specialty}"
