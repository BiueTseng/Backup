#二元樹排序法規則
#左邊小，右邊大
#左中右，中間取值
#經過排序的資料，禁止使用二元樹
#資料越亂，速度越快，資料越整齊，速度越慢
#延伸觀念-->牽扯到資料庫為日記帳最好，盡量避免排序資料
import numpy as np
import time
class Node():
    def __init__(self,d):
        self.data = d
        self.left = None
        self.right = None
def buildBTree(node,d):
    if node is None:
        node=Node(d)
    elif d<node.data:
        node.left = buildBTree(node.left,d)
    else:
        node.right = buildBTree(node.right,d)
    return node
def bs(node):
    if node.left is not None:
        bs(node.left)
    sort_datas.append(node.data)
    if node.right is not None:
        bs(node.right)
np.random.seed(0)
n=10000
datas=np.random.randint(0,10000,n)
print(datas)
root = None
for d in datas:
    root = buildBTree(root,d)

sort_datas=[]

t1=time.time()
bs(root)
t2=time.time()
print(f"總共花{t2-t1}秒")
#print(sort_datas)
