def factor(x):
    i=1
    str1=''
    while i < x:
        if x%i==0:
            str1=str1+' '+str(i)
            print("%d is %d yinshu "%(i,x))
        i=i+1
    print(str1)
factor(100)