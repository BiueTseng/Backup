#1. 物件變數會由類別 copy 一份到每個物件中
#2. 每個物件變數都獨立存在，不會相互影響
#3. 物件變數前面要加 self, 若在方法中沒有加self, 則為區域變數
#4. attribute : 屬性, 也就是物件變數
#5. 凡是能被描述的特性，都叫物件，所以特性，屬性，物件變數，都是指同一個東西(self.XXX)
#6. Java, C#物件變數定義在類別內，只要一new物件，變數就存在
#   但Python一定要執行才會生成  請參考第29行 需要執行第29行才會存在該物件變數(self.speed)
#   Kotlin 取代 Java
###############################################################################
# 變數使用中文的時機
# 1.應付英文不好的人
# 2.專業用詞
class Pokemon():
    def __init__(self): #可以想成寫在__init__ 這區塊內的都是先天的
        print("神奇寶貝出生了")
        self.等級 = 1
        self.level = 1
        speed = 100 #非物件變數，為區域變數
    def setSpeed(self): #寫在__init__以外的都是後天的
        self.speed = 1

p1=Pokemon()
p1.level = 4000
p2=Pokemon()
p2.level = 500
print('p1.level :',p1.level) # "." ->"的"，的意思 => p1的level
print('p2.level:' ,p2.level)
#########################
p1.setSpeed()
p1.speed = 100
print('p1.speed :',p1.speed)
print('p2.speed:' ,p2.speed) #會有 AttributeError 指 p2未定義speed 這物件變數
#print('p1.speed:' ,p1.speed) #會有 AttributeError

