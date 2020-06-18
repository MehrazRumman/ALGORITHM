import sys
sys.setrecursionlimit(9999)


def find_pivot(list1,first,last):
    pivot=list1[first]
    left=first+1
    right=last
    while True:
        while left<=right and list1[left]<=pivot:
            left=left+1
        while left<=right and list1[right]>=pivot:
            right=right-1
        if left> right:
            break
        else:
            list1[left],list1[right]=list1[right],list1[left]
    list1[first],list1[right]=list1[right],list1[first]
    return right
def quick_sort(list1,first,last):
    if first < last:
        p=find_pivot(list1,first,last)
        quick_sort(list1,first,p-1)
        quick_sort(list1,p+1,last)

p=[x for x in range(7000)]
m=len(p)
quick_sort(p,0,m-1)
print(p)

