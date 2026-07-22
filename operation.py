#布尔运算
a=True
b=False
print(f"a and b:{a and b}")
print(f"a or b:{a or b}")
print(f"非a:{not a}")
print(f"非b:{not b}")
#比较运算
x,y=3,8
print(f"{x}>{y}:{x > y}")
print(f"{x}<{y}:{x < y}")
print(f"{x}=={y}:{x == y}")
print(f"{x}!={y}:{x != y}")

#成员运算符与身份运算符

#in 与 not in(成员运算符）
text="hello world"
print(f"hello is in text:{'hello' in text}")
print(f"world is in text:{'world' in text}")
print(f"hello is not in text:{'hello' not in text}")
#is 与 is not
a1=[1,2,3,4]
a2=[1,2,3,4]
c=a1
print(f"a1 == a2:{a1 == a2}")  #值相同
print(f"a1 is b:{a1 is b}")  #对象不同
print(f"a1 is not c:{a1 is not c}")  #对象相同
