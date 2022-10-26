#父子類別的建構子都是同名稱__init__，所以一定會覆蓋，除非子類別不寫建構子
###底下為區別 Java 的觀念
#public class Pokemon{
#   public pokemon(){
#   }
# }
#class Pikachu extends Pokemon{
#   public Pikachu(){
#       super()# 自動加入
#   }
# }
#因為 Java 會自動在子類別加上 super，
#所以建議在 Python中最好，讓父子有關聯
class Pokemon():#父類別
    def __init__(self,level):
        self.level = level
class Pikachu(Pokemon):
    def __init__(self):
        print("皮卡丘出生了")
        super().__init__(10)
p1=Pikachu()

print(p1.level)

#以上說明，每次看的時候，感覺不一樣，大概會經過3~4次，才會定型