

def Hanoi(lst1,lst2,lst3):
    #dic = {}
    print(lst1,lst2,lst3)
    if 0 not in lst3:
        return True
    index1 = lst1.index(0) - 1
    index2 = lst2.index(0) - 1
    index3 = lst3.index(0) - 1

    if lst3[index3] < lst2[index2] and lst2[index2] < lst1[index1]:
        lst2[index2 + 1] = lst3[index3]
        lst3[index3] = 0
        return Hanoi(lst1,lst2,lst3)

    if lst1[index1] < lst2[index2] and lst2[index2] >= lst3[index3] :
        lst2[index2 + 1] = lst1[index1]
        lst1[index1] = 0
        return Hanoi(lst1,lst2,lst3)
    
    elif lst1[index1] < lst3[index3] and lst2[index2] <= lst3[index3] :
        lst3[index3 + 1] = lst1[index1]
        lst1[index1] = 0
        return Hanoi(lst1,lst2,lst3)
    
    elif lst2[index2] < lst3[index3] and lst2[index2] <= lst1[index1]:
        lst3[index3 + 1] = lst2[index2]
        lst2[index2] = 0
        return Hanoi(lst1,lst2,lst3)
    
    elif lst2[index2] < lst1[index1] and lst3[index3] <= lst1[index1]:
        lst1[index1 + 1] = lst2[index2]
        lst2[index2] = 0
        return Hanoi(lst1,lst2,lst3)

    elif lst3[index3] < lst1[index1] and lst2[index2] <= lst1[index1]:
        lst1[index1 + 1] = lst3[index3]
        lst3[index3] = 0
        return Hanoi(lst1,lst2,lst3)
    
    else:
        lst2[index2 + 1] = lst3[index3]
        lst3[index3] = 0
        return Hanoi(lst1,lst2,lst3)

    print(lst1,lst2,lst3)
    #return Hanoi(lst1,lst2,lst3)
    

lst1 = [8, 7, 6, 5, 4, 3, 2, 1, 0]
lst2 = [10, 0, 0, 0, 0, 0, 0, 0, 0]
lst3 = [10, 0, 0, 0, 0, 0, 0, 0, 0]

lst1_ = [8, 7, 6, 5, 4, 0, 0, 0, 0]
lst2_ = [10, 3, 2, 1, 0, 0, 0, 0, 0]
lst3_ = [10, 0, 0, 0, 0, 0, 0, 0, 0]
Hanoi(lst1_,lst2_,lst3_)
