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

"""
def filter_list(l):
    filtered_list = [element for element in l if type(element) == int]

    print(filtered_list)
    return filtered_list

filter_list([1, 2, "a", "b"])
"""
# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
"""
def high_and_low(numbers):
    nums_as_ints =[int(number) for number in numbers.split()]
   
    print(f"{max(nums_as_ints)} {min(nums_as_ints)}")
    print(nums_as_ints[0], nums_as_ints[-1])
    return (f"{max(nums_as_ints)} {min(nums_as_ints)}")

high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
"""
# Given two integers a and b, which can be positive or negative,
#  find the sum of all the integers between and including them and return it. 
# If the two numbers are equal return a or b.
def get_sum(a,b):
    if a == b: 
        print(a)
    else:
        print(sum(range(a, b + 1)))

get_sum(0, -1)