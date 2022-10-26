import random
#錯誤寫法，有機會重複
# ls=[]
# for i in range(7):
#     ls.append(random.randint(1,49))
# print(ls)
nums=set([])
index = 0
while len(nums)<7:
    n=random.randint(1,49)
    nums.add(n) #因為在set下的 .add函數不允許重複內容
    index+=1
    print(f"產生第{index}次 : {n}")
print(nums)