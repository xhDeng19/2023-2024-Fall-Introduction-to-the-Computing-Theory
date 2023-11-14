#-----------------1-------------------
def distinct_value(lst):
    lst2 = []
    for x in lst:
        if x not in lst2:
            lst2.append(x)

    lst2.sort(reverse = True) #列表中的元素从大到小排列
    return lst2

lst1 = [3, 2, 1, 4, 2, 3, 5]
print(distinct_value(lst1))

#-----------------2-------------------
str2 = input("uppercase:")

print(str2.upper()) #将字母全都转换为大写

#-----------------3-------------------
def merge(a,b):
    a.extend(b) #将b列表中的元素全部加到a的列表中
    a.sort() #将a列表中的元素按从小到大的顺序排列
    return a

str3_1 = [1, 2, 3]
str3_2 = [-1, 2, 4]

print(merge(str3_1,str3_2))

#-----------------4-------------------
def even_odd(lst):
    odd = 0
    even = 0
    for x in lst:
        if int(x)%2:
            odd += 1
        else:
            even +=  1
    return even, odd

lst4 = [1, 3, 5, 7, 9, 2, 8, 10]
#lst4 = input().split() #输入为一串数字
print(even_odd(lst4))

#-----------------5-------------------
def is_valid(str):
    boolen1 = False
    boolen2 = False
    boolen3 = False
    if 6 <= len(str) <= 16 and (str.count("$") > 0 or str.count("@") > 0 or str.count("#") > 0):
        for x in str:
            if 48 <= ord(x) <= 57: #ASCII码中48代表0，57代表9
                #print("number")
                boolen1 = True
            if "a" <= x <= "z":
                #print("lower")
                boolen2 = True
            if "A" <= x <= "Z":
                #print("upper")
                boolen3 = True
    
    if boolen1 and boolen2 and boolen3:
        return True
    else:
        return False
    
str5 = input("is password valid?")
print(is_valid(str5))

#-----------------6-------------------
def is_vowel(a):
    if a in "aAeEiIoOuU": #直接列出所有可能出现的元音
        return True
    else:
        return False

print(is_vowel("a"))
print(is_vowel("d"))


#-----------------7-------------------
def Month_days(str):
    str = str.lower()
    dic = {"january" : 31, "february" : 28, "march" : 31, "april" : 30, "may" : 31, "june" : 30, "july" : 31,
            "august" : 31, "september" : 30, "october" : 31, "november": 30, "december" : 31} #用字典将月份名称与天分对应起来
    
    return dic[str]

print(Month_days("October"))

#-----------------8-------------------
def is_integer(str):
    return str.isdigit() #用老师ppt上讲的isdigit()函数

str8 = input("is integer?")
print(is_integer(str8))

#-----------------9-------------------
def season(month,day):
    if day >= 21: #按照春分、秋分等划分四季
        month += 1
    
    if 3 < month <= 6:
        return "Spring"
    elif 6 < month <= 9:
        return "Summer"
    elif 9 < month <= 12:
        return "Autumn"
    else:
        return "Winter"
    
print(season(10,24))

#-----------------10-------------------

