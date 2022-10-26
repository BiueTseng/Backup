class DivZero(ArithmeticError):
    pass
def mymath(x,y):
    if y==0:
        raise DivZero("被除數為 0") #raise: 丟出，如同Java的 throw
    return x/y
def main():
    try:
        z=mymath(10,0)
    except Exception as e:
        # print(e)
        raise e #重丟

try:
    main()
except DivZero as e:
    print(e)