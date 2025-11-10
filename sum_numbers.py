
# nums = [1, 2, 3, 4]
# running_sum = []
# total = 0

# for x in nums:
#     total = total + x
#     running_sum.append(total)

# print(running_sum)

a=[1,2,3,4]
s=0
out=[]
for x in a:
    s+=x
    out.append(s)
    print(out)