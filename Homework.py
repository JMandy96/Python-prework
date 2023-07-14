#Question 1:
def hello_name(user_name):
    print("hello_"+user_name+"!")
hello_name("USERNAME")

#Question 2:
def first_odds():
    for number in range(1, 100):
        if number % 2 == 1:
            print(number)
        else:
            continue

#question 3:
def max_num_in_a_list(a_list):
    max_number = a_list[0]
    for number in a_list:
        if max_number < number:
            max_number = number
        else:
            continue
    print(max_number)
a_list= [1,7,8,10,9,100,23,54]
max_num_in_a_list(a_list)

#question 4:
def is_leap_year(a_year):
    if a_year % 4 == 0 or a_year % 400 == 0 and a_year % 100 != 0:
        leap_year = True
    else:
        leap_year = False
    return leap_year
print(is_leap_year(2101))
print(type(is_leap_year(2008)))

#question 5:
def is_consecutive(a_list):
    for integer in range(0, len(a_list) -1):
        if a_list[integer + 1 ] != a_list[integer] + 1:
            return False

    return True
a_list = [1, 2, 3, 8, 5]
print(is_consecutive(a_list))
print(type(is_consecutive(a_list)))