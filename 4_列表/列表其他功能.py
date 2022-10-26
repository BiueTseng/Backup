planets=['mercury','venus','jupiter']
#附加
planets.append("saturn")
print(planets)
#插入
planets.insert(2,'earth')
print(planets)
planets.insert(3,'mars')
print(planets)
#修改
planets[2] ='hell'
print(planets)
#刪除
planets.pop(2)
print(planets)
#
# #集合中的集合
# math=[ ['thomas',80] , ['kevin',90] , ['tracy',100] ]
# print(math)
# print(math[0])
# print(math[0][0]) #二為list
# for m in math:
#     print(m)




alist = ['d','d',7,5,'d','d',2,1]
print(len(alist))
for i in range(len(alist)-1,-1,-1):
    print(i)
    if alist[i]=='d':
        alist.pop(i)

print(alist)