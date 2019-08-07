fish_record='鲫鱼5条、鲤鱼8条、炼鱼10条、条'
i = 1
for var in fish_record:
    if var == '条':
        print("第"+str(i)+"条鱼")
        i = i + 1