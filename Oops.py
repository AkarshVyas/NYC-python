# a = 12 
# b = 13 

# print(a + b)

# def addition(a,b):
#     print(a+b)

# addition(12,13)
# addition(12,13)


# class Car:
#     a = 12 #attribute

#     def hello():  #method
#         print("how are you ")

# #you can access attributes and 
# #methods after accessing the class 

# print(Car.a) #accessing attributes 

# Car.hello() # accessing methods 


#objects 

# class Bags:
#     name = "Notyourcollege"
    
#     def details(self):
#         print("hello this is a company who creates bag")

# reebok = Bags()
# campus = Bags()


# print(reebok.name)
# print(campus.name)

# reebok.details()


# class Bags:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips 
#         self.pockets = pockets 

    
# reebok = Bags("leather",3,2)
# campus = Bags("polyster",2,4)


# print(reebok.material)
# print(campus.material)


# class Animal:
#     a = 12  #class attribute 

#     def __init__(self,name):
#         self.name = name  #object/instance attribute 

    
#     def hello(self):  #instance/object method   captures the location of obj
#         print(f"how are you my name is {self.name}")

#     @classmethod
#     def details(cls):  #class method. captures the location of class
#         print(f"how are you my name is {cls.a}")
    
#     @staticmethod
#     def speak():  #tthis is a static method and it will not target any location 
#         print("hello how are you I am a static method")

    

# obj = Animal("lion")


# obj.details()

# class Animal:  #parent class 
#     a = 12
#     def __init__(self,name):
#         self.name =  name 
    
#     def details(self):
#         print(f"hello your name is {self.name}")

# class Humans(Animal): #child class 
#     pass 

# obj = Animal("lion")

# obj2 = Humans("Harsh")

# obj2.details()
# print(obj2.a)

#your child class objects has all the powers to access 
#the attributes and methods of parent class 


#multileavel inheritance

# class BagFactory:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips 
#         self.pockets = pockets

#     def details(self):
#         print("your bag details are :")
#         print(self.material )
#         print(self.zips )
#         print(self.pockets )

# class Reebok(BagFactory):
#     def __init__(self, material, zips, pockets,color):
#         super().__init__(material, zips, pockets)
#         self.color = color
    
#     def details(self):
#         print(self.color)
#         return super().details()

# class Campus(Reebok):
#     def __init__(self, material, zips, pockets, color,):
#         super().__init__(material, zips, pockets, color)


# bag1 = BagFactory("leather",3,4)

# bag2 = Reebok("polyster",4,2)

#multiple inheritance 

# class Animal:
#     def __init__(self,name):
#         self.name = name 
    
# class Humans:
#     def __init__(self,id):
#         self.id = id 

# class Robots(Humans,Animal):
#     def __init__(self, id,name):
#         Humans.__init__(id)
#         Animal.__init__(name)
    
# robo = Robots(12,"akarsh")

#polymorphism

# def hello():
#     print("how are you ")


# def hello():
#     print("what are you doing ")


# hello()

# class animal:
#     def speak(self):
#         print("Animas will not speak ")

# class humans:
#     def speak(self):
#         print("we are humans we can speak")


# obj = animal()
# obj2 = humans()

# obj.speak()
# obj2.speak()

#method overriding (we need inheritance)

# class Animal:
#     a = 12 
#     def __init__(self,name):
#         self.name = name 

#     def details(self):
#         print(f"your name is {self.name}")

# class Humans(Animal):
#     b = 12 
#     def details(self):
#         super().details()
#         print(f"your info is {self.name} and this is all we have ")

# obj = Humans("Harsh")

# obj.details()

#when we are doing inheritance and parent and child classes have same 
#method name so the child class method will override your parent class method 


#method overloading

# class hello:
#     def speak(self,a):
#         print(f"how are you ")
    
#     def speak(self,a,b):
#         print("how are you ")


# class Factory:
#     __name = "kia" #private  class attriute 
#     a = 12 #public class attribute 
#     def __init__(self,type,tyre,color):
#         self.color = color   #public object attribute
#         self.__trye = tyre   #private object attribute 
#         self.type = type  
    
#     def __detail(self): #public method
#         print("hello your details are : ")


# class hello(Factory):
#     print(Factory.__name)



# obj = Factory("sedan","MRF","black")


# class hello:
#     __a = 12 
    
#     @classmethod
#     def info(cls):
#         print(cls.__a)

# obj = hello()

# obj.info()


#abstraction

# from abc import ABC , abstractmethod

# class enforce(ABC):
#     @abstractmethod
#     def enginestart():
#         pass


# class bike(enforce):
#     def enginestart():
#          pass 

# class car(enforce):
#     def enginestart():
#         pass

# class truck(enforce):
#     pass 

# obj1 = bike()
# obj2 = car()
# obj3  = truck()


#dunder methods 

# class Animal:
#     def __init__(self,name):
#         self.name = name 
    
#     def __str__(self):
#         return f"hello my name is {self.name}"

# obj = Animal("Lion") 
# obj2 = Animal("giraffe")
# print(obj2)


# class numbers:
#     def __init__(self,num):
#         self.num = num
    
#     def __add__(self, other):
#         return self.num + other.num

#     def __eq__(self, value):
#         return self.num == value.num
    
# num1 = numbers(30)
# num2 = numbers(30)

# print(num1 + num2)

# print(num1 == num2)

# a = 12 
# b = 12 

# print(a + b)
# print(type(a))

# print(dir(int))

# v = [12,45,78,90]




