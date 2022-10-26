#SDK : Softwore development kit (軟體開發套件)
#底下是SDK 的寫法
class MathSdk():
    @staticmethod
    def triangle(x,y):
        return (x**2 + y**2)**0.5
class PhysicsSdk():
    @staticmethod
    def tp(v):
        c=299_792_458
        return 1/(1-(c/v)**2)**0.5

#底下是函數庫的寫法(library | lib)
def triangle(x,y):
    return (x**2 + y**2)**0.5
def tp(v):
    c=299_792_458
    return 1/(1-(c/v)**2)**0.5

# b = BiueSdk()
# x = b.triangle((3,4)#可以用但禁止
#print(x)

z=MathSdk.triangle(3,4)
print(z)