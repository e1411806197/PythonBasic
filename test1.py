"""1.python基础1"""
# chr-ord 交互使用
# chr 将整数转化为字符（unicall） ord字符转化为整数（ascii）

s=45
kk=chr(s)
print(ord(kk))

# oct hex bin
# 分别转化为8 16 2 进制

# eval 转化为表达式
pp='3.1415+21'
print(eval(pp))

# 复数使用
dd=complex(2,3)
print(dd)

# python中的is使用(用来标识两个变量是否指向相同的地址)
a,b=3,3
print(a is b)

c=[1,2,3]
d=[1,2,3]
print(c is d)

c=lambda x,y :x is y
print(c(3,3))
# python中的三元表达式
xx=a if a>3 else b
print(xx)