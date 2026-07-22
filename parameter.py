#不同类型的参数
def function_parameters(required,default_param="默认值",*args,**kwargs):
    print(f"必需参数：{required}")
    print(f"默认参数：{default_param}")
    print(f"可变位置参数：{args}")
    print(f"可变关键字参数：{kwargs}")
    print("-" * 30)
#测试不同的调用方式
function_parameters("必需值")
function_parameters("必需值","自定义默认值")
function_parameters("必需值","自定义默认值",1,2,3)
function_parameters("必需值",extra1="额外1",extra2="额外2")
function_parameters("必需值","自定义",1,2,name="张三",age=25)

#关键字参数和位置参数
def create_profile(name,age,city="未知",*,email,phone=None):
    """创建用户档案
    Args:
        name:姓名（位置参数）
        age:年龄（位置参数）
        city:城市（默认参数）
        email:邮箱（仅关键字参数）
        phone:电话（仅关键字参数，可选）
    """
    profile={
        "姓名":name,
        "年龄":age,
        "城市":city,
        "邮箱":email,
    }

    if phone:
        profile["电话"]=phone

    return profile
#调用方式
profile1=create_profile("张三",30,email="zhangsan@example.com")
profile2=create_profile("李四",25,city="北京",email="lisi@example.com",phone="13800138000")

print(f"用户档案1：{profile1}")
print(f"用户档案2：{profile2}")

#函数作为参数（高阶函数）
def apply_operation(numbers,operation):
    """对数字列表应用操作"""
    return [operation(num) for num in numbers]
def square(x):
    """平方函数"""
    return x ** 2
def cube(x):
    """立方函数"""
    return x ** 3
def double(x):
    """双倍函数"""
    return x * 2
#使用函数作为参数
numbers=[1,2,3,4,5]

print(f"原数字：{numbers}")
print(f"平方：{apply_operation(numbers,square)}")
print(f"立方：{apply_operation(numbers,cube)}")
print(f"双倍：{apply_operation(numbers,double)}")
#使用lambda函数
print(f"加10:{apply_operation(numbers,lambda x:x+10)}")

#返回函数（闭包）
def create_multiplier(factor):
    """创建乘法器函数"""
    def multiplier(x):
        return x * factor
    return multiplier
def create_counter(start=0):
    """创建计数器函数"""
    count=start
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
#使用返回的函数
double_multiplier=create_multiplier(2)
triple_multiplier=create_multiplier(3)

#使用计数器
counter1=create_counter()
counter2=create_counter(10)

print(f"计数器1：{counter1()},{counter1()},{counter1()}")
print(f"计数器2:{counter2()},{counter2()},{counter2()}")