from Employee import Employee

class Manager(Employee):
    def __init__(self, employee_id, first_name, last_name, email, salary, department, direct_reports, management_rate):
        super().__init__(employee_id, first_name, last_name, email, salary)
        self.department = department
        self.direct_reports = direct_reports
        self.management_rate = management_rate

    def calculate_earnings(self):
        # Manager earns some percentage rate to his salary
        return self.salary + (self.management_rate / 100) * self.salary

