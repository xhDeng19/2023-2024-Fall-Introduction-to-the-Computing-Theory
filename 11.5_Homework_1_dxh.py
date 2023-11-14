import math
#1. Tower of Hanoi
print("------------------1------------------")
def hanoi_plus(n, x, y, z):
    global num_moves # record the number of moves
    
    if n == 1: 
        if y == z:   # move the disk between adjacent rods 
            print(f"{x}->{y}")
            num_moves += 1 
        else:
            print(f"{x}->{y}\n{y}->{z}")
            num_moves += 2
        return True # end the recursion
    
    else:   
        #print(n)
        return hanoi_plus(n-1, x, y, z) and hanoi_plus(1, x, y, y) and hanoi_plus(n-1, z, y, x) and hanoi_plus(1, y, z, z) \
                and hanoi_plus(n-1, x, y, z) # (n-1):1->2->3 and (1):1->2 and (n-1):3->2->1 and (1):2->3 and (n-1):1->2->3

num_moves = 0
hanoi_plus(2,"A", "B", "C")
print(f"The total moves are {num_moves}", end="\n------------------2------------------\n")

#2.	The Josephus Problem
#----------------------2.1----------------------
def circle(n):
    lst = [x for x in range(1, n+1)]
    
    count = 1 # simulate the counting process
    lst_index = 1 # record the location of the person about to count
    while(len(lst) != 1):
        if not count % 2: 
            lst.pop(lst_index - 1) # person who announces an even number leaves
            lst_index -= 1 # imagine that the next person moves anti-clockwise
        
        count += 1
        lst_index += 1

        if lst_index > len(lst): # simulate a sequence of people
            lst_index -= len(lst)

    return lst[0]

print(circle(4))

#----------------------2.2----------------------
def Josephus_function_1(n):
    if n == 1:
        return 1 # T(1) = 1
    
    if n % 2:
        return Josephus_function_1((n-1)/2)*2 + 1 # T(2n) = 2T(n) - 1, n >= 1
    else:
        return Josephus_function_1(n/2)*2 - 1 # T(2n+1) = 2T(n) + 1, n >= 1
    
print(Josephus_function_1(4))

#----------------------2.2----------------------
def Josephus_function_2(n):
    m = int(math.log2(n)) # use log2 to calculate m
    #print(m)
    l = n - (2 ** m)
    return 2 * l + 1

print(Josephus_function_2(4), end="\n------------------3------------------\n")

#3.	棋盘问题
def grid_cover(k, i, j):
    global lst, length
    length = 2 ** k
    lst = [[x for x in range(length)] for i in range(length)] #这样定义列表防止内层列表id相同
    #print(lst)
    return grid_cover_recursion(k, i, j, [0, 0]) and check_black_blocks(lst, i, j)


