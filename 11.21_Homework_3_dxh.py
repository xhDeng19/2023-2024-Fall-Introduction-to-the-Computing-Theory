#输出最长的字符长度
def maxlen(str1, str2):
    return len(str1) if len(str1) > len(str2) else len(str2)

#记录前数和后数分别是否为负数，且去除str1和str2的负号
def negative_type(str1, str2):
    NegativeType = 0 #记录前数和后数分别是否为负数：0为前后都是正数,1为只有前数为负数,2为只有后数为负数,3为前后均为负数
    if str1[0] == "-" and str2[0] == "-":
        NegativeType = 3
        str1 = str1[1:]
        str2 = str2[1:]
    elif str1[0] == "-":
        NegativeType = 1
        str1 = str1[1:]
    elif str2[0] == "-":
        NegativeType = 2
        str2 = str2[1:]
    return str1, str2, NegativeType

#去除str1和str2开头的0
def no_zero_begin(str1, str2):
    count1, count2 = 0, 0
    for i in range(len(str1)):
        if str1[i] == "0":
            count1 = i + 1
        else:
            break
    for i in range(len(str2)):
        if str2[i] == "0":
            count2 = i + 1
        else:
            break 
    if str1 == "0": #检测str1和str2是不是本身就是0
        count1 = 0
    if str2 == "0":
        count2 = 0
    return str1[count1:], str2[count2:]

#将字符串倒序转换为数字列表
def string_to_lst(str1, str2, lst1, lst2):
    for i in range(1, len(str1) + 1):
        lst1[i - 1] = int(str1[-i])
    for i in range(1, len(str2) + 1):
        lst2[i - 1] = int(str2[-i])
    return lst1, lst2
    
#两个整数字符串比大小
def IsGreater(str1, str2): #判断前一个整数字符串是否大于于后一个整数字符串
    if len(str1) > len(str2):
        return True
    if len(str1) < len(str2):
        return False
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] > str2[i]: #第一次出现前数比后数大的一位
                return True
            elif str1[i] < str2[i]: #第一次出现前数比后数小的一位
                return False
        return False #两个数相等
    
#将列表转换为字符数组输出
def output_string(ans, isNegative):
    string = [0] * len(ans)
    ZeroBegin = True
    count = 0
    for i in range(1, len(ans) + 1): #将ans列表里的数字转为字符数组，再用join输出字符串
        if ZeroBegin and ans[-i] == 0: #将ans中前面剩余的0去掉
            count += 1
            continue
        string[i - 1] = str(ans[-i])
        ZeroBegin = False
    if count == len(ans): #判断ans是否就是0
        return "0"
    return "-" + "".join(string[count:]) if isNegative else "".join(string[count:])

#-------------------------------------------------------------------------------------------------------------------#

#高精度加法
def add(str1, str2):
    str1, str2, NegativeType = negative_type(str1, str2)
    str1, str2 = no_zero_begin(str1, str2)
    match NegativeType:
        case 0:
            isNegative = False
        case 1:
            return sub(str2, str1)
        case 2:
            return sub(str1, str2)
        case 3:
            isNegative = True
    lst1, lst2 = [0] * maxlen(str1, str2), [0] * maxlen(str1, str2)
    lst1, lst2 = string_to_lst(str1, str2, lst1, lst2)
    ans = [0] * (maxlen(str1, str2) + 1)
    temp = 0
    for i in range(maxlen(str1, str2)):
        t = lst1[i] + lst2[i] + temp
        if t >= 10: #进位检测
            ans[i] = t - 10
            temp = 1
        else:
            ans[i] = t
            temp = 0
    if temp != 0: #判断最高位有无进位
        ans[maxlen(str1, str2)] += temp
    
    return output_string(ans, isNegative)

#高精度减法
def sub(str1, str2):
    str1, str2, NegativeType = negative_type(str1, str2)
    str1, str2 = no_zero_begin(str1, str2)
    match NegativeType:
        case 0:
            if IsGreater(str2, str1): #如果str2大于str1
                str1, str2 = str2, str1
                isNegative = True
            else:
                isNegative = False
        case 1:
            return add("-" + str1, "-" + str2)
        case 2:
            return add(str1, str2)
        case 3:
            return sub(str2, str1)       
    lst1, lst2, ans = [0] * maxlen(str1, str2), [0] * maxlen(str1, str2), [0] * maxlen(str1, str2)
    lst1, lst2 = string_to_lst(str1, str2, lst1, lst2)
    temp = 0
    for i in range(maxlen(str1, str2)):
        t = lst1[i] - lst2[i] - temp
        if t < 0: #借位检测
            ans[i] = 10 + t
            temp = 1
        else:
            ans[i] = t
            temp = 0
    return output_string(ans, isNegative)
     
#高精度乘法
def mul(str1, str2):
    str1, str2, NegativeType = negative_type(str1, str2)
    str1, str2 = no_zero_begin(str1, str2)
    if NegativeType == 0 or NegativeType == 3:
        isNegative = False
    if NegativeType == 1 or NegativeType == 2:
        isNegative = True
    lst1, lst2 = [0] * maxlen(str1, str2), [0] * maxlen(str1, str2)
    lst1, lst2 = string_to_lst(str1, str2, lst1, lst2)
    temp = 0
    ans = [0] * (len(lst2) + len(lst1))
    for i in range(len(lst1)): #lst1与lst2地位对等
        for j in range(len(lst2)):   
            t = lst1[i] * lst2[j] + temp + ans[i + j]       
            if t >= 10: #进位检测
                ans[i + j] = t % 10
                temp = t // 10
            else:
                ans[i + j] = t
                temp = 0
        if temp != 0: #判断一轮的最高位有无进位
            ans[i + len(lst2)] += temp
        temp = 0
    return output_string(ans, isNegative)

#高精度除法
def div(str1, str2): #str1, str2 里均为非负整数
    if str2 == "0":
        return False
    str1, str2 = no_zero_begin(str1, str2)
    ans = [0] * (maxlen(str1, str2) + 1)
    minuend = str1[0 : len(str2)] #被减数
    for i in range(0, len(str1) - len(str2)): #列竖式除法
        while int(sub(minuend, str2)) >= 0:
            ans[i + len(str2)] += 1
            minuend = sub(minuend, str2)
        minuend += str1[i + len(str2)]
    while int(sub(minuend, str2)) >= 0: #最后一次除法单独讨论
        ans[len(str1)] += 1
        minuend = sub(minuend, str2)
    ans.reverse()
    count = 0
    for x in minuend: #消去余数中的前置0
        if x == "0":
            count += 1
        else:
            break
    remainder = "0" if count == len(minuend) else minuend[count:]
    return output_string(ans, False), remainder
    
#高精度？幂运算
def pow(str1, n):
    if n == 0:
        return "1"
    t = pow(str1, n // 2)
    return mul(t, t) if n % 2 == 0 else mul(mul(t, t), str1)

print(pow("-1", 3))
#test1: 
print(add(pow("2", 100), pow("3", 100)))
print(2 ** 100 + 3 ** 100)
#test2: 
print(sub(add(mul("2", "100"), mul("123456", "789")), div("8773849905050505", "123")[0]))
print(2*100 +123456*789-8773849905050505//123)


