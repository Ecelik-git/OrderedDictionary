from collections import OrderedDict

N = int(input()) #how many items we need to enter
item_dic= OrderedDict()
for i in range(N):
    #putting input in a list
    item = input().split()
    #price is the last element in item list, banana -->50
    item_Price= int(item[-1])
    #item name is the rest of the item list, if we remove price [:-1]
    item_Name= " ".join(item[:-1])
    if item_dic.get(item_Name):
    #checking if item_Name already exists
       item_dic[item_Name] += item_Price
    else:
       item_dic[item_Name] = item_Price
#printing ordered list
for i in item_dic.keys():
    print(i, item_dic[i])
