def sumofSubarray(arr):
    s=0
    n=len(arr)
    for i in range(n+1):
        for j in range(i):
            s+=sum(arr[j:i])
    return s
arr=list(map(int,input().split()))
print(sumofSubarray(arr))