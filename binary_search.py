def bin_search(lst,value):
    li, hi = 0 , len(lst)-1
    while li<=hi:
        mid = (li+hi)//2
        if lst[mid]<value:
            li = mid +1
        elif lst[mid]>value:
            hi= mid-1
        else:
            return mid
    return -1

l = [0,1,2,3,4,5,6]
x = int(input("Enter the element you want to check!"))

print(bin_search(l,x))
