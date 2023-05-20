c = int(input())
arr = [0,1]
for i in range(c-1):
    arr.append(arr[i] + arr[i+1])
print(arr[-1])