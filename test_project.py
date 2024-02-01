import pytest
from Employee import Employee

# Define a fixture to create a sample employee for testing
@pytest.fixture
def sample_employee():
    return Employee(1, "John", "Doe", "john@example.com", 60000, "Manager")

def test_employee_constructor(sample_employee):
    assert sample_employee.employee_id == 1
    assert sample_employee.first_name == "John"
    assert sample_employee.last_name == "Doe"
    assert sample_employee.email == "john@example.com"
    assert sample_employee.base_annual_salary == 60000
    assert sample_employee.role == "Manager"
    assert sample_employee.allowances == {}
    assert sample_employee.bonuses == 0
    assert sample_employee.deductions == 0
    assert sample_employee.attendance_records == []

def test_employee_set_allowances(sample_employee):
    sample_employee.set_allowances({"housing": 5000, "transportation": 2000})
    assert sample_employee.allowances == {"housing": 5000, "transportation": 2000}

def test_employee_set_bonuses(sample_employee):
    sample_employee.set_bonuses(3000)
    assert sample_employee.bonuses == 3000

def test_employee_set_deductions(sample_employee):
    sample_employee.set_deductions(1000)
    assert sample_employee.deductions == 1000


def test_employee_record_attendance(sample_employee):
    sample_employee.record_attendance("09:00", "17:00")
    assert len(sample_employee.attendance_records) == 1
    assert sample_employee.attendance_records[0] == {"in_time": "09:00", "out_time": "17:00"}

def test_employee_display_attendance(capsys, sample_employee):
    sample_employee.record_attendance("09:00", "17:00")
    sample_employee.display_attendance()
    captured = capsys.readouterr()
    expected_output = "Attendance Records:\nRecord 1: In-Time - 09:00, Out-Time - 17:00\n"
    assert captured.out == expected_output


def test_employee_generate_pay_slip(sample_employee):
    payslip = sample_employee.generate_pay_slip()
    assert "Employee ID: 1" in payslip
    assert "Name: John Doe" in payslip
    assert "Email: john@example.com" in payslip
    assert "Base Annual Salary: $60000" in payslip
    assert "Role: Manager" in payslip

# Run the tests
if __name__ == '__main__':
    pytest.main()
