def mergesort(arr):
    if len(arr) >1:
        mid = len(arr)//2
        left_list = arr[:mid]
        right_list = arr[mid:]
        mergesort(left_list)
        mergesort(right_list)

        i=0
        j=0
        k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]< right_list[j]:
                arr[k] = left_list[i]
                i = i+1
                k = k+1
            else:
                arr[k] = right_list[j]
                j = j+1
                k = k+1


        while i < len(left_list):
            arr[k]=left_list[i]
            i = i+1
            k=k+1
        while j < len(right_list):
            arr[k] = right_list[j]
            j=j+1
            k = k+1


ele = int(input("How many element do you wish to insert?: "))
listt = [int(input()) for x in range(ele)]

mergesort(listt)
print(listt)
