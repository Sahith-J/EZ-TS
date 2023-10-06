def is_subset_sum(arr, n, target_sum,res):
    if target_sum == 0:
        return True
    if n == 0:
        return False
    if arr[n - 1] > target_sum:
        return is_subset_sum(arr, n - 1, target_sum,res)
    return is_subset_sum(arr, n - 1, target_sum,res) or is_subset_sum(arr, n - 1, target_sum - arr[n - 1],res+[arr[n-1]])

def func(l,target):
    def backtrack(start,sum,subset):
        if sum==target:
            res.append(subset[:])
            return
        if sum>target:
            return
        for i in range(start,len(l)):
            if i>start and l[i]==l[i-1]:
                continue
            if sum+l[i]>target:
                break
            backtrack(i+1,sum+l[i],subset+[l[i]])
    res=[]
    backtrack(0,0,[])
    return res


arr=list(map(int,input().split(" ")))
target_sum=int(input())
n=len(arr)
print(is_subset_sum(arr,n,target_sum,[]))
print(func(arr,target_sum))



