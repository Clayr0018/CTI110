# Rikira Clay
# April 14, 2025
# P4HW2 – Payroll Calculator with Totals
# This program calculates regular and overtime pay for each employee entered.
# It also prints total values after all employee data has been processed.

# Pseudocode:
# 1. Set total counters to zero
# 2. Use loop to process employee data
# 3. Calculate overtime and regular hours
# 4. Calculate pay and display employee breakdown
# 5. Add values to running totals
# 6. After loop, display totals

# Initialize totals
total_employees = 0
total_overtime = 0.0
total_regular = 0.0
total_gross = 0.0

# Employee #1
employee_name = "Delriana Ayan"
pay_rate = 22.00
hours_worked = 47

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * (pay_rate * 1.5)
gross_pay = regular_pay + overtime_pay

print("--------------------------------------")
print("Employee Name:", employee_name)
print("Hours Worked:", hours_worked)
print("Pay Rate: $", format(pay_rate, ".2f"))
print("Overtime Pay: $", format(overtime_pay, ".2f"))
print("Regular Pay: $", format(regular_pay, ".2f"))
print("Gross Pay: $", format(gross_pay, ".2f"))
print("--------------------------------------")

total_employees = total_employees + 1
total_overtime = total_overtime + overtime_pay
total_regular = total_regular + regular_pay
total_gross = total_gross + gross_pay

# Employee #2
employee_name = "Destyne Asadia"
pay_rate = 18.50
hours_worked = 36

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * (pay_rate * 1.5)
gross_pay = regular_pay + overtime_pay

print("--------------------------------------")
print("Employee Name:", employee_name)
print("Hours Worked:", hours_worked)
print("Pay Rate: $", format(pay_rate, ".2f"))
print("Overtime Pay: $", format(overtime_pay, ".2f"))
print("Regular Pay: $", format(regular_pay, ".2f"))
print("Gross Pay: $", format(gross_pay, ".2f"))
print("--------------------------------------")

total_employees = total_employees + 1
total_overtime = total_overtime + overtime_pay
total_regular = total_regular + regular_pay
total_gross = total_gross + gross_pay

# Totals
print()
print("========== TOTALS ==========")
print("Total employees:", total_employees)
print("Total Overtime Pay: $", format(total_overtime, ".2f"))
print("Total Regular Pay: $", format(total_regular, ".2f"))
print("Total Gross Pay: $", format(total_gross, ".2f"))
print("============================")
