# d = {10:11,20:200,30:300,40:400}

# #vanilla python 

# d[50] = 500 #creating a new key value pair 
# print(d[30]) # 300 - Reading a value 
# d[10] = 100 #updating a key value that already exist 


#methods approach 
# d = {10:100,20:200,30:300,40:400}


# print(d.get(10))
# print(d.items())
# print(d.keys())
# print(d.values())
# # print(d.pop(20))
# # d.popitem()
# print(d.setdefault(60,3000))


# d.update({70:700})

# print(d)


#traversing (loops) 


# d = {10:100,20:200,30:300,40:400}

# for i in d:
#     print(f"key {i} : value {d[i]}")

#questions

# d1 = {"a":10,"b":20,"c":30} 
# d2 = {"c":40,"d":50,"e":60} 

# for i in d2:
#     d1[i] = d2[i]

# print(d1)



# d1 = {"a":10,"b":20,"c":30} 


# sum = 0 

# for i in d1:
#     sum = sum + d1[i]

# print(sum)

# l = ["a","b","a","c","b","a","c","a","b"]

# d = {}

# for i in l:
#     if i in d.keys():
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1

# print(d)



# d1 = {"a":10,"b":20,"c":30} 
# d2 = {"c":40,"d":50,"e":60} 

# for i in d2:
#     if i in d1.keys():
#         d1[i] = d1[i] + d2[i]
#     else:
#         d1[i] = d2[i]

# print(d1)



