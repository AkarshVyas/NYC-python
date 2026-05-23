# a = [12,23,45,67,89]

# #ordered nature you can 
# #access any element at any point of time 
# print(a[1])


#mutable nature - you can change any values on your list

# l = [10,22,30,40,50]

# l[1] = 20

# print(l)

#duplicates - you can have duplicate values 

# t = [1,1,1,2,2,2,2,3,3,3,3]

# #traversing on list 

# a = [10,20,30,40,50]

#traversing on values 

# for i in a:
#     print(i)


#traversing on index
# for i in range(0,len(a)):
#     print(f"{i} : {a[i]}")

# a = [10,20,40,50]


# a.append(60) #adds a value to the last spot

# a.insert(2,30) #add values in the middle 


# print(a)


# l = [10,20,55,30,40,55,50]

# l.clear()

# print(l)

# l = [29,45,67,12,90,34]

# l.sort(reverse=True)

# print(l)


# l = [3, -1, 4, -5, 9]

# pos = []
# neg = []

# for i in l:
#     if i >= 0:
#         pos.append(i)
#     else:
#         neg.append(i)

# print(f"your positive elements are {pos}")
# print(f"your negative elements are {neg}")

# l = [10, 20, 30, 40]

# sum = 0 

# for i in l:
#     sum = sum + i

# print(f"your average is {sum/len(l)}")


# a = [20,43,17,100,68,29,90,47]

# largest = a[0]
# index = 0


# for i in range(len(a)):
#     if a[i] > largest:
#         largest = a[i]
#         index = i

# print(f"your largest value is {largest} at index {index}")


# a = [4, 7, 2, 9, 1,8]

# largest = a[0]
# sec_largest = a[0]

# for i in a:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i

# print(sec_largest)



# a = [10,20,30,40,50]

# for i in range(len(a)-1):
#     if a[i] > a[i+1]:
#         print("your list is not sorted")
#         break
# else:
#     print("your list is sorted")

        
    