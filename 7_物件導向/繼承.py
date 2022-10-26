class Pokemon():#父類別
    def __init__(self,level):
        self.level = level
    def setSpeed(self,s):
        self.speed = s

######################################
#若要針對每隻腳撰寫，管理/維護上都很麻煩
# class Pikachu():
#     def __int__(self,level):
#         self.level = level
# class Eve():
#     def __int__(self,level):
#         self.level = level
#######################################
#繼承:
#1.懶，不想重寫
#2.會把父類別的所有方法，都會被繼承
#3.物件變數都是要由物件方法觸發而產生，所以沒有繼承問題
#4.創造出大致上一樣。但其實有些微不同的類別
#5.每個子類別相同的功能，都會在父類別中統一保管
class Pikachu(Pokemon):#子類別
    def lightning(self):#子類別的擴充功能
        print("技能:十萬伏特")
class Eve(Pokemon):#子類別
    def SpeedStar(self):
        print("技能:高速星星")
print("寶可夢 : 皮卡丘")

p1 = Pikachu(10)
p1.setSpeed(100)
print(p1.speed)
print(p1.level)
p1.lightning()
print("寶可夢 : 伊布")
e1=Eve(10)
e1.setSpeed(50)
print(e1.speed)
e1.SpeedStar()