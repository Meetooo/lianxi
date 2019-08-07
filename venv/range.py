# for i in range(10):
#     if i%2 == 0:
#         print("%d是偶数"%(i))
#
# print("-"*50)
#
# for j in range(1,20,2):
#     print(j)
#
# print("-"*50)

fish_record = '甲鱼80条、乙鱼32条、鱼8条、炼鱼10条'
# nu = 0
# for var in fish_record:
#     if var == "鱼":
#         i=i+1
#     print(i)
nu = 0
for a in range(len(fish_record)):
    if fish_record[a] == "鱼":
        nu = int(fish_record[a+1])+nu
        # return(nu)
# a = len(fish_record)
print(nu)
print(a)
#
# print(a())