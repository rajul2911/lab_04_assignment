class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, age):
        result = []
        for employee in self.employees:
            if employee.age == age:
                result.append(employee)
        return result

    def search_by_name(self, name):
        result = []
        for employee in self.employees:
            if employee.name.lower() == name.lower():
                result.append(employee)
        return result

    def search_by_salary(self, operator, salary):
        result = []
        if operator == ">":
            for employee in self.employees:
                if employee.salary > salary:
                    result.append(employee)
        elif operator == "<":
            for employee in self.employees:
                if employee.salary < salary:
                    result.append(employee)
        elif operator == ">=":
            for employee in self.employees:
                if employee.salary >= salary:
                    result.append(employee)
        elif operator == "<=":
            for employee in self.employees:
                if employee.salary <= salary:
                    result.append(employee)
        return result

def main():
    print("Rajul Gupta")
    print("E22CSEU1549")
    employee_db = EmployeeDatabase()

    employee_db.add_employee(Employee("161E90", "Raman", 41, 56000))
    employee_db.add_employee(Employee("161F91", "Himadri", 38, 67500))
    employee_db.add_employee(Employee("161F99", "Jaya", 51, 82100))
    employee_db.add_employee(Employee("171E20", "Tejas", 30, 55000))
    employee_db.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Choose search parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    option = int(input("Enter your choice (1/2/3): "))

    if option == 1:
        age = int(input("Enter age to search: "))
        result = employee_db.search_by_age(age)
    elif option == 2:
        name = input("Enter name to search: ")
        result = employee_db.search_by_name(name)
    elif option == 3:
        salary_operator = input("Enter salary operator (> / < / >= / <=): ")
        salary = int(input("Enter salary to search: "))
        result = employee_db.search_by_salary(salary_operator, salary)
    else:
        print("Invalid option")
        return

    if result:
        print("Search Results:")
        for employee in result:
            print(f"Employee ID: {employee.emp_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")
    else:
        print("No matching records found.")

if __name__ == "__main__":
    main()
