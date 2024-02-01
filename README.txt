
HR Management System README

Introduction
============
The HR Management System is a software application prototype designed to facilitate human resource management tasks within an organization. This system allows HR professionals to perform various operations, such as adding and managing employees, recording attendance, calculating total working hours, generating payslips, and more.

Project Structure
=================
The HR Management System consists of several Python files, each with its specific role in the system.

Files:
======
- Director.py: Contains the Director class for employees with the role of Director.
- Employee.py: Core class representing employees with functions for calculating salaries, allowances, and bonuses.
- Manager.py: Contains the Manager class for employees with the role of Manager.
- Intern.py: Designed for employees with the role of Intern.
- HRManager.py: Manages various HR-related tasks, including adding, updating, and removing employees.

How to Use
==========
1. Clone the project repository to your local machine.
2. Ensure Python is installed on your system (the system relies on Python for its functionality).
3. Run the main.py script to launch the HR Management System.
4. Use the interactive menu to perform various HR operations.
5. Options include adding employees, updating information, recording attendance, calculating working hours, and generating payslips.
6. The system provides features to view employee information, salary summaries, and save salary records to JSON files.
7. To exit the system, select the "Exit" option from the menu.

Menu Options
============
The system offers a menu with the following options:
1. Add Employee
2. Update Employee
3. Remove Employee
4. Record Attendance
5. Display Employee Attendance
6. Calculate Total Working Hours
7. View Employees
8. View Salary Summary
9. Generate Payslip
10. Save Salary Records to JSON
11. Exit

Using Text Files
================
To generate and save payslips as text files for each employee ID, you can add a function in your code that creates these text files within the `employees/` directory. Ensure filenames match employee IDs for easy reference.

Using JSON Files
================
To save salary details as JSON files for each employee ID, implement a function in your code that creates and saves JSON files within the `salary_records/` directory. Each JSON file should store comprehensive salary information for a specific employee.

Testing
=======
To ensure the system's functionality and reliability, a test class is provided. This class includes tests for various features of the HR Management System, such as creating employees, recording attendance, calculating salaries, and generating payslips. You can run these tests using the `pytest` framework.

```RUN this in bash
pytest test_project.py
