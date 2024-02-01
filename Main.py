#================================================================================================================

import json
from Employee import Employee
from HRManager import HRManager
from datetime import datetime, date

def main():
    hr_manager = HRManager()

    while True:
        print("\nHR Management System")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Remove Employee")
        print("4. Record Attendance")
        print("5. Display Employee Attendance")
        print("6. Calculate Total Working Hours")
        print("7. View Employees")
        print("8. View Salary Summary")
        print("9. Generate Payslip")
        print("10. Save Salary Records to JSON")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            role = input("Enter the role (Director, Manager, or Intern): ").capitalize()
            if role not in ["Director", "Manager", "Intern"]:
                print("Invalid role. Please enter Director, Manager, or Intern.")
                continue

            try:
                employee_id = int(input("Employee ID: "))
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                email = input("Email: ")
                base_annual_salary = float(input("Base Annual Salary: "))
                
                # Create an employee object with the collected data
                employee = Employee(employee_id, first_name, last_name, email, base_annual_salary, role)
                
                if role == "Director":
                    annual_bonus = float(input("Annual Bonus: "))
                    employee.set_bonuses(annual_bonus)

                elif role == "Manager":
                    department = input("Department: ")
                    direct_reports = int(input("Direct Reports: "))
                    management_rate = float(input("Management Rate (%): "))
                    employee.set_allowances({
                        "department": department,
                        "direct_reports": direct_reports
                    }) 
                    employee.set_bonuses(management_rate)

                else:
                    university = input("University: ")
                    program = input("Program: ")
                    internship_duration = int(input("Internship Duration (months): "))
                    employee.set_allowances({
                        "university": university,
                        "program": program,
                        "internship_duration": internship_duration
                    })

                # Add the employee to the HRManager
                hr_manager.add_employee(employee)
                print(f"{role} added successfully.")
            except ValueError:
                print("Invalid input. Please enter valid numerical values for employee details.")

        elif choice == "2":
            employee_id = input("Enter the Employee ID to update: ")
            if not employee_id.isdigit():
                print("Employee ID should be a number.")
                continue

            new_attributes = {}
            while True:
                attribute = input("Enter the attribute to update (or 'done' to finish): ")
                if attribute == "done":
                    break
                value = input(f"Enter the new value for {attribute}: ")
                new_attributes[attribute] = value

            hr_manager.update_employee(int(employee_id), new_attributes)
            print("Employee information updated successfully.")

        elif choice == "3":
            employee_id = input("Enter the Employee ID to remove: ")
            if not employee_id.isdigit():
                print("Employee ID should be a number.")
                continue

            hr_manager.remove_employee(int(employee_id))
            print("Employee removed successfully.")

        elif choice == "4":
            employee_id = input("Enter the Employee ID to record attendance: ")
            if not employee_id.isdigit():
                print("Employee ID should be a number.")
                continue

            in_time = input("Enter In-Time (HH:MM): ")
            out_time = input("Enter Out-Time (HH:MM): ")
            hr_manager.record_attendance(int(employee_id), in_time, out_time)
            print("Attendance recorded successfully.")

        elif choice == "5":
            employee_id = input("Enter the Employee ID to display attendance: ")
            if not employee_id.isdigit():
                print("Employee ID should be a number.")
                continue

            hr_manager.display_employee_attendance(int(employee_id))

        elif choice == "6":
            employee_id = input("Enter the Employee ID to calculate total working hours: ")
            if not employee_id.isdigit():
                print("Employee ID should be a number.")
                continue

            start_date = input("Enter the start date (YYYY-MM-DD): ")
            end_date = input("Enter the end date (YYYY-MM-DD): ")
            hr_manager.calculate_employee_total_working_hours(int(employee_id), start_date, end_date)

        elif choice == "7":
            print("==============================")
            hr_manager.view_employees()
            # Within your main program, after displaying employee information:
            for employee in hr_manager.employees:
                employee.generate_pay_slip()



        elif choice == "8":
            hr_manager.view_salary_summary()

        elif choice == "9":
            employee_id = input("Enter the Employee ID to generate a payslip: ")
            if not employee_id.isdigit():
                print("Employee ID should be a number.")
                continue

            hr_manager.generate_payslip(int(employee_id))
            print("Payslip generated successfully.")

        elif choice == "10":
            hr_manager.save_all_salary_records_to_json()
            print("Salary records saved to JSON files.")

        elif choice == "11":
            break

if __name__ == "__main__":
    main()