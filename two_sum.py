# nums = [2, 3, 2, 4, 3, 5, 6]
# target = 4
# result = []

# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             result = [i, j]

# print(result)

a=nums = [2, 7, 11 , 15]
target = 9
ans = None
for i in range(len(a)):
   for j in range(i+1, len(a)):
      if a[i] + a[j] == target:
         ans=[i,j]
         break
      if ans: break
      print(ans)
    
