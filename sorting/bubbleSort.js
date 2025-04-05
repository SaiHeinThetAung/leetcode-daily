const sorting=(arr)=>{
    const n=arr.length;
    for(i=0;i<n;i++){
        for(j=0;j<n-1-i;j++){
            if(arr[j]>arr[j+1]){
                const temp=arr[j]
                 arr[j]=arr[j+1]
                 arr[j+1]=temp;
            }
        }
    }
    return arr
}
console.log(sorting([6,4,5,0]))