print("""    
                            ir                   
                        vPMBBDPMPv:               
             ...      vBQDgEUYrrqSSd.             
        ..ir7i:ir:   uBQRgD5X22sUbsPB             
      .5v7ri.:r2vrv::Z7Y2DDRggDggBMgMI    .::     
      d7i:iivjU2Pvri:.iri::.LS1s::i:7S :r7v:i7i   
     Ju:irLuvLv7:.....  .iiivqSY:iii. rjsXXr..:77 
     2PuU5U777i::.:.:::.             ...r5uUL:. r:
      .  Uv1i::i:::::::i:          ......:s7jUi:::
         r5::iiii::::.:.i:        .::...:.:sLKK1I 
         Yiiiiiiii::.:i: r.      .i..:.:::.iqL .. 
        2riiiiiii:::ii:irr:      :r.::::::i.u     
       Iriiiiiiii7jBQY7i:ri     .r::.:r::iiii7    
      JYiiiiiiiiJiQQQ QLi7i     .7irgDiUYiii:j    
     .Sriiiiiiir7 XBQBQji:       7rRBB.Q2vii:Y:   
     :5rriiii:::2  r2KZ:  .::..   LMgQBd.5iiirv   
     iIviiii::..:v:.:i   BQBQQ1BB  J:i: rv:iiis   
     .q77ii::::...:i:     1QBBBQ7   r::r: ::iij   
      JUvvriii::::::  7.    ..    :  :.....:i77   
       SuLYrrii:i:i:  .77ri:..i::r:  ::.:::ii2.   
        u5YYv7rriiii     QQBgBB...   i:i:irLSr    
         :2IUYY7rirr: .  .MPXQ:     :irr7v5qi     
           :71j7rrr77:...  ir.   ..rvsJ5qq7       
               K5Lvrrrr::..   ..:rLIqSI7:         
              jBgDEEqK5XXX2SUU5qXPb:              
             1BX51IXBBBBRusJPMqdQggv              
            :BPX1s7Lssrj:.  .7..71PBU             
            QgqISusi:.iY:...ir..v.iJKv            
           rBDKXSK5Lr7v2rLJIXvruY::irg.           
    .7YYq  dRqEKqXP2vJuvPMBQBBBQujuSZQ            
  ivXv:L   Bbq5bPEdgZPPDPDdZqvj5ZQMQb.            
  Q2i.:i  iQEqK2XKXIDuX2PXdPsJsY7r2UYsi L7s       
 .Er:.:r  7BqPPPSX1I5s215KE5v7U7  7UJuXM. QU      
  21r:ivr  JP5S5qPXPKj5UbZd21 :Pr r115qQL77       
   IKL77jI77LJj2SPbDP5qqPE5IL. J . . 2gB.         
   :S5K5qqI7J7r:::ii7uPKgSKY:. 7I: : EB.          
      .:.   uusi::. :DrrZRbDg: :PUsUZQ5           
            YjIvrrr.:SXK1JMDQQQEZEDEQR            
            :K2Jirir. ......:2IdQBEBXi            
             7KLL77rr::::::ii::.vr .Kvr:rb:       
              Uuirrs2v     1LrrJL:   7gBBB        
               UbKP2::     .QZM1: r                     
      
      """) #狗年标志（迫真

#-----------------11-------------------
def is_LeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0: #判断是否为闰年
        #print("leapyear")
        return True
    else:
        return False

def next_date(year,month,day):
    dic = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31} #将月份和其中的天数对应起来
    if is_LeapYear(year):
        dic[2] = 29 #若为闰年，则2月有29天
        #print(dic)
    
    if dic[month] == day :
        #print("end")
        if month == 12: #12-31
            return str(year+1), "1", "1"
        else: #非12月的最后一天
            return str(year), str(month+1), "1"
    else: #一个月的非最后一天
        return str(year), str(month), str(day+1)

year = int(input("Input a year:"))
month = int(input("Input a month:"))
day = int(input("Input a day:"))

ans = "-".join(next_date(year,month,day)) #用“-”连接
print(f"The next date is [yyyy-mm-dd] {ans}")

#-----------------12-------------------
def words_appeared(lst): #用字典记录列表中单词出现的次数
    dic = {}
    for x in lst:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    return dic

def letters_appeared(str):
    dic = {}
    for x in range(97, 123): #ASCII码中97代表a，122代表z
        dic[chr(x)] = str.count(chr(x)) # x从“a”循环到“z”
    return dic

def speech_function(speech):
    speech_ = speech.replace(',' , '') #删除字符串中的“,”
    speech_ = speech_.replace('--' , '') #删除字符串中的“--”
    speech_ = speech_.replace('.' , '') #删除字符串中的“.”
    speech_lower = speech_.lower()
    #print(speech_lower)
    lst = speech_lower.split()  #将字符串转换为列表
    #print(lst)

    print(words_appeared(lst), end="\n\n")
    print(letters_appeared(speech_lower))

speech_given = "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. \
Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this. \
But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth. \
Abraham Lincoln \
November 19, 1863"

speech_function(speech_given)
