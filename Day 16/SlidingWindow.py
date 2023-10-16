# Sliding Window
# Sum of subarray should be equal to the target
le = list(map(int, input().split()))
target = int(input())
l, r = 0, 0
currsum = 0
res = []

while r <= len(le):
    if currsum == target:
        res.append(le[l:r])
        currsum -= le[l]
        l += 1
    elif currsum < target:
        if r < len(le):
            currsum += le[r]
            r += 1
        else:
            break
    else:
        currsum-= le[l]
        l += 1

print(res)


