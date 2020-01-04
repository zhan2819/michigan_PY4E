import re
fd = open('regex_sum_346950.txt')
lst = list()

for line in fd:
    nums = re.findall('[0-9]+',line)
    if(len(nums)==1):
        num1 = int(nums[0])
        lst.append(num1)
    elif(len(nums)==2):
        num2 = int(nums[0])
        num3 = int(nums[1])
        lst.append(num2)
        lst.append(num3)
    elif(len(nums)==3):
        num4 = int(nums[0])
        num5 = int(nums[1])
        num6 = int(nums[2])
        lst.append(num4)
        lst.append(num5)
        lst.append(num6)
s = 0
for num in lst:
    s = s + num
print(s)