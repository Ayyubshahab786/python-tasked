# area of triangle
tri = lambda base,height: (1/2)*(base*height)
print(tri(5,66))

name =[1,4,5,6]
# map function
square = list(map(lambda a: a**2,name))
print(square)
numbers = [1,3,2,5,6,6,8,9,33,44,57]
even =[]
def is_even():
    for a in numbers:
        if a % 2 == 1:
            even.append(a)

is_even()
print(even)
lisc = []
def square():
    
    for b in name:
        c = b**2
        lisc.append(c)
square()
print(lisc)
# filter function
"""solution simple"""
numbers_list = [1,3,4,5,6,9,7,8,10]
def is_even_2():
    evens = []
    for a in numbers_list:
        if a%2 == 0:
            evens.append(a)
    print(evens)
is_even_2()
"""using filter and lamda"""
is_even_3 = list(filter(lambda a: a % 2 == 0, numbers_list))
print(is_even_3)


# zip function
# example list convert into tuples
user_id = ["user_1","user_2","user_3","user_4",]
user_id_names = ["Shahab","Hamza","wahahb"]
print(tuple(zip(user_id,user_id_names)))
# convert into dictionary
print(dict(zip(user_id,user_id_names))):


