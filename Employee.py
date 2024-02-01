#===========================================================================================

from datetime import datetime, date
from datetime import datetime
import json


class Employee:
    def __init__(self, employee_id, first_name, last_name, email, base_annual_salary, role=None):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.base_annual_salary = base_annual_salary
        self.role = role
        self.allowances = {}
        self.bonuses = 0
        self.deductions = 0
        self.attendance_records = []
        self.salary_records = []

    def set_allowances(self, allowances):
        self.allowances = allowances

    def set_bonuses(self, bonuses):
        self.bonuses = bonuses

    def set_deductions(self, deductions):
        self.deductions = deductions

    def calculate_monthly_salary(self):
        annual_salary = self.base_annual_salary + sum(self.allowances.values()) + self.bonuses - self.deductions
        monthly_salary = annual_salary / 12
        return monthly_salary

    def record_attendance(self, in_time, out_time):
        # Add the attendance record for the employee
        self.attendance_records.append({"in_time": in_time, "out_time": out_time})
    def display_attendance(self):
        if not self.attendance_records:
            print("No attendance records found for this employee.")
        else:
            print("Attendance Records:")
            for i, record in enumerate(self.attendance_records, start=1):
                in_time = record["in_time"]
                out_time = record["out_time"]
                print(f"Record {i}: In-Time - {in_time}, Out-Time - {out_time}")

    def save_attendance_records_to_json(self):
        # Save attendance records to a JSON file
        attendance_data = {
            "employee_id": self.employee_id,
            "attendance_records": self.attendance_records
        }
        with open(f"attendance_record_employee_{self.employee_id}.json", "w") as json_file:
            json.dump(attendance_data, json_file, indent=4)

    def calculate_total_working_hours(self, start_date, end_date):
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        
        total_hours = 0

        for record in self.attendance_records:
            record_datetime = datetime.strptime(record["in_time"], "%H:%M")
            if start_date <= record_datetime.date() <= end_date:
                total_hours += record_datetime.hour + record_datetime.minute / 60

        return total_hours

    
    def calculate_monthly_salary(self):
        if isinstance(self.allowances, dict):
            # If allowances are a dictionary, calculate the sum of the values
            allowances_sum = sum(float(value) for value in self.allowances.values() if str(value).replace(".", "", 1).isdigit())
        else:
            # If allowances are a single value, convert it to a float
            allowances_sum = float(self.allowances)

        annual_salary = self.base_annual_salary + allowances_sum + self.bonuses - self.deductions
        monthly_salary = annual_salary / 12
        return monthly_salary



    def save_salary_record_to_json(self):
        # Save the employee's salary record to a JSON file
        salary_data = {
            "employee_id": self.employee_id,
            "monthly_salary": self.calculate_monthly_salary()
        }
        with open(f"salary_record_employee_{self.employee_id}.json", "w") as json_file:
            json.dump(salary_data, json_file, indent=4)


    def generate_pay_slip(self):
        payslip = f"Employee ID: {self.employee_id}\n"
        payslip += f"Name: {self.first_name} {self.last_name}\n"
        payslip += f"Email: {self.email}\n"
        payslip += f"Base Annual Salary: ${self.base_annual_salary}\n"
        payslip += f"Role: {self.role}\n"
        payslip += f"Monthly Salary: ${self.calculate_monthly_salary()}\n"
        payslip += f"Allowances: {self.allowances}\n"
        payslip += f"Bonuses: ${self.bonuses}\n"
        payslip += f"Deductions: ${self.deductions}\n"

        return payslip

   


    def to_json(self):
        employee_data = {
            "employee_id": self.employee_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "base_annual_salary": self.base_annual_salary,
            "role": self.role,
            "allowances": self.allowances,
            "bonuses": self.bonuses,
            "deductions": self.deductions
        }
        return json.dumps(employee_data)
    
    def display_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Base Annual Salary: {self.base_annual_salary}")
        print(f"Role: {self.role}")
        print(f"Allowances: {self.allowances}")
        print(f"Bonuses: {self.bonuses}")
        print(f"Deductions: {self.deductions}")
        print("Attendance Records:")
        for record in self.attendance_records:
            print(f"In-Time: {record['in_time']}, Out-Time: {record['out_time']}")
        print()



    @classmethod
    def from_json(cls, json_data):
        employee_data = json.loads(json_data)
        employee = cls(
            employee_data.get("employee_id", None),
            employee_data.get("first_name", None),
            employee_data.get("last_name", None),
            employee_data.get("email", None),
            employee_data.get("base_annual_salary", 0),
            employee_data.get("role", None)
        )
        allowances = employee_data.get("allowances", {})
        employee.set_allowances(allowances)

        bonuses = employee_data.get("bonuses", 0)
        employee.set_bonuses(bonuses)

        deductions = employee_data.get("deductions", 0)
        employee.set_deductions(deductions)

        return employee

