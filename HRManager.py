#===============================================================================================================
import json
from Employee import Employee


class HRManager:
    def __init__(self):
        self.employees = []
        self.load_from_json()  # Load existing employee data from a JSON file

    def add_employee(self, employee):
        if self.is_employee_id_unique(employee.employee_id):
            self.employees.append(employee)
            print("Employee added successfully.")
            self.save_to_json()  # Save updated employee data to a JSON file
        else:
            print("Employee ID already exists. Please choose a different ID.")

    def update_employee(self, employee_id, new_attributes):
        found = False
        for employee in self.employees:
            if employee.employee_id == employee_id:
                for key, value in new_attributes.items():
                    if hasattr(employee, key):
                        setattr(employee, key, value)
                found = True
                break
        if found:
            print("Employee information updated successfully.")
            self.save_to_json()  # Save updated employee data to a JSON file
        else:
            print("Employee not found with the given ID.")

    def remove_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)
                print("Employee removed successfully.")
                self.save_to_json()  # Save updated employee data to a JSON file
                return
        print("Employee not found with the given ID.")

    def is_employee_id_unique(self, employee_id):
        return all(employee.employee_id != employee_id for employee in self.employees)

    def save_to_json(self):
        # Save the list of employees to a JSON file
        employee_data = [employee.to_json() for employee in self.employees]
        with open("employee_data.json", "w") as json_file:
            json.dump(employee_data, json_file, indent=4)

    def load_from_json(self):
        # Load employee data from a JSON file
        try:
            with open("employee_data.json", "r") as json_file:
                data = json.load(json_file)
                for item in data:
                    employee = Employee.from_json(item)
                    self.employees.append(employee)
        except FileNotFoundError:
            print("Employee data file not found.")

    def record_attendance(self, employee_id, in_time, out_time):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.record_attendance(in_time, out_time)
                print("Attendance recorded successfully.")
                self.save_to_json()  # Save updated employee data to a JSON file
                return
        print("Employee not found with the given ID.")

    def display_employee_attendance(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.display_attendance()
                return
        print("Employee not found with the given ID.")

    def calculate_employee_total_working_hours(self, employee_id, start_date, end_date):
        total_hours = 0
        for employee in self.employees:
            if employee.employee_id == employee_id:
                total_hours = employee.calculate_total_working_hours(start_date, end_date)
                break
        if total_hours > 0:
            print(f"Total working hours for the specified period: {total_hours:.2f} hours")
        else:
            print("No attendance records found for the given employee ID or date range.")

    def view_employees(self):
        for employee in self.employees:
            employee.display_info()
            print()

    def save_employee_attendance_to_json(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.save_attendance_records_to_json()
                print(f"Attendance records for employee ID {employee_id} saved to JSON.")
                return
        print("Employee not found with the given ID.")

    def view_salary_summary(self):
        for employee in self.employees:
            salary_file_name = f"salary_record_employee_{employee.employee_id}.json"
            try:
                with open(salary_file_name, "r") as json_file:
                    salary_data = json.load(json_file)
                    monthly_salary = salary_data.get("monthly_salary", 0)
                    print(f"Employee ID: {employee.employee_id}")
                    print(f"Monthly Salary: ${monthly_salary:.2f}")
                    print()
            except FileNotFoundError:
                print(f"Salary record for Employee ID {employee.employee_id} not found.")
                print()

    def save_all_salary_records_to_json(self):
        # Save salary records for all employees to separate JSON files
        for employee in self.employees:
            employee.save_salary_record_to_json()

    def generate_payslip(self, employee_id):
        # Find the employee with the given employee_id
        employee = None
        for emp in self.employees:
            if emp.employee_id == employee_id:
                employee = emp
                break

        if employee:
            # Generate the payslip for the employee and save it to a text file
            payslip = employee.generate_pay_slip()
            with open(f"{employee_id}.txt", "w") as payslip_file:
                payslip_file.write(payslip)
        else:
            print("Employee not found.")

    
