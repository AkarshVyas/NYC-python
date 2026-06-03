

# def extragreeting(func):
#     def wrapper():
#         print("hello from the NYC team")
#         func()
#         print("thankyou visit again")
    
#     return wrapper



# @extragreeting
# def greetings():
#     print("good morning")

# greetings()


# def addition(*args):
#     s = 0
#     for i in args:
#         s = s + i
#     return s


# print(addition(20,30,50,39,5,6,78,90))

# def info(**kwargs):
#     return kwargs

# print(info(name = "Akarsh",age = 24,profession = "Data scientist"))



# def extragreeting(func):
#     def wrapper(*args,**kwargs):
#         print("hello from the NYC team")
#         func(*args,**kwargs)
#         print("thankyou visit again")
    
#     return wrapper


# @extragreeting
# def addition(a,b,c):
#     print(a + b + c)

# addition(10,20,30)


# a = 20 

# if a % 2 ==0:
#     print("even number")
# else:
#     print("odd numbers")

# print("even number") if a % 2 == 0 else print("odd number")
#ternary operation 

# a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# b = [i for i in a if i % 2 ==0]

# print(b)


# def check(a):
#     if a % 2 ==0:
#         print("even number")
#     else:
#         print("odd number")

# check(12)

# check = lambda x: "even number" if x % 2 ==0 else "odd number"

# print(check(12))



# addition = lambda a,b : a +b

# print(addition(10,20))

# a = ["Sarthak","harsh","vedant","Akarsh"]

# lengths = list(map(len,a))

# print(lengths)


# temp_cel = [0,20,30,35]

# temp_far = list(map(lambda x : (x * 9/5) + 35 , temp_cel))

# print(temp_far)

# m = [35,80,80,12,60,49]

# passed = list(filter(lambda x : x >= 40,m))

# print(passed)


#zip 

# name = ['sarthak',"Akarsh","harsh","vedant"]

# marks = [12,90,42,6,60]

# result = list(zip(name,marks))

# print(result)

