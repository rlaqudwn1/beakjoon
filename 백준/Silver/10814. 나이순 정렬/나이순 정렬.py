n=int(input())
member=[]
for i in range(n):
    age,name= input().split()
    member.append([int(age),name])
member.sort(key=lambda x:x[0])
for i in member:
    print(f"{i[0]} {i[1]}")

    