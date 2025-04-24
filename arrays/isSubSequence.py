def checkifSubString(s,t):
    n=len(s)
    count=0
    for char in t:
        if count<n and s[count]==char:
            count+=1
    return count==n