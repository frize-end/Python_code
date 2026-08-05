#元组的创建和基本操作
coordinates=(1,2)
print(f"坐标：{coordinates}")
print(f"坐标的x轴：{coordinates[0]}")
print(f"坐标的y轴：{coordinates[1]}")
#元组的解包
x,y=coordinates
print(f"解包后：x={x},y={y}")

#可以用*运算符把一个可迭代对象拆开作为函数的参数
divmod(20,8)
t=(20,8)
print(divmod(*t))
quo,rem=divmod(*t)
print(f"商：{quo},余数：{rem}")
#用*来处理剩下的元素
a,b,*rest=range(5)
print(f"用*来处理剩下的元素：{a},{b},{rest}")
#平行赋值
m,*body,n,q=range(5)
print(f"平行赋值：{m},{body},{n},{q}")
#命名元组
from collections import (
    namedtuple,  #使用from ... import ...可以从模块中导入特定的部分，如函数、类或变量
)

Point=namedtuple('Point',['x','y'])
p = Point(1,2)
print(f"命名元组：{p}")
print(f"x坐标：{p.x};y坐标：{p.y}\n")
print(p._fields)  #_fields属性是一个包含这个类所有字段名称的tuple
pil=p._make(p)
print(f"_make()方法命名元组：{pil}")  #_make方法将一个tuple转换为命名元组
print(p._asdict())  #_asdict方法将具名元组以collections.OrderedDict形式返回
#字典的创建
student={
    "name":"张三",
    "age": 18,
    "subject":"python",
    "score":[80,84,91]
}
print(f"学生信息：{student}")
print(f"学生姓名:{student['name']}")
print(f"学生年龄：{student.get('age','unknown')}")
"""
get函数是字典对象的一个非常有用的方法。它允许你通过键来安全地访问字典中的值。
如果键不存在于字典中，get函数可以返回一个默认值
"""
#添加和修改
student["num"]="scp_096"
student["age"]=20
print(f"修改后的信息：{student}")
#字典的遍历
print("\n遍历字典：")
for key,value in student.items():
    print(f"{key}:{value}")
#字典推导式
square_dict={x: x**2 for x in range(1,7)} #创建平方字典
print(f"平方字典：{square_dict}")
scores={"lily":84,"vincent":92,"micheal":96,"poul":91} #筛选字典
high_scores={name:score for name,score in scores.items() if score>=90}
print(f"高分成绩：{high_scores}")
words=["windows","linux","macos","kali"]
len_dict={word:len(word) for word in words}
print(f"字符串长度字典：{len_dict}")