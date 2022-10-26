'''
一定要自己思考
1.輸入薪資 salary
2. 0    <salary<=20000":6%
3. 20000<salary<=40000":7%
4. 40000<salary<=60000":8%
5. 60000<salary<=80000":9%
6. 80000以上:13%
請列出薪資，所得稅，實領
以50000而言
薪資 : 50000, 所得稅: 4000, 實領 :46000
'''
############第一次接觸Python寫法，避免python內寫這種，因為會影響設計者判讀################
# salary = eval(input('請輸入薪水: '))
# real = 0
# if salary <= 20000 :
#     a=salary * 0.06 ; real = salary-a
#     print('輸入薪水:{},您的所得稅為:{},實領:{} '.format(salary,a,real))
# else:
#      if salary <= 40000 :
#          b = salary * 0.07 ; real = salary-b
#          print('輸入薪水:{},您的所得稅為:{},實領:{} '.format(salary,b,real))
#      else:
#          if salary <= 60000 :
#              c = salary * 0.08; real = salary - c
#              print('輸入薪水:{},您的所得稅為:{},實領:{} '.format(salary,c,real))
#          else:
#              if salary <= 80000:
#                  d = salary * 0.09; real = salary - d
#                  print('輸入薪水:{},您的所得稅為:{},實領:{} '.format(salary, d, real))
#              else:
#                  e = salary * 0.13 ;real = salary - e
#                  print('輸入薪水:{},您的所得稅為:{},實領:{} '.format(salary, e, real))

#######################
###變數命名非常重要，要注意!!! (盡量避免a,b,c,d,....等命名)#####
salary = eval(input('請輸入薪水: '))
if salary <= 20000 :
    a=salary * 0.06  #底下重複了，可精簡
    print(f'輸入薪水:{salary},您的所得稅為:{a},實領:{salary-a}')
else:
     if salary <= 40000 :
         b = salary * 0.07 #底下重複了，可精簡
         print(f'輸入薪水:{salary},您的所得稅為:{b},實領:{salary-b} ')
     else:
         if salary <= 60000 :
             c = salary * 0.08  # 底下重複了，可精簡
             print(f'輸入薪水:{salary},您的所得稅為:{c},實領:{salary-c} ')
         else:
             if salary <= 80000:
                 d = salary * 0.09  # 底下重複了，可精簡
                 print(f'輸入薪水:{salary},您的所得稅為:{d},實領:{salary-d} ')
             else:
                 print(f'輸入薪水:{salary},您的所得稅為:{salary * 0.13},實領:{salary*(1-0.13)} ')
#########可參考稍精簡寫法###############
salary = eval(input('請輸入薪水: '))
if salary <=20000:
   print(f'輸入薪水:{salary },您的所得稅為:{salary*0.06},實領:{salary*(1-0.06)}')
elif salary<=40000:
    print(f'輸入薪水:{salary},您的所得稅為:{salary * 0.07},實領:{salary * (1 - 0.07)}')
elif salary<=60000:
    print(f'輸入薪水:{salary},您的所得稅為:{salary * 0.08},實領:{salary * (1 - 0.08)}')
elif salary<=80000:
    print(f'輸入薪水:{salary},您的所得稅為:{salary * 0.09},實領:{salary * (1 - 0.09)}')
else:
    print(f'輸入薪水:{salary},您的所得稅為:{salary * 0.13},實領:{salary * (1 - 0.13)}')
########可參考精簡寫法###############
salary=eval(input("薪資:"))
tax=0
if salary <= 20000:
   tax=0.06
elif salary <=40000:
   tax=0.07
elif salary <=60000:
   tax=0.08
elif salary <=80000:
   tax=0.09
else:
   tax=0.13
print(f"薪資:{salary},所得稅:{salary*tax},實收:{salary*(1-tax)}")
#########也可參考最精簡寫法###########
salary=eval(input("薪資:"))
tax=0.13
if salary <= 20000:
   tax=0.06
elif salary <=40000:
   tax=0.07
elif salary <=60000:
   tax=0.08
elif salary <=80000:
   tax=0.09
print(f"薪資:{salary},所得稅:{salary*tax},實收:{salary*(1-tax)}")