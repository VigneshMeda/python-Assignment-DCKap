a = {}
n = int(input())
exp = input().split()
for i in range(n):
    k = input()
    v = input()
    a.update({k:v})
# print(a)
# print(exp)
keys = list(a.keys())
# print(keys)
res = []
for i in range(len(exp)):
    if exp[i] == "and":
        for i in range(len(keys)):
            if keys[i] in exp:
                res.append(a[keys[i]])
        break
    
    elif exp[i] == "or":
        for i in range(len(keys)):
            if keys[i] in exp:
                res.append(a[keys[i]])
                break

print("".join(res))