company_employees = {}

command = input()

while command != 'End':
    command = command.split(" -> ")
    if command[0] not in company_employees:
        company_employees[command[0]] = []
        company_employees[command[0]].append(command[1])
    else:
        if command[1] not in company_employees[command[0]]:
            company_employees[command[0]].append(command[1])
    command = input()

sorted_company = sorted(company_employees.items(), key=lambda x: x[0])

for (company, employee) in sorted_company:
    print(company)
    for empl in employee:
        print(f"-- {empl}")


