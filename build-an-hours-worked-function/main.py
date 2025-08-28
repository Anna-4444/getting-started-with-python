# Write function here
def calculate_pay(hours_worked, pay_per_hour):
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_pay = 40 * pay_per_hour
        overtime_pay = overtime_hours * pay_per_hour * 2
        return regular_pay + overtime_pay
    else:
        return hours_worked * pay_per_hour

def calculate_monthly_pay(week1_hours, week2_hours, week3_hours, week4_hours, pay_per_hour):
    week1_pay = calculate_pay(week1_hours, pay_per_hour)
    week2_pay = calculate_pay(week2_hours, pay_per_hour)
    week3_pay = calculate_pay(week3_hours, pay_per_hour)
    week4_pay = calculate_pay(week4_hours, pay_per_hour)
    return week1_pay + week2_pay + week3_pay + week4_pay 

# Worked 40 hours at $20 an hour
print(calculate_pay(40, 20))
# Worked 50 hours at $20 an hour
print(calculate_pay(50, 20))
# Worked 40 hours at $12 an hour
print(calculate_pay(40, 12))

print(calculate_monthly_pay(40,50,35,40,50))
