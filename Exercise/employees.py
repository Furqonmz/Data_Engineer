employees = [
    {
        "id": "EMP001",
        "name": "Andi",
        "department": "Engineering",
        "status": "Present",
        "working_hours": 8
    },
    {
        "id": "EMP002",
        "name": "Budi",
        "department": "Engineering",
        "status": "Late",
        "working_hours": 7
    },
    {
        "id": "EMP003",
        "name": "Citra",
        "department": "Finance",
        "status": "Present",
        "working_hours": 8
    },
    {
        "id": "EMP004",
        "name": "Dina",
        "department": "Finance",
        "status": "Absent",
        "working_hours": 0
    }
]

class Employee:
  def __init__(self, id, name, department, status, working_hours):
    self.id = id
    self.name = name
    self.department = department
    self.status = status
    self.working_hours =  working_hours

  def display_employee(self):
    print(f"ID : {self.id} | Nama : {self.name} | Department : {self.department} | Status : {self.status}")

class AttendanceProcessor:
  def __init__(self):
    self.employees = []
  def add_employee(self, employee):
    self.employees.append(employee)
  def calculate_total_working_hours(self):
    total = 0
    for employee in self.employees:
      total += employee.working_hours
    return total
  def count_present_employees(self):
    count_present = 0
    for employee in self.employees:
      if employee.status == "Present":
        count_present += 1
    return count_present
  def count_absent_employees(self):
    count_absent = 0
    for employee in self.employees:
      if employee.status == "Absent":
        count_absent += 1
    return count_absent
  def calculate_average_working_hours(self):
    total = self.calculate_total_working_hours()
    return total / len(self.employees)

processor = AttendanceProcessor()
for employee in employees:
  employee_obj = Employee(employee["id"], employee["name"], employee["department"], employee["status"], employee["working_hours"])
  employee_obj.display_employee()
  processor.add_employee(employee_obj)

print(f"Total Working Hours: {processor.calculate_total_working_hours()}")
print(f"Total Present Employees: {processor.count_present_employees()}")
print(f"Total Absent Employees: {processor.count_absent_employees()}")
print(f"Average Working Hours: {processor.calculate_average_working_hours()}")