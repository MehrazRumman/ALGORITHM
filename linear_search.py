def linear_search(list,key):
    list2=[]
    flag=False
    for i in range(len(list)):
        if list[i]==key:
            flag=True
            list2.append(i)
    if flag==True:
            print("found")
            print(list2)
    else:
        print("not found")







p=[x for x in range(999)]
linear_search(p,12)
