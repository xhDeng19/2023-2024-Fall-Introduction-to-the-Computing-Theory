
"""
def minus_matrix(lst,ans,i):

    for x in lst:
        if type(x) != type([]):
            ans[i] = -x
            i += 1

        else:
            return minus_matrix(x,ans,lst.index(x))

    return ans

lst = [1,2,3,[3,5,123]]

ans= [0]*len(lst)
minus_matrix(lst,ans,0)

print(ans)

def Walsh_Hadamard(k):
    if k == 0:
        return 1
    if k == 1:
        return [[1,1],[1,-1]]
    
    return [[Walsh_Hadamard(k-1),Walsh_Hadamard(k-1)],
            [Walsh_Hadamard(k-1),"-"+Walsh_Hadamard(k-1)]]

print(Walsh_Hadamard(3))"""

import copy
#---------------------subset----------------------
def subsets_2(nums):
    res = [[]]
    for num in nums:
        res += [ i + [num] for i in res]
    
    return res

print(subsets_2([1,5,2,4]))
