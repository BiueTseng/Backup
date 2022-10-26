def add(x,y):
    z=100 #在函數內定義，不是main的z
    print(f'函數中的z: {z}')
    return z

z = 50
k = add(10,20)
print(f'mian 中的z: {z}')
print('############')
def add(x,y):
    # 有golbal時，使用外面的 z
    # 沒有golbal時，產生新的
    global z  #golbal一定要放在函數的第一行
    z = 100   #此時的z為全域變數的z，故在這邊將z值更新為100時，即為更新全域變數的值

    print(f'函數中的z: {z}')
    return z

z = 50
k = add(10,20)
print(f'透過global函數傳回 mian 中的z: {z}')