#统计100内所有的因数、因数梳理、因忽视和 李处挺好粗
count=0
i=100
all_yinshu=""
sum=0
for j in range(1,101):
        if i%j == 0:
            count=count+1
            all_yinshu=all_yinshu+"%d，"%(j)
            sum = sum+j
            # print("%j is yin shu "%(j))
            print("%d is yin shu "%(j))
print("we have %d yin shu here"%(count))
print(all_yinshu)
print("the sum of the num is %d"%(sum))