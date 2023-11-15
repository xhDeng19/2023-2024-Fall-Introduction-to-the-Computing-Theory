import time
#1. Brute Force
def find_prime_BruteForce(n):
    time_start = time.time()
    number_pn = 0
    boolen = 1

    for x in range(2, n+1):
        for i in range(2, x):
            if not x % i: #如果i为x的因子
                boolen = 0 #x不为素数
                break

        if boolen:
            #print(x)
            number_pn += 1 #素数数量+1
        boolen = 1

    time_end = time.time()
    return time_end - time_start, number_pn

#2. Optimize Brute Force
def find_prime_BruteForceOptimize(n):
    time_start = time.time()
    number_pn = 0
    boolen = 1

    for x in range(2, n+1):
        mid = int(x ** 0.5) 
        for i in range(2, mid + 1): #让i从2到√x中遍历
            if not x % i: #如果i为x的因子
                boolen = 0 #x不为素数
                break

        if boolen:
            #print(x)
            number_pn += 1 #素数数量+1
        boolen = 1

    time_end = time.time()
    return time_end - time_start, number_pn

#3. Optimize Factor
def find_prime_BruteForce_FactorOptimize(n):
    time_start = time.time()
    number_pn = 0
    boolen = 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    
    number_pn += 2 #2, 3为所有小于5的素数
    #6k-1:
    for x in range(5, n+1, 6):
        mid = int(x ** 0.5) 
        for i in range(2, mid + 1, ): #让i从2到√x中遍历
            if not x % i: #如果i为x的因子
                boolen = 0 #x不为素数
                break

        if boolen:
            #print(x)
            number_pn += 1 #素数数量+1
        boolen = 1

    #6k+1:
    for x in range(7, n+1, 6): 
        mid = int(x ** 0.5) 
        for i in range(2, mid + 1, ): #让i从2到√x中遍历
            if not x % i: #如果i为x的因子
                boolen = 0 #x不为素数
                break

        if boolen:
            #print(x)
            number_pn += 1 #素数数量+1
        boolen = 1

    time_end = time.time()
    return time_end - time_start, number_pn

#4. Sieve of Eratosthenes 筛法
def find_prime_Eratosthenes(n):
    time_start = time.time()
    number_pn = 0
    prime_number_lst = [1] * (n + 1) #以列表坐标确定数字，用空间换时间
    prime_number_lst[0], prime_number_lst[1] = 0, 0

    for i in range(len(prime_number_lst)):
        if prime_number_lst[i] == 1:
            number_pn += 1 #素数数量+1
            for j in range(i * i, len(prime_number_lst), i): #以i*i为起点，i为步长确定非素数
                prime_number_lst[j] = 0
    
    time_end = time.time()
    return time_end - time_start, number_pn

#5. Miller-Rabin 素数判定
def is_prime(n): #用来对照Miller-Rabin素数判定的速度
    time_start = time.time()
    if n < 2:
        time_end = time.time()
        return time_end - time_start, False
    
    for x in range(2, int(n ** 0.5) + 1):
        if not n % x:
            time_end = time.time()
            return time_end - time_start, False
    
    time_end = time.time()    
    return time_end - time_start, True

def is_prime_Miller_Rabin(n):
    time_start = time.time()
    lst = [2, 3, 5, 7] # a的取值
    a_total = len(lst)
    boolen = 1

    if n <= 3 or not n % 2: # 特判n小于等于3的情况
        time_end = time.time()
        return time_end - time_start, n == 2 or n == 3
    if n in lst: # a的取值均为素数，特判n等于a的情况（Miller-Rabin要求a与n互质）
        count += 1
        time_end = time.time()
        return time_end - time_start, True
    
    u = n - 1
    t = 0
    while(u % 2 == 0): # n - 1 = u * (2 ^ t)
        t += 1
        u //= 2
    
    for a in lst:
        for i in range(t + 1):
            power = pow(2, i) * u
            power = int(power)
            num = pow(a, power, n)
            if (num ** 2) % n == 1:
                if num == 1 or num == n - 1:
                    if boolen != a_total: #a的其中一个取值正确
                        boolen += 1
                        break
                    else: # a的所有取值均正确
                        time_end = time.time()
                        return time_end - time_start, True
                else:
                    time_end = time.time()
                    return time_end - time_start, False

    time_end = time.time()
    return time_end - time_start, False

print(find_prime_BruteForce(1000000)) #long, long time……

print(find_prime_BruteForceOptimize(1000000)) #quicker

print(find_prime_BruteForce_FactorOptimize(1000000)) #a little quicker than the former

print(find_prime_Eratosthenes(1000000), end="\n\n") #WOW

num = 9999999900000001
print(f"is_prime function: {is_prime(num)}")
print(f"is_prime_Miller_Rabin function: {is_prime_Miller_Rabin(num)}") #When the prime number is quite large, Miller-Rabin primality test is very efficient.



