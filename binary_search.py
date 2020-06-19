def binary_search(list,key):
    high=len(list)-1
    low=0
    found=False
    while low<=high and not found:
        mid=(high+low)//2
        if key==list[mid]:
            found=True
        elif key>list[mid]:
            low=mid+1
        else:
            high=mid-1
    if found==True:
        print("found")
    else :
        print("not found")

l1=[x for x in range(9999999)]
l1.sort()
binary_search(l1,9765555)
