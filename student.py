from nss_person import NSSPerson


class Student(NSSPerson):
    def __init__(self, first_name, last_name, slack_handle, cohort):
        super().__init__(first_name, last_name, slack_handle, cohort)
        self.current_exercises = list()

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is in {self.cohort}"
