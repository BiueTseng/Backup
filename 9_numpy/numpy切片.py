import cv2
import numpy as np
import pylab as plt
img = cv2.imdecode(np.fromfile("D:/生物/圖片/大阪第二天.jpg", dtype=np.uint8), cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, (768, 580), interpolation=cv2.INTER_LINEAR)
print(img.shape)
#         由上而下,由左而右, RGB顏色全都要
# img=img[ 400:  , 400:  ,  :  ]
img=img[:,:,::-1] # BGR 2 RGB   -1為反向選取
#img=img[...,::-1].copy() #...為前面設定都取  | # cv2.cvtColor()使用深度 copy
#img[第0維全部,第1維全部,第2維全部但反向]

plt.imshow(img)
#cv2.imshow("大阪第二天",img)
#cv2.waitKey(0)

plt.axis("off")
plt.show()


# #一維的切片方式
# a=np.array([0,1,2,3,4,5,6,11,12,45,78,45,1,528,4,1,8,21,5,6])
# print(a.shape)
# print(a[3:-1]) #此時-1跟6的用法就有差
# #二維的切片方式
# b=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(b)
# #b[第0維起始:第0維結束  , 第1維起始:第1維結束  ,第2維起始:第2維結束]
# c=b[1:, 1:-1]
# print(c)

d=np.array([1,2,3,4,5])
#e=d[2:]
e=d[2:].copy() #深度copy，拷貝新的一份，到其他記憶體，比較浪費空間
e[0]=100
print(d)
print(e)






