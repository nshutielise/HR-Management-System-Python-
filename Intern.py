from Employee import Employee

class Intern(Employee):
    def __init__(self, employee_id, first_name, last_name, email, salary, university, program, internship_duration):
        super().__init__(employee_id, first_name, last_name, email, salary)
        self.university = university
        self.program = program

        # condition on time for internship (3-6 months)
        if internship_duration < 3:
            self.internship_duration = 3
        elif internship_duration > 6:
            self.internship_duration = 6
        else:
            self.internship_duration = internship_duration

    def calculate_earnings(self):
        # intern earns based on the months worked between 3-6 months
        return (self.salary * self.internship_duration) / 12

