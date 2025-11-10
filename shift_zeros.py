# nums = [0, 1, 0, 3, 12]
# out = []

# # Step 1: Add all non-zero numbers first
# for x in nums:
#     if x != 0:
#         out.append(x)

# # Step 2: Count how many zeroes and add them at the end
# for x in nums:
#     if x == 0:
#         out.append(x)

# print(out)

a=[0,3,0,5,7,0,12]
out=[]
zeros=0
for x in a:
   if x ==0:
     zeros +=1
   else:
     out.append(x)
   
for i in range(zeros):
      out.append(0)

print(out)