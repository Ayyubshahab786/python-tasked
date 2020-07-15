import re
# 1 Find the Odd Integer
def find_odd(lst):
  for i in lst:
    if lst.count(i) % 2 == 1:
        return i
print(find_odd([2,3,2,7,6]))
# Older Than Me
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def compare(self,other):
        if other.age > self.age:
            return other.name + " is older than me"
        elif other.age < self.age:
            return other.name + " is younger than me"
        else:
            return other.name + " and me both has same age"
p1 = Person("shahab",21)
p2 = Person("sajid",21)
p3 = Person("zubair",25)
print(p1.compare(p2))
print(p1.compare(p3))
# Return the Next Number from the Integer Passed
def Next_no(number):
    return number + 1  
print(Next_no(6))    
def even_no_generator(list_even_generator):
    length = len(list_even_generator)
    for loop_list_even in list_even_generator:
        if loop_list_even % 2 == 0 :
            print(f"the even number in list is {loop_list_even}")
even_no_generator([2,4,7])
even_no_generator([1,3,5])

# How Many Vowels?
def take_strings(string):
    vowel = "aeiou"
    count = 0
    for vowelss in string: 
        if vowelss in vowel:
            print(vowelss)
            count += 1
    return count
print(take_strings("shahab ul din "))
# Area of a Triangle                1 first solve without see solution
def take_area(base,height):
    area = (1/2)*(base*height)
    return area
print(take_area(10,20))
print(take_area(10,34))
# Return a String as an integer         2 solve without see solution
def take_ste(a):
    return int(a)
print(take_ste("665"))
# Convert Hours into Seconds            3 solve without see solution
def hours_sec(hrs):
    users = input("enter s if you convert seconds or h if you convert into minutes ")
    if users == "s":
        return (hrs)*(60*60)
    elif users == "h":
        return hrs*60
print(hours_sec(6))
