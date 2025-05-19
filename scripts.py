# n=1
# for i in range(1,5):
#     for k in range(1,i+1):
#         print(n,end=' ')
#         n+=1
#     print( )

# n=123456
#
# res=0
# while n>0:
#     dig=n%10
#     res=res*10+dig
#     n=n//10
# print(res)

# n=[12,3,4,6]
# v=lambda x: print("even numers") if x%2==0 else print("odd numers")
# v(n)


# def even(n):
#     if n%2==0:
#         return n
# print(list(filter(even,[2,3,4,5,6,67,8,12])))

# a=10,30,8
# print(a)
# print(type(a))
# n=1
# for i in range(1,5):
#     for k in range(1,i+1):
#         print(n,end=" ")
#         n=n+1
#     print(" ")




import re
# s="haribabu@gmail.com"
# pattern=r"[a-zA-z0-9_\-\>]+[@][a-z]+[\.][a-z]{2,3}"
# s1=re.findall(pattern,s)
# print(s1)


# ? it will return zero or one
# * - it will return zero or more
# * + ->it will return one or more
# s="my naame my is hari123"
# # s1=re.findall(r"\bmy",s)
# # print(len(s1))
# s1=re.findall("naame+",s)
# print(s1)

# s="7916008833"

import re

test_str = '04/01/1997'
# pattern_str = r'^\d{2}/\d{2}/\d{4}$'
#
# if re.match(pattern_str, test_str):
#     print("True")
# else:
#     print("False")


pa_str=r'^[0-9]{2}/[0-9]{2}/[0-9]{4}$'
# if re.match(pa_str,test_str):
#     print("Tru")
# else:
#     print()
# # print(s1)

s1=re.findall(pa_str,test_str)
print(s1)














