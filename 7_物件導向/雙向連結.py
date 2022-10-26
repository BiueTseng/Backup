import random
class Node():
    def __init__(self):
        self.prev = None
        self.next= None
        self.data = 0

random.seed(1)
d = [random.randint(1,100) for i in range(10)]
print(d)
root = Node()
index = root

# index.data = datas[0] #18
# index.next = Node() #0x01.next = 0x02
# index.next.prev = index #0x01.0x02.prev = 0x01
# index = index.next
#
# index.data = datas[1] #73
# index.next = Node() #0x03
# index.next.prev = index #0x02.0x03.prev = 0x02
# index = index.next

for i in range(10):
    index.data = d[i]
    index.next = Node()
    index.next.prev = index
    index = index.next

# 正向列印 :由最前往後執行
index = root
print("正向列印")
while index.next is not None:
    print(index.data)
    index = index.next
print("反向列印")
# 反向列印 :由最後往前執行
while index.next is not None:
    index = index.next
while index.prev is not None:
    print(index.prev.data)
    index = index.prev
