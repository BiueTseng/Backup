'''
時間的微觀                        單位       代碼
1秒 = 1,000 ms(豪秒)          thousand(千)   K
    = 1,000,000 (mu)s(微秒)   million(百萬)  m (大陸用語 兆)
    = 1,000,000,000 ns(奈秒)  billion(十億)  g
p.s.大陸 : 1000M : 1000兆

CPU : 1GHZ : 表示 1 秒鐘會執行10億個指令
              mov ax , 1   <--為一個指令
              mov bx , 2   <--為一個指令
              inc cx , ax, bx <--為一個指令
              mov ax , cx   <--為一個指令

              1個指令需花費: 1 /10億 (秒) = 1奈秒
'''
import time

t1=time.time()
for i in range(1_000_000):
    pass
t2=time.time()
print(f'總花費 : {t2-t1}秒')