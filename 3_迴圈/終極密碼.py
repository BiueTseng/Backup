import random
#0<=random.random()<1
# password = random.random() #alt+enter
# print(password)
#
# for i in range(100):
#     password = random.randint(2,99) #有包含上下界
#     print(password)
password = random.randint(2,99)
#print('password: ',password)
max = 100 ; min=1
while True:
    a= eval(input(f'請輸入 {min}~{max}之間的數 :'))
    if a==password:
        print('bingo')
        break
    elif a<password :
        min = a
    else:
        max = a


##################################################
### 確定會跑幾圈，用for
### 不確定會跑幾圈，用while
#########確定#######################################