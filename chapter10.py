# a = 123 
# copy = a 
# rev = 0 

# while a > 0:
#     rev = rev * 10 + a%10 
#     a = a //10 

# if copy == rev:
#     print("palindrome number")
# else:
#     print("not a palindrome")


# def addition(a,b):
#     print(a + b)
    
# addition(20,20)
# addition(50,50)

# def palindrome_checker(a):
#     copy = a 
#     rev = 0 

#     while a > 0:
#         rev = rev * 10 + a%10 
#         a = a //10 

#     if copy == rev:
#         print(f"{copy} is a palindrome number")
#     else:
#         print(f"{copy} is not a palindrome")

# palindrome_checker(121)
# palindrome_checker(456)
# palindrome_checker(324)


#parameters and arguments 
#parameters are the values you accept while 
# calling the function
#arguments are the values you provide to parameters 
# while calling the function

#positional arguments 

# def multiply(a,b,c,d):
#     print(a * b * c * d)

# multiply(5,2,3,6)

#default arguments 

# def addition(a,b,d,c = 12):
#     print(a + b + c + d)

# addition(5,5,5)

#keyword arguments

# def substraction(a,b,c):
#     print(b - a)

# substraction(20,c = 40,b = 34)