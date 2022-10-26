# def add(x,y,z): #自訂函數
#     return x+y+z
#
# def add(*x):#當參數動態變動時，則可以用*x以tuple的方式接收
#     sum = 0
#     for i in x:
#         sum+= i
#     return sum
# z=add(10,20,30,40,55)
# print(z)
#
# m=[10,20,30,40,50,55]
# # z=add(m[0],m[1],m[2],m[3],m[4],m[5])
# #上面太麻煩了，改用下面的
# z=add(*m) #將m list 裡一個一個展開
# print(z)

n = int(input())
for i in range(1, n+1):
    print(i, end="")