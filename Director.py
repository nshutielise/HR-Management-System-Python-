from Employee import Employee

class Director(Employee):
    def __init__(self, employee_id, first_name, last_name, email, base_annual_salary, annual_bonus):
        super().__init__(employee_id, first_name, last_name, email, base_annual_salary)
        self.annual_bonus = annual_bonus


    def calculate_earnings(self):
        # Directors earn an annual bonus added to their salary
        return self.salary + self.annual_bonus
