#定義 def
# def 函數名(參數1,參數2,參數3,...) :
#    pass要內縮
def add(x,y):
    print(x+y)
def bubble_sort(x,y):
    pass #todo

#程式進入點，由此開始 : 呼叫函數
#當程式碼太長時，方便維護使用
if  __name__=='__main__':
    add(110,10)

# 無法在第一個位置的形式參數有預設值，
# def demo(a=10,b,c):
#     print(a,b,c)

# if __name__=='__main__':
#     N = int(input())
#     input_list = []
#     for _ in range(N):
#         commends =  input().split()
#         #print(type(int(commends[1])))
#         if len(commends) <= 3:
#             if commends[0] == 'insert':
#                 input_list.insert(int(commends[1]),int(commends[2]))
#             elif commends[0] == 'remove':
#                 input_list.remove(int(commends[1]))
#             elif commends[0] == 'append':
#                 input_list.append(int(commends[1]))
#             elif commends[0] == 'sort':
#                 input_list.sort()
#             elif commends[0] == 'pop':
#                 input_list.pop()
#             elif commends[0] == 'reverse':
#                 input_list.reverse()
#             elif commends[0] == 'print':
#                 print(input_list)
#         else:
#             print("input out of range")
#         #print(len(commends))

####################高級寫法 一 ############################
# if __name__ == '__main__':
#     arr = []
#     function_dictionary = {
#         "insert": lambda i,e: arr.insert(int(i), int(e)),
#         "print": lambda : print(arr),
#         "remove": lambda x: arr.remove(int(x)),
#         "append": lambda x: arr.append(int(x)),
#         "sort": lambda : arr.sort(),
#         "pop": lambda : arr.pop(),
#         "reverse": lambda : arr.reverse(),
#     }
#     for task in [input().split(" ") for _ in range(int(input()))]:
#         #print(task)
#         function_dictionary.get(task[0])(*task[1:])
'''
在Python語法中:某函數後面有兩個括號 "fun(q)(w)"的用法，後面的(w)為呼叫 fun(q)內有其他fun的參數(w)
來呼叫 fun(q)(w) 得到整個fun(q)(w)的結果

例如:用 A_function(x)(y) 呼叫
=>即在 A_function(x)中有 B_function(y)時，
  呼叫A_function(x)且後面加一個括號(y)為B_function(y)的參數，以達到A_function同時觸發B_function
  的目的。 p.s.若無第二括號，執行結果僅A_function的結果


def basic(c):
    print(c)
    def add_1(d):
        print(c + d)
    return add_1
basic(20)(8)

'''
###################高級寫法 二 #############################
# if __name__ == '__main__':
#     arr = []
#     for a in range(int(input())):
#         f,*args = input().split(" ")
#         if f=="print":
#             print(arr)
#         else:
#             exec(f'arr.{f}({",".join(args)})')
#############################################################
#             #exec()執行儲存在字符、字串或文件中的Python 語句，相比於 eval()的 執行 "一行字串" ，
#             # exec()可以執行"多行字串"，並把輸入的字串，轉換成可執行的程式碼並執行
#             #  例如:
#             #    exec('''
#             #    for i in range(10):
#             #        print(i)
#             #    ''')
#             # https://vimsky.com/zh-tw/examples/usage/exec-in-python.html

# exec(object ,globals, locals)
# object : 必須為 字串 或是 code
# globals : 可選全域參數，如果呼叫必須為字典形式{key :value}
# locals : 可選區域參數，如果呼叫必須為字典形式{key :value}，若忽略，則取globals的相同參數的值，
#          若無該區域參數(不計字串中的)，但又被呼叫則該呼叫無效。
# x = 10
# expr = """
# z = 20
# sum = x + y + z
# print(sum)
# """
# def func():
#     y = 20
#     exec(expr)
#     exec(expr, {'x': 1, 'y': 2})
#     exec(expr, {'x': 1, 'y': 2 }, {'y': 3, 'z': 4})
# func()