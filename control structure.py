#条件判断基础
try:
  score=float(input("请输入您的成绩（0~100）："))
  print(f"您的成绩为{score}")
except ValueError:
  print("输入错误！")
if score>=90:
    grade="优秀"
elif score>=80:
    grade="良好"
elif score>=70:
    grade="中等"
elif score>=60:
    grade="及格"
else:
    grade="不及格"
print(f"您的成绩等级为：{grade}")

#多条件判断
age=25
income=50000
has_job=True

if age>=18 and income>=20000 and has_job==True:
    if age<65 and income>=50000:
        loan_amount=50000
    else:
        loan_amount=20000
    print(f"贷款审批通过，贷款额度为：{loan_amount}")
else:
    print("贷款审批未通过")
    if age<18:
        print("原因：年龄未满18岁")
    if income<20000:
        print("原因：收入不足20000")
    if not has_job:
        print("原因:无工作")
