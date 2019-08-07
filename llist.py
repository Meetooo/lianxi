i=0
fish_record = ["1月2日","甲鱼",23,"1月3日","亿鱼",223,"1月4日","甲鱼",45]
for i in range(len(fish_record)):
    if i%3==0:
        print(i)
        print('%s，%s,%d'%(fish_record[i],fish_record[i+1],fish_record[i+2]))
        # i=i+4
# print(fish_record[0])