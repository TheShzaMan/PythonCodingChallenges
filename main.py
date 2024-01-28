"""
hours_worked = 45
pay_rate = 15
reg_hours = 0
ot_pay_rate = pay_rate * 1.5
ot_hours = 0

if (hours_worked > 40): 
    reg_hours= 40
    ot_hours = hours_worked - 40
else:
    reg_hours = hours_worked
    ot_hours =  0

total_pay = reg_hours * pay_rate + ot_hours * ot_pay_rate

print(total_pay)
"""

def filter_list(l):
    filtered_list = [element for element in l if type(element) == int]

    print(filtered_list)
    return filtered_list

filter_list([1, 2, "a", "b"])