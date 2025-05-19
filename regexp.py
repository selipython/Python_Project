import re
# verifyinn the emailid
#
# s="kuruaha@gmail.com"
# pattern="[a-zA-Z0-9]+@[a-zA-Z]+\.(com|net)"
# if(re.search(pattern,s)):
#     print("valid email")
# else:
#     print("invalid email")

a="my name is haribabu my age is 25"
v=re.sub(r"[\s+]","",a)

# print(v)

import re
with open("C:\\Users\\Dell\Desktop\\tst.txt","w") as file:
    file.write("12. hllo\n")
    file.write("23. au")
with open("C:/Users/Dell/Desktop/tst.txt","r") as file:
    v=file.read()
    # for i in v:
    v1=re.findall("[0-9]{2}",v)
    print(v1)


