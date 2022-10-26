#方法覆蓋 override
#Python 沒有方法重載(overload)
#方法覆蓋發生在父子繼承時，子類別方法跟父類別方法同名稱
#子類別覆蓋父類別方法時，父類別屍骨無存
#若想要在子類別覆蓋方法中調用父類別方法，就要用觀落陰法: super()
class Pokemon():#父類別
    def __init__(self,level):
        self.level = level
    def setSpeed(self,ss):
        self.speed = ss
class Pikachu(Pokemon):
    def setSpeed(self,s): #子類別方法名同於父類別故覆蓋
        print("現在開始設定速度")
        super().setSpeed(s) #參數是用子類別的，再由子類別傳給父類別

p1=Pikachu(1)
print(f"初始速度為:{p1.level}")
p1.level = 99
print(f"升級為 :{p1.level}")
p1.setSpeed(100) #子類別中沒有設定速度
print(p1.speed)  #故會出錯0