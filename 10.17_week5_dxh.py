import copy

#-----------------------1-------------------------
def sum_product(lst):
    sum = 0
    product = 1
    for x in lst:
        sum += int(x)
        product *= int(x)

    return sum, product


#lst1 = list(input())
#print(sum_product(lst1))
#print(lst1)
#print(sum(lst1))

#-----------------------2-------------------------
def sort_list(lst1,lst2): #将列表长度按小到大排序
    if len(lst1)<len(lst2):
        return lst1,lst2
    else:
        return lst2,lst1


def compare_list(lst1,lst2):
    if lst1 == lst2: #所给的两个列表相同
        return lst1
    
    lst1,lst2 = sort_list(lst1,lst2)
    #print(lst1,"\n",lst2)
    for x in lst1:
        if x not in lst2:
            return False #如果长度小的列表里面有一个元素不在长度长的列表里，则返回假
    
    return True, lst1

#lst2_1 = list(input("1?"))
#lst2_2 = list(input("2?"))
#print(compare_list(lst2_1,lst2_2))

#-----------------------3-------------------------
def even_digit(inf,sup):
    ans = []
    for i in range(inf,sup+1):
        #print(ans)
        boolen = 1
        lst = list(str(i))
        for x in lst:
            if int(x)%2:
                boolen = 0
        
        if boolen:
            ans.append(lst) #将所有答案加到列表中
            #print(ans)
    
    return ans
    
lst3 = even_digit(1000,3000)

for x in lst3[0]: #先输出列表中的第一位数，防止逗号位置有误
    print(x,end="")

for i in lst3[1:]: #将之后列表中的答案以整数和逗号的形式输出
    print(",",end="")
    for j in i:
        print(j,end="")

print("\n")

#-----------------------4-------------------------
def remove_duplicate(lst):
    ans = []
    for x in lst:
        if x not in ans:
            ans.append(x) #将原列表中不重复的数字移至新列表
    return ans

lst4 = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
print(remove_duplicate(lst4))
print("\n")

#-----------------------5-------------------------
def reverse_integer(num):
    lst = list(str(num))
    if num < 0:
        del lst[0]   #删掉负号
        lst.reverse()
        lst[0:0] = "-" #添加负号
        return lst
    if num > 0:
        lst.reverse()
        return lst
    
lst5 = int(input("integer?"))

for x in reverse_integer(lst5): #输出列表中的元素
    print(x,end="")

print("\n")

#-----------------------6-------------------------
def list_intersection(lst1,lst2):
    ans = []
    for x in lst1: #寻找交集中的元素，只需遍历两个集合中的一个即可
        if x in lst2:
            ans.append(x)
    
    if len(ans):
        return ans
    else:
        print("no intersection")
        return False
    
test1 = [1,2,3,4,5,6,7,8,9]
test2 = [1,3,5,2,10,100000,-1]
test3 = [-1,10,-9]

print(list_intersection(test1,test2))
print(list_intersection(test1,test3))

print("\n")
#-----------------------7-------------------------

def print_star(n):
    ans = []
    lst = []
    for i in range(1,n+1):
        ans.append(["*"]*i)
    
    lst = copy.deepcopy(ans) #deepcopy防止修改ans时lst跟着变
    ans.reverse()
    lst.extend(ans[1:]) #形成对称的列表，且使得拥有最多星星数的行只出现一次

    for x in lst: #输出lst里的元素
        for y in x:
            print(y,end=" ")
        print("\n",end="")


print_star(10)
print("\n",end="")
#-----------------------8-------------------------
def count_digits(n):
    lst = list(str(n))
    lst_int = [int(i) for i in lst]
    ans = []
    #print(lst.count('1'))
    #print(lst)
    for i in range(10): #遍历0-9的所有数字
        ans.append(lst_int.count(i)) #计算该数字在列表中出现的次数
    return ans

print(count_digits(1223334444555556666667777777888888889999999990))
print("\n",end="")

#-----------------------9-------------------------
def sum_of_two(n):
    sum = 0
    for i in range(1,n+1):
        sum += int(float("2"*i)) #利用字符的乘法

    return sum

print(sum_of_two(5))
print("\n")

#----------------------10-------------------------
#多个嵌套数组即为多维矩阵？？
A = [[x for x in range(1,11)]]*10
B = [[x]*10 for x in range(1,11)]

print(A, "\n")
print(B, "\n")

#----------------------11-------------------------
def find_min(lst):
    return lst.index(max(lst)) #找出列表中最大值第一次出现的位置

lst11 = input("12321?")
print(find_min(lst11),"\n")

#----------------------12-------------------------
def is_prime(n):
    not_prime = []
    is_prime = []
    for i in range(2,n//2+1): #寻找n可能能整除的数
        if i not in not_prime: #寻找最小的不在not_prime中的数字：即为素数
            is_prime.append(i) 
            not_prime.extend(x for x in range(i*2,n+1,i)) #筛法除掉非素数
    #print(not_prime)
    #print(is_prime)
    if n in not_prime:
        return False
    else:
        return True

print("Is it a prime number?",is_prime(2023)) #判断2023是否为素数



def find_prime(n):
    not_prime = []
    is_prime = []
    for i in range(2,n//2+1):
        if i not in not_prime: #寻找最小的不在not_prime中的数字：即为素数
            is_prime.append(i) 
            not_prime.extend(x for x in range(i**2,n+1,i)) #筛法除掉非素数
            
            print(i)

    #not_prime.sort()
    #print(not_prime)
    print(is_prime)

find_prime(1000000)
#运行的太慢了