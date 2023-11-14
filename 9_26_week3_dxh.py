import math

#------------------------------1---------------------------------

a = float(input("a=?"))
b = float(input("b=?"))
c = float(input("c=?"))

print(f"int: {int(a)}, {int(b)}, {int(c)}") #转换为int
print(f"float: {float(a)}, {float(b)}, {float(c)}\n") #转换为float


#------------------------------2---------------------------------

def triangle(a,b,c): #定义triangle函数, 用三边计算三角形内各项数值
    p = (a+b+c)/2
    S = (p*(p-a)*(p-b)*(p-c))**0.5 #三角形面积
    print(f"S = {S:.3}")
    
    sinA = S/(0.5*b*c)
    sinB = S/(0.5*a*c)
    sinC = S/(0.5*a*b)
    print(f"A = {math.asin(sinA):.3}, B = {math.asin(sinB):.3}, C = {math.asin(sinC):.3}") #三个角的弧度制

    circumscribed_circle_r = (a/sinA)/2 #正弦定理计算外接圆半径
    cirS = math.pi*(circumscribed_circle_r**2) 
    print(f"外接圆半径为 {circumscribed_circle_r:.3}, 外接圆面积为 {cirS:.3}")
    
    inscribed_circle_r = (2*S)/(a+b+c) #公式计算内切圆半径
    insS = math.pi*(inscribed_circle_r**2)
    print(f"内切圆半径为 {inscribed_circle_r:.3}, 内切圆面积为 {insS:.3}\n")

def is_tri(a,b,c): #判断输入的三个数是否满足三角形三边的条件
    if a<=0 or b<=0 or c<=0:
        return  False
    elif(a+b<=c) or (a+c<=b) or (b+c<=a) or (abs(a-b)>=c) or (abs(b-c)>=a) or (abs(c-a)>=b):
        return False
    else:
        return True



print("please input three sides of a triangle.")   #输入三角形三边
tri_a = float(input("a=?"))
tri_b = float(input("b=?"))
tri_c = float(input("c=?"))


if is_tri(tri_a,tri_b,tri_c):  #判断是否能组成三角形，并输出三角形的各项数值
    triangle(tri_a,tri_b,tri_c)
else:
    print("it's not a correct triangle.\n")



#------------------------------3---------------------------------

math_exp = input("please input a math expression: ")
print(f"{math_exp} = {eval(math_exp)}\n") #计算出数学表达式的结果


#------------------------------4---------------------------------

def swap(a,b): #交换两数
    temp = a
    a = b
    b = temp
    return a,b

print("please enter two numbers.")
x = float(input("x=?"))
y = float(input("y=?"))

x,y = swap(x,y)
print(f"\nx = {x}, y = {y}\nthe first number minus the second number equals {y-x}\n")#交换两数，并输出第一个数与第二个数的差


#------------------------------6---------------------------------
#（实则已经在第二题做过了）

def area(a,b,c):   #三角形面积
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5

def angle(a,b,c):  #三角形三个角的弧度制
    cosA = (b**2+c**2-a**2)/(2*b*c)
    cosB = (a**2+c**2-b**2)/(2*a*c)
    cosC = (b**2+a**2-c**2)/(2*b*a)
    return math.acos(cosA),math.acos(cosB),math.acos(cosC)

def circumcircle(a,b,c):  #三角形外接圆
    cosA = (b**2+c**2-a**2)/(2*b*c)
    A = math.acos(cosA)
    r = (a/math.sin(A))/2
    S = math.pi*(r**2)
    return r,S

def incircle(a,b,c):  #三角形内切圆
    p = (a+b+c)/2
    triS = (p*(p-a)*(p-b)*(p-c))**0.5
    r = (2*triS)/(a+b+c)
    S = math.pi*(r**2)
    return r,S


print("enter three sides of a triangle.")
ta = float(input("a=?"))
tb = float(input("b=?"))
tc = float(input("c=?"))

# 输出函数
if is_tri(ta,tb,tc):
    print(f"\narea: {area(ta,tb,tc)}\nangle: {angle(ta,tb,tc)}\ncircumcircle: {circumcircle(ta,tb,tc)}\nincirlce: {incircle(ta,tb,tc)}\n")
else:
    print("please construct a correct circle\n")


#------------------------------7---------------------------------

def cir_point(x1,y1,r1,x2,y2,r2):
    lenth = ((x1-x2)**2+(y1-y2)**2)**0.5 #两个原点间的距离
    if lenth > r1+r2:     #外离
        return 0
    elif lenth == r1+r2:     #外切
        return 1
    elif lenth < r1+r2 and lenth > abs(r1-r2):     #相交
        return 2
    elif lenth == abs(r1-r2):     #内切
        return 1
    else:     #内含
        return 0

def is_cir(r1,r2): #判断输入的是否为两个圆
    if r1>0 and r2>0:
        return True
    else:
        return False


print("please input two circles' circle points (x1,y1),(x2,y2), and their radii r1,r2")
x1 = float(input("x1=?"))
y1 = float(input("y1=?"))
r1 = float(input("r1=?"))
x2 = float(input("x2=?"))
y2 = float(input("y2=?"))
r2 = float(input("r2=?"))

if is_cir(r1,r2):
    print(f"the number of their intersection point is {cir_point(x1,y1,r1,x2,y2,r2)}")
else:
    print("they're not two correct circles.")