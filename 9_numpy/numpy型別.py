import numpy as np
a = np.array([1,2,3,4,5],dtype = np.float32)
print(a)
b = np.zeros([10],dtype = np.int32)
print(b)
# numpy型別
# np.int8 : -128~127
# np.int16 : -32768~32767
# np.int32 : -21億~21億(-2^31~2^31-1)
# np.int64 : -2^63~2^63-1
# np.uint8(0~255),np.uint16(0~65536),np.uint32,np.uint64 : 沒有負數(unsign)
# np.float16, np.float32(精準到小數第7位),np.float64(精準到小數第15數)
# #bool, string
c = np.zeros([10],dtype = np.int8)
print(c.dtype)
c = np.zeros([10],dtype = np.int8)+200
print(c.dtype)