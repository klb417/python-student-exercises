from nss_person import NSSPerson


class Student(NSSPerson):
    def __init__(
        self, first_name, last_name, slack_handle, cohort, current_exercises=[]
    ):
        super().__init__(first_name, last_name, slack_handle, cohort)
        self.current_exercises = current_exercises

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is in {self.cohort}"
