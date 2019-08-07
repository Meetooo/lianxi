# i=0
# while i<10:
#     i=i+1
#     print(i)
#

i,j=1,2

while i<2:
    while i<j:
        print("%d",%(i+1)*j)
        j-=1
    i+=1


print(i,j)