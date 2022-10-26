# # break :退出整個迴圈
for i in range(100):
    a=input('請輸入一個數字')
    print(a)
    if a=='q':
        break
# continue : 後面的事情不做 ex: line 9 & 10遇到5的倍數就不執行print()的動作
for i in range(100):
    if i %5==0:
        continue
    print(i)