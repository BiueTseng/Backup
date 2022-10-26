#Call Stack :調用棧(大陸用語)
#1. mymath處理例外
#2. 若mymath不處理，則會丟給上一層(stack) 處理，稱為call stack
#3. 若所有層都不處理，則交由系統處理，此時就是閃退

#1
def mymath(x,y):
    try:
        z=x/y
        return z
    except:
        print("error")

def main():
    try:
        print(mymath(10,0))
    except:
        print("error")

if __name__=="__main__":
    main()
#2



#3
