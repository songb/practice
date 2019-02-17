def merge_sort(num):
    if (len(num) == 1):
        return num
    lst1 = num[:int(len(num) / 2)]
    lst2 = num[int(len(num) / 2):]
    sl1 = merge_sort(lst1)
    sl2 = merge_sort(lst2)
    r = merge(sl1, sl2)
    return r


def merge(lst1, lst2):
    i = 0
    j = 0
    r = []
    while (i < len(lst1) and j < len(lst2)):
        if (lst1[i] < lst2[j]):
            r.append(lst1[i])
            i = i + 1
        else:
            r.append(lst2[j])
            j = j + 1

    if (i >= len(lst1)):
        r.extend(lst2[j:])
    else:
        r.extend(lst1[i:])

    return r


print(merge_sort([38, 27, 43, 3, 9, 82, 10]))


def partition(num, low, high):
    pivot = num[low]
    i = low + 1
    j = high
    while (i < j):
        if (num[i] < pivot):
            i = i + 1
            continue

        if (num[j] >= pivot):
            j = j - 1
            continue

        s = num[i]
        num[i] = num[j]
        num[j] = s
        i=i+1
        j=j-1


    if(pivot>num[i]):
        swap = i
    else:
        swap = i-1
    num[low] = num[swap]
    num[swap] = pivot
    return swap


def quick_sort(arr, low, high):
    if(low<high):
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


a=[45, 80, 30, 90, 40, 50, 70]
quick_sort(a, 0, 6)
print(a)


def maxProfit(prices):
    max_profit=0
    for i in range(1, len(prices)):
        p = prices[i]-prices[i-1]
        if p>0:
            max_profit=max_profit+p

    return max_profit