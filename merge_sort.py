def merge_sort(list1):


    if len(list1)>1:
        mid=len(list1)//2
        right_list=list1[:mid]
        left_list=list1[mid:]
        merge_sort(right_list)
        merge_sort(left_list)
def merg(i,j,k,left_list,right_list,list1):
        i=0
        j=0
        k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                list1[k]=left_list[i]
                i+=1
                k+=1
            else:
                list1[k]=right_list[j]
                j+=1
                k+=1
def abandan_i(i,left_list,k,list1):
        while i < len(left_list):
            list1[k]=left_list[i]
            i+=1
            k+=1
def abandan_j(j,right_list,k,list1):
        while j<len(right_list):
            list1[k]=right_list[j]
            j+=1
            k+=1




list3=[i for i in range(9999999)]
merge_sort(list3)
print(list3)