def grid_cover_recursion(k, i, j, top_left): #top_left记录当前棋盘左上角的坐标
    global lst
    #print(top_left)

    if k == 1:
        match i, j:
            case 1, 1: #黑色方块在2*2棋盘的左上角
                #print(top_left)
                lst[top_left[0]][top_left[1]] = 0
                lst[top_left[0]][top_left[1] + 1] = 4
                lst[top_left[0] + 1][top_left[1]] = 4
                lst[top_left[0] + 1][top_left[1] + 1] = 4
                return True
            case 1, 2: #黑色方块在2*2棋盘的右上角
                lst[top_left[0]][top_left[1]] = 3
                lst[top_left[0]][top_left[1] + 1] = 0
                lst[top_left[0] + 1][top_left[1]] = 3
                lst[top_left[0] + 1][top_left[1] + 1] = 3
                #print(lst)
                return True
            case 2, 1: #黑色方块在2*2棋盘的左下角
                lst[top_left[0]][top_left[1]] = 2
                lst[top_left[0]][top_left[1] + 1] = 2
                lst[top_left[0] + 1][top_left[1]] = 0
                lst[top_left[0] + 1][top_left[1] + 1] = 2
                #print(lst)
                return True
            case 2, 2: #黑色方块在2*2棋盘的右下角
                lst[top_left[0]][top_left[1]] = 1
                lst[top_left[0]][top_left[1] + 1] = 1
                lst[top_left[0] + 1][top_left[1]] = 1
                lst[top_left[0] + 1][top_left[1] + 1] = 0
                #print(lst)
                return True
    
    mid = int(2 ** k / 2)

    upper_left_tl = top_left #分割后棋盘左上角的左上坐标
    upper_right_tl = [top_left[0], top_left[1] + mid] #分割后棋盘右上角的左上坐标
    lower_left_tl = [top_left[0] + mid, top_left[1]] #分割后棋盘左下角的左上坐标
    lower_right_tl = [top_left[0] + mid, top_left[1] + mid] #分割后棋盘右下角的左上坐标

    if i <= mid and j <= mid: #黑色方块在左上角
        return grid_cover_recursion(k-1, i, j, upper_left_tl) and grid_cover_recursion(k-1, mid, 1, upper_right_tl) and grid_cover_recursion(k-1, 1, mid, lower_left_tl) and grid_cover_recursion(k-1, 1, 1, lower_right_tl) 
    if i <= mid and j > mid: #黑色方块在右上角
        return grid_cover_recursion(k-1, mid, mid, upper_left_tl) and grid_cover_recursion(k-1, i, j - mid, upper_right_tl) and grid_cover_recursion(k-1, 1, mid, lower_left_tl) and grid_cover_recursion(k-1, 1, 1, lower_right_tl) 
    if i > mid and j <= mid: #黑色方块在左下角
        return grid_cover_recursion(k-1, mid, mid, upper_left_tl) and grid_cover_recursion(k-1, mid, 1, upper_right_tl) and grid_cover_recursion(k-1, i - mid, j, lower_left_tl) and grid_cover_recursion(k-1, 1, 1, lower_right_tl)
    else: #黑色方块在右下角
        return grid_cover_recursion(k-1, mid, mid, upper_left_tl) and grid_cover_recursion(k-1, mid, 1, upper_right_tl) and grid_cover_recursion(k-1, 1, mid, lower_left_tl) and grid_cover_recursion(k-1, i - mid, j - mid, lower_right_tl)
    
#print(lst)
def check_black_blocks(lst, i_Bblock, j_Bblock): #把之前假设的特殊方块变成L型牌
    #print(lst, length)
    lst[i_Bblock - 1][j_Bblock - 1] = -1 #先将给定的黑色方块与假设的特殊方块区分开
    for i in range(length - 1):
        for j in range(length):
            #print(lst[i][j])
            if lst[i][j] == 0 and j < length - 1: #遍历检测0
                if lst[i+1][j] == 0 and lst[i][j+1] == 0: #1型L牌
                    lst[i][j], lst[i+1][j], lst[i][j+1] = 1, 1, 1
                elif lst[i][j+1] == 0 and lst[i][j+1] == 0: #2型L牌
                    lst[i][j], lst[i+1][j+1], lst[i][j+1] = 2, 2, 2
                elif lst[i+1][j] == 0 and lst[i+1][j+1] == 0: #3型L牌
                    lst[i+1][j], lst[i+1][j+1], lst[i][j] = 3, 3, 3
                else: #4型L牌
                    lst[i][j], lst[i+1][j], lst[i+1][j-1] = 4, 4, 4

            elif lst[i][j] == 0: #0出现在最后一列，只能为4型L牌
                lst[i][j], lst[i+1][j], lst[i+1][j-1] = 4, 4, 4
    lst[i_Bblock - 1][j_Bblock - 1] = 0
    return

grid_cover(2, 3, 3)

#按格式输出棋盘：
print("[", end="")
for x in lst[:-1]:
    print(x, end=",\n ")
print(lst[-1], end="]")




            

