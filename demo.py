'''
input : list[str]
output :list[list[]]
 each list : 3 to 5
'''

# input = [a,b,c,d,e]
# example output : a,b,c ,.. so on

def groups(list):
    #basic
    if not list:
         return [[]]

    n = len(list)
    start = 0
    end = n
    window_size = 3
    ans = []
    while start < end:
        int_ans = list[start:start+window_size]
        ans.append(int_ans)
        if start + window_size < n:
            start += window_size
        else:
            break

    return ans


print (groups(['a','b','c','d','e']))