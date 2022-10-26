# def getColor(item, color =None):
#     if color is None:
#         color =[]
#     color.append(item)
#     print('顏色:',color)
# key = input('y 繼續..,n結束迴圈..:')
# while key == 'y':
#     wd = input('輸入顏色:')
#     getColor(wd)
#     key = input('y 繼續..,n結束迴圈..:')
import turtle
# turtle.setup(width:畫布寬, height:畫布高, startx :畫布x起始位置,starty :畫布y起始位置)
turtle.setup(400,400)
# 看turtle 原始畫布
turtle.Turtle()
#設定畫筆速度
# turtle.speed(1)
turtle.title("畫布練習")
turtle.setpos(-50,50)
turtle.position()
# turtle.setposition(-50,-50)
# turtle.goto(-50,50)
# turtle.goto(50,50)
# turtle.goto(-50,-50)
# turtle.goto(50,-50)
# turtle.home()

#turtle 運行結束後視窗會跟著結束，若不要turtle視窗自動關掉，則加入底下這行
turtle.done()