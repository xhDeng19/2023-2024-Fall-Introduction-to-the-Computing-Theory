import math
import time
"""
#--------------------1----------------------

def is_triangle(a,b,c):
    if a>0 and b>0 and c>0 and a+b>c and c+a>b and b+c>a and abs(a-b)<c and abs(b-c)<a and abs(c-a)<b: # a，b，c均大于0且满足三角形不等式
        return True
    else:
        return False

print("please input three sides of a triangle")
a1 = float(input("a=?"))
b1 = float(input("b=?"))
c1 = float(input("c=?"))

if(is_triangle(a1,b1,c1)):
    print("your input is correct.\n")
else:
    print("your input is wrong.\n")

#--------------------2----------------------

def delta(a,b,c):
    d = b**2-4*a*c #b方-4ac
    if a == 0:
        if b == 0:
            if c == 0:
                return "infinite" # 0=0 无穷解
            else:
                return "no solution" # 0=-c c不等于0 无解
        else:
            return "1" # bx+c=0 b不等于0 唯一解
    else:
        if d < 0:
            return "no solution" # 二次函数无实数解
        elif d == 0:
            return "1" # 二次函数有唯一实数解
        else:
            return "2" # 二次函数有两个实数解

print("Given a function as 'a*x^2+b*x+c=0', please enter three parameters a, b and c")
a2 = float(input("a=?"))
b2 = float(input("b=?"))
c2 = float(input("c=?"))

print(f"the function's solution: {delta(a2,b2,c2)}.\n")

#--------------------3----------------------

def is_prime(n):
    match n:
        case 1:
            return False
        case 3:
            return True
        case 5:
            return True
        case _:
            if n%2:
                for i in range(3,(n+1)//2): #判断奇数n是否有大于等于3的因子
                    if n%i == 0:
                        return False
                return True   
            else:
                return False
            
a3 = float(input("please enter a natural number:"))
if a3 == int(a3) and a3>0:
    a3 = int(a3)
    if(is_prime(a3)):
        print("yout input is a prime numebr.\n")
    else:
        print("your input is NOT a prime number.\n")
else:
    print("your input is NOT a natural number.\n")

#--------------------4----------------------

def is_palindrome_year(year):
    l = len(str(year))
    #print(l)
    if year//10:
        for i in range(1,l//2+1):
            if not(year//(10**(l-1)) == year%10): #判断year的最后一位数字与最前一位数字是否相同
                return False
            year = year//10 #移除year最后一位数字
            year = year%(10**(l-2)) #移除year最前一位数字
            l -= 2 #year的长度减2
            #print(year)
            if year < 10:
                return True
        return True
    else:
        return True

a4 = int(input("please enter a particular year:"))
if(is_palindrome_year(a4)):
    print("your input is a palindrome year.\n")
else:
    print("your input is NOT a palindrome year.\n")


#--------------------5----------------------
def f(x):
    if x<-2:
        return x**4
    elif x>2:
        return math.e**x
    else:
        return math.sin(x)
    
a5 = float(input("f(x). x=?"))
print(f(a5),"\n")


#--------------------6----------------------
def count_zeros(n): #将末尾0移至前排
    ans = 0
    if n==0: return n
    while(not(n%10)): #一直检测最后一位是否为0
        ans += 1
        n //= 10
    return ans

def inverse(n):
    l = len(str(n))
    ans = 0
    if n//10:
        for i in range(1,l+1):
            ans += (n%10)*(10**(l-1)) #将n的末尾数字移至ans的头部
            #print(ans)
            n = n//10 #移除n的最后一位数字
            #print(n)
            l -= 1 #n的长度减1
        return ans
    else:
        return n
    
a6 = int(input("(20也可转换为02)please input a number x to be inversed:"))
while(a6):
    #if a6 == 0: break
    if a6 == -1:
        a6 = int(input("please input a number x:"))
    elif a6 == abs(a6):
        print(count_zeros(a6)*'0'+str(inverse(a6)),"\n")
    else:
        print("-"+count_zeros(a6)*'0'+str(inverse(-a6)),"\n")
    a6 = int(input("please input a number x:"))
print("\n")

#--------------------7----------------------
def count_zeros(n):
    ans = 0
    while(not(n%10)): #一直检测最后一位是否为0
        ans += 1
        n //= 10
    return ans

a7 = int(input("please enter a positive integer:"))
print(f"there are {count_zeros(a7)} zeros at its end.\n")

#--------------------8----------------------
def Hamming(a,b):
    num = a ^ b
    #print(num)
    return str(bin(num)).count('1') #计算两数异或后1的数量（即两数在对应的二进制表示下，有多少位不同）

print("please enter two integers.")
a8 = int(input("a=?"))
b8 = int(input("b=?"))
print(f"the hamming distance between the two integers is {Hamming(a8,b8)}.\n")
"""
#--------------------9----------------------
def is_valid(n):
    while(not(n==1)):
        if n%2:
            n = n/2
        else:
            n = 3*n+1
    return True

def is_valid_portable(n):
    k = 3
    if((n-1)%k==0 or str(bin(int(n))).count('1')==1): #检测n是否可被表示为3x+1 或者n为2的幂
        #print(n)
        return True
    else:
        while(not(str(bin(int(n))).count('1')==1)): #一直检测n是否为2的幂
            #print(n)
            if n%2==0:
                n = n/2
            else:
                n = k*n+1
        if(str(bin(int(n))).count('1')==1):
            return True
        else:
            return False

a9 = int(input("please input an integer n:"))
if(is_valid(a9)):
    print("it fits the 3n+1 conjecture.\n")
else:
    print("it does NOT fit the 3n+1 conjecture.\n")


print("please wait for about 40s")
boolen = True
upper = 1000000
for i in range(1,upper):
    print(i)
    if(not(is_valid_portable(i))):
        print(f"{i} does NOT fit the 3n+1 conjecture.\n")
        boolen = False

if boolen:
    print("the 3n+1 conjecture is correct for all integers less than 10^6.\n")

"""
#--------------------10----------------------
def China_Remainder_Theorem1(n):
    if n%3 == 2 and n%5 == 3 and n%7 == 2:
        return True
    else:
        return False

def China_Remainder_Theorem2():
    num = 2*70+3*21+2*15
    return num%105

print(f"三人同行七十稀,五树梅花廿一枝,七子团圆正半月,除百零五便得知。答案是{China_Remainder_Theorem2()}。\n")

time.sleep(2) #让子弹飞一会（雾
for i in range(1,100000):
    if(China_Remainder_Theorem1(i)):
        print(i)
print("即为105n+23\n")


#--------------------11----------------------
def factorial(n): #计算n的阶乘
    if n==0:
        return 1
    ans = 1
    for i in range(1,n+1):
        ans*=i
    return ans

def choose(n,k): #计算C(n,k)
    return factorial(n)/(factorial(n-k)*factorial(k))

def Pascal_Triangle(n):
    k = 0
    while(n>k):
        for i in range(k+1):
            print(int(choose(k,i)),end=" ")
        print("\n")
        k+=1

a11 = int(input("please enter the size n of the Pascal Triangle:")) #杨辉三角
Pascal_Triangle(a11)
"""