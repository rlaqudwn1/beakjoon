from itertools import permutations
from itertools import combinations

N = int(input())
def clac(nums,ops):
    cur = nums[0]
    for i, op in enumerate(ops):
        num = nums[i+1]
        if op =='+':
            cur += num
        elif op =='-':
            cur -= num
        elif op =='*':
            cur *= num
        elif op =='/':
            if cur <0:
                cur = -(-cur//num)
            else:
                cur //= num
    return cur
ops=[]
A = list(map(int, input().split()))
nums = list(map(int, input().split()))
symbols = ['+','-','*','/']
max_val = -10**9
min_val = 10**9

for cnt, sym in zip(nums, symbols):
    ops += [sym]*cnt
for p in set(permutations(ops, len(ops))):
    val = clac(A,p)
    max_val = max(max_val,val)
    min_val = min(min_val,val)
print(max_val)
print(min_val)
