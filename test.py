# print("Hello World")

x = 1
# x = 2.0
# y = 1
# x = "This is a string"

# x = True
# x = False

# def fun(a, b, c=False):
#     # print(a)
#     if a == 2:
#         print("True")
#     elif b == 1:
#         print("Won")
#     else:
#         print(c)

# fun(c=5,b=3,a=4)
# fun(4,3,5)

a = [1,2,3,4,5]
# print(a)
# c = 0
# while c < len(a):
#     a[c]+=1
#     c+=1
# for i in range(1,len(a),2):
#     a[i]+=1
# # print(a)

# # f = open("Dockerfile","r")
# # for line in f:
# #     if "RUN" in line:
# #         print(line)

# a.append("6")
# a += ["7"]
# a.insert(0,"8")
# a = ["9"] + a
# for i in range(len(a)):
#     # a[i]=str(a[i])
#     i = a[i]
#     # if isinstance(i,str):
#     #     print(f"{i} is a string")
#     # else:
#     #     print(f"{i} is a not a string")
#     try:
#         y = i+"bob" #lazy string check
#         print(f"{i} is a string")
#     except Exception as e: # bad practice
#         print(f"{e} is my exception")

# print(a)

d = {"key2":"value2"}
d["key"]="value"
d["key"]+=" some string"
d["key3"]={}
d["key4"]=[3,4,5,6]
d["comments"]=[]
d["comments"]+=[{
    "author":"Bryan",
    "comment":"Dictionarys are cool"
}]
print(d)

# print(x)