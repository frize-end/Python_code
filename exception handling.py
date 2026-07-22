def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("错误：除数不能为零")
        return None
    except TypeError:
        print("错误；参数不正确")
        return None
    except Exception as e:
        print(f"未知错误；{e}")
        return None
    finally:
        print("计算完成")
#测试异常处理
print("异常处理测试:")
print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"'10' / 2 = {safe_divide('10', 2)}")

#多重异常处理
def process_user_input():
    try:
        # 获取用户输入
        num_str = input("请输入一个数字,计算它的平方根: ")
        num = float(num_str)

        # 计算平方根
        if num < 0:
            raise ValueError("不能计算负数的平方根")

        result = num ** 0.5
        print(f"{num} 的平方根是 {result:.2f}")

    except ValueError as e:
        if "could not convert" in str(e):
            print("错误: 输入的不是有效数字")
        else:
            print(f"数值错误: {e}")
    except KeyboardInterrupt:
        print("\n用户中断了程序")
    except Exception as e:
        print(f"未预期的错误: {e}")
    else:
        print("计算成功完成")
    finally:
        print("程序执行结束")

process_user_input()

#自定义异常
class CustomError(Exception):
 """自定义异常基类"""
pass
class AgeError(Exception):
    """年龄相关异常"""
def __init__(self,age,message="年龄值无效"):
    self.age=age
    self.message=message
    super().__init__(self.message)
class ScoreError(Exception):
    """分数相关异常"""
    def __init__(self,score,message="分数值无效"):
        self.score=score
        self.message=message
        super().__init__(self.message)
def validate_student_info(name,age,score):
   if not isinstance(name,str) or len(name.strip())==0:
       raise ValueError("姓名不能为空")
   if not isinstance(age,int) or age<0 or age>150:
       raise AgeError(age,f"年龄{age},不在合法范围内(1~150)")
   if not isinstance(score,(int,float)) or score<0 or score>100:
       raise ScoreError(score,f"分数{score}不在有效范围内(0~100)")
   return True
test_cases=[
    ("张三", 20, 85),
    ("", 20, 85),
    ("李四", -5, 85),
    ("王五", 20, 150)
]
for name,age,score in test_cases:
    try :
        validate_student_info(name,age,score)
        print(f"√ , {name}的身份验证信息通过")
    except (ValueError,AgeError,ScoreError) as e:
        print(f"× ，身份验证信息不通过,{e}")

#断言的使用
def calculate_average(numbers):
    """计算平均值"""
    #前置断言判断条件是否合适
    assert isinstance(numbers,list),"参数必须是列表"
    assert len(numbers)>0,"参数不能为空"
    assert all(isinstance(x,(int,float)) for x in numbers),"列表必须是数字"

    total=sum(numbers)
    average=total/len(numbers)

    #后置断言判断结果是否合理
    assert isinstance(average,(int,float)),"平均值必须是数字"
    return average
test_list=[
    [1, 2, 3, 4, 5],
    [],  # 空列表
    [1, 2, "3", 4],  # 包含非数字
    "not a list"  # 不是列表
]
for data in test_list:
    try:
        result = calculate_average(data)
        print(f"√ ，{data}的平均值是{result}")
    except AssertionError as e:
        print(f"× ， 断言失败 ：{e}")
    except Exception as e:
        print(f"× ， 其他错误：{e}")