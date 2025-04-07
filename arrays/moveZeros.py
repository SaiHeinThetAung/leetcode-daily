def move(arr):
    left=0
    for r in range(len(arr)):
        if arr[r]!=0:
            arr[left],arr[r]=arr[r],arr[left]
            left+=1
    return        