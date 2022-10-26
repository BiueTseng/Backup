#from 目錄.檔案名 import 類別名稱
#只需要import該class名稱，就可以調用裡面所有的類別方法
#方便程式設計師開發時，統合/整理/分類 /針對模組方法的呼叫
from sdk.BiueSdk import MathSdk
print(MathSdk.triangle(3,4))
from sdk.BiueSdk import PhysicsSdk
print(PhysicsSdk.tp(10000))

#函式庫"無法"做歸納/整理/分類/針對模組方法的呼叫
# from sdk.BiueSdk import *
from sdk.BiueSdk import triangle
from sdk.BiueSdk import tp
print(triangle(4,5))
print(tp(10000))