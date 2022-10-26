#pandas 跟numpy一樣，都有很多東西還沒講，跟AI深度學習有關係
import pandas as pd
planets={'mercury':'水星','venus':'金星','earth':'地球','mars':'火星','jupiter':'木星','saturn':'土星','uranus':'天王星','netpune':'海王星','pluto':'冥王星'}
solor=pd.Series(data=planets) #data可加可不加
print(solor['earth'])
print(solor[2])