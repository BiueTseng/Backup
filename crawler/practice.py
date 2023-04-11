"""
>> play = q5(50)
終極密碼: 1~100
>> play.choose(1101)
'僅能輸入範圍內的整數'
>> play.choose(40)
終極密碼: 41~100
>>play.choose(20)
'僅能輸入範圍內的整數'
>>play.choose(50)
'中!'
"""
class q5():
    def __init__(self,set_num =None):
        from random import randint
        self.rand_num = randint(1,100)
        self.upnum = 100
        self.dwnum = 1
        print("終極密碼:" ,self.current_range())
    # 回傳目前的上下限
    def current_range(self):
            pass

        return self.dwnum , self.upnum
    # 印出選字結果
    def choose(self,num):

        return self.current_range()
