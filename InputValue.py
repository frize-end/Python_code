#输入类型转换
try:
    age=int(input("请输入您的年龄："))
    height=float(input("请输入您的身高（米）："))
    print(f"您今年{age}岁，身高{height}米\n")
except ValueError:
    print("输入错误！\n")
#数字类型转换
num_int=100
print(f"{num_int},类型:{type(num_int)}")
num_float=3.14
print(f"{num_float},类型：{type(num_float)}")
num_complex=3 + 4j
print(f"{num_complex},类型：{type(num_complex)}")
#强制类型转换
print(f"整数转浮点数(100)：{float(num_int)}")
print(f"浮点数转整数(3.14)：{int(num_float)}")
print(f"字符串转数字：{int('123')},{float('3.14')}\n")
#数据类型判断
def check_type(value):
    print(f"值：{value}")
    print(f"类型：{type(value)}")
    print(f"是否为字符串：{isinstance(value, str)}")
    print(f"是否为整数:{isinstance(value, int)}")
    print(f"是否为列表：{isinstance(value, list)}")
    print(f"是否为数字：{isinstance(value, (int, float))}")
    print("*" * 30)

check_type("124")
check_type("hello")
check_type([1,2,3])
check_type(3.145)