list1=[2, 3, 1, 9, 5, 4, 7, 8]
def bubble_sort(list1):
    i=len(list1)-1
    sorted=False

    while not sorted:
        sorted=True
        for j in range(0, i):
            if list1[j]>list1[j+1]:
                sorted=False
                list1[j],list1[j+1]=list1[j+1], list1[j]

    return list1

print(bubble_sort(list1))



def binary_search(A,val):
    N=len(A)
    result=False
    first=0
    last=N-1
    pos=-1
    while first<=last:
        middle=(first+last)//2
        if val==A[middle]:
            result = True
            pos=middle
            break
        elif val>A[middle]:
            first = middle + 1
        else:
            last=middle-1

    if result==True:
        print('Value found')
        return pos
    else:
        print('Value not found')
        return -1

print(binary_search(list1, 9))





