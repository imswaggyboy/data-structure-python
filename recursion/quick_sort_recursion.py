def qsort(l):
    if l :
        return qsort([x for x in l[1:] if x < l[0]]) + l[:1] + qsort([x for x in l[1:] if x >= l[0]])
    return []

lst = [1,4,2,5,3,6,3,7,4,0]
qsort(lst)
[0, 1, 2, 3, 3, 4, 4, 5, 6, 7]
type(lst[:1])
<class 'list'>
lst[0]
1
type(lst[0])
<class 'int'>
qsort()
