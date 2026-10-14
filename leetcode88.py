nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
x = 0
for i in range(m-1,m+n):
    nums1[i] = nums2[x]
    x = x+1

nums1.sort()

print(nums1)
print(nums2)