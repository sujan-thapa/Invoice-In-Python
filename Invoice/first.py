import os
file = open("vg.txt","r")
product = file.read()
sth = product.strip()
print(sth)
file.close()
# print(type(product))
# for i in product:
#     print(i)
# dict = {}
def dict1():
    list = sth.split("\n")
    # print(list)
    # global dict
    # print(dict)
    # dict = {} #empty dictionary
    dict = {}
    
    for i in list: #iterating list
        newList = i.split(" ") #splitting list items into new list
        # print(newList)
        dict[newList[0]] = {} #creating nested dictionary 
        dict[newList[0]]["price"] = newList[1]
        dict[newList[0]]["stock"] = newList[2]
    return dict


    