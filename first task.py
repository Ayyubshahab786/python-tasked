# (1) sConvert Minutes into Seconds
def take_integer(a):
    return a*60
b = take_integer(3)
print(f"the second of is : {b}")
# (2) take lowercase and convert into in upper case and save into dictionary
def take_lower(a):
    c = []
    c.append(a)
    d = {}
    d[a] = a.upper()
    print(c)
    print(d)
take_lower("b")
# (3) Filter out integer from an Array
def filter(list1):
    new = []
    for i in list1:
        if type(i) is int:
            new.append(i)
    return new
listed = filter([2,"shahab","hamza","5",6,7,4])
print(listed)
# (4) Filter out strings from an Array
def fil(list1):
    new = []
    for i in list1:
        if type(i) is str:
            new.append(i)
    return new
print(fil([2,"shahab","hamza","5",6,7,4]))
# (5) Get Student Names
def get_st_name(dic):
    dic1 = []
    for i in dic.values():
        dic1.append(i)
        dic1.sort()

    return dic1
student_name = get_st_name({"st1":"shahab","st2":"hamza","st3":"zubair","st4":"ahmed","st5":"basit"})
print(student_name)
# (6) Secret Society
def s_society_name(g):
    listt = " "
    g.sort()
    for a in g:
        listt +=a[0]
    return listt.upper()
bg = s_society_name(["shahab","zubair","sajid","husnain"])
print(bg)
# Less Than 100?
def less_than(a,b):
    c = a+b
    print(f"sum of {a} and {b} = {c}")
    if c < 100:
        return True
    else:
        return False
print(less_than(15,25))
print(less_than(45,55))
# Find the Smallest Number in a List
def small_no(a):
    a.sort()
    c = []
    for d in a:
        c.append(d)
    return a
    
print(small_no([22,33,44,45,11,10,12,32]))
# Check if an Integer is Divisible By Five
divisible = lambda a:True if a % 5 == 0 else False
print(divisible(10))
print(divisible(225))
# Factorial of a Number
def factorial_no(a):
    res = 1
    for i in range(1,a+1):
    # for res,i in enumerate(range):
         res*=i
        #  1 *1 =1
        #  1 *2 =2
        #  2 *3 =6
        #  6*4=24
        # 24*5=120
    return res
print(factorial_no(5))
def input_user():
    a = input("enter a string or integer")
    if type(a) == int:
        b = int(a)
        print(b)
    else:
        print(a)
input_user()
def int_to_str(integer_input):
    return str(integer_input)
def str_to_int(string_input):
    return int(string_input)
print(int_to_str(3))
print(str_to_int("7"))
# FizzBuzz Interview Question
def fizz_input(a):
    if a%3 == 0 and a % 5 == 0:
         return "FizzBuzz"
    elif a%5 == 0:
        return "Buzz"
    elif a%3 == 0:
        return "Fizz"
    else:
        return str(a)
print(fizz_input(45))

print(fizz_input(9))

print(fizz_input(15))
# calculate commision in sale
def cal_commision():
    a = input("enter a sales")
    f = int(a)
    if f > 100000:
        b = 10 / 100
        c = b * 12000
        d = c + 12000
        return d
    elif f > 150000:
        b = 15 / 100
        c = b * 12000
        d = c + 12000
        return d
    elif f > 200000:
        b = 20 / 100
        c = b * 12000
        d = c + 12000
        return d
    else:
        return "you are not eligible of commision"
print(cal_commision())
print(cal_commision())
# calculate profit of sales
def cal_profit():
    total_sales = int(input("enter a total sales in 1 day: "))
    total_percentage = int(input("enter a total percentage of medicine"))
    percentage = total_percentage / 100
    total_money = percentage * total_sales
    total_investment_in_1_day = total_sales - total_money
    print(total_money)
    print(total_investment_in_1_day)
    expenses = int(input("enter a total expenses"))
    after_expenses = total_money - expenses
    print(f"total expenses is {after_expenses}")
    month = {}
    month["19-02-2020"] = after_expenses
    print(month)
cal_profit()