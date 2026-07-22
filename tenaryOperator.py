a=10
b=6

if a>b:
    max_value=a
else:
    max_value=b

#三元运算符
max_value_ternary=a if a>b else b
print(f"较大值:{max_value}")
print(f"三元运算结果：{max_value_ternary}")

#复杂的三元运算
age=int(input("请输入年龄："))
status="成年人" if age>=18 else "未成年人"
print(status)

#嵌套三元运算符
score=float(input("请输入成绩：(0~100)"))
grade="优" if score>=90 else "良" if score>=80 else "中等" if score>=70 else "及格" if score>=60 else "不及格"
print(grade)
