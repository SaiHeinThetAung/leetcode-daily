def product(arr):
    n=len(arr)
    ans=[1]*n
    prefix=1
    for i in range(1,n):
        ans[i]=prefix
        prefix*=arr[i]

    suffix=1
    for i in range(n-2,-1,-1):
        ans[i]*=suffix
        suffix*=arr[i]