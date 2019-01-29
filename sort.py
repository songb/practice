def merge_sort(num):
    if(len(num) == 1):
        return num
    lst1 = num[:int(len(num)/2)]
    lst2 = num[int(len(num)/2):]
    sl1 = merge_sort(lst1)
    sl2 = merge_sort(lst2)
    r = merge(sl1,sl2)
    return r


def merge(lst1, lst2):
    i=0
    j=0
    r=[]
    while(i<len(lst1) and j<len(lst2)):
        if(lst1[i]<lst2[j]):
            r.append(lst1[i])
            i=i+1
        else:
            r.append(lst2[j])
            j=j+1

    if(i>=len(lst1)):
        r.extend(lst2[j:])
    else:
        r.extend(lst1[i:])

    return r



print(merge_sort([38,27,43,3,9,82,10]))