#上下文管理器
class Timer:
    """计时器上下文管理器"""
    def __init__(self,name="操作"):
        self.name = name
    def __enter__(self):
        import time
        self.start_time=time.time()
        print(f"开始{self.name}")
        return self
    def __exit__(self,exc_type,exc_value,exc_tb):
        import time
        self.end_time=time.time()
        duration=self.end_time-self.start_time
        print(f"{self.name}完成，耗时：{duration:.4f}")
        if exc_type is not None:
            print(f"发生异常{exc_type.__name__}: {exc_value}")
            raise False  #不抑制异常
#使用上下文管理器
with Timer("数据处理"):
    #模拟一些耗时操作
    import time
    time.sleep(0.1)
    data=[i**2 for i in range(10000)]
    print(f"处理了{len(data)}个数据")
#使用contextlib简化上下文管理器
from contextlib import contextmanager
@contextmanager
def database_transaction():
    print("开始数据库事务")
    try:
        yield "数据库连接"
        print("提交事务")
    except Exception as e:
        print(f"回滚事务：{e}")
        raise
    finally:
        print("关闭数据库连接")

#使用简化的上下文管理器
with database_transaction() as db:
    print(f"使用{db}执行操作")
    #模拟数据库操作
print("**********************************")
#生成器基础
def number_generator(n):
    """生成0到n-1的数字"""
    for i in range(n):
        print(f"生成数字：{i}")
        yield i
#使用生成器
print("生成器示例：")
gen = number_generator(5)
print(f"生成器对象；{gen}")
#逐个获取值
for num in gen:
    print(f"接收到:{num}")
#斐波那契数列生成器
def fibonacci_generator(n):
    """生成斐波那契数列的前n项"""
    a,b=0,1
    count=0
    while count < n:
        yield a
        a,b=b,a+b
        count+=1
print(f"\n斐波那契数列：")
fib_gen = fibonacci_generator(10)
fib_numbers = list(fib_gen)
print(f"前十项：{fib_numbers}")
print("**********************************")
#生成器表达式
#与列表推导式的对比
print("列表推导式 vs 生成器表达式：")

#列表推导式 —— 立即创建所有元素
list_comp = [x**2 for x in range(10)]
print(f"列表推导式：{list_comp}")
print(f"内存占用：{list_comp.__sizeof__()}字节")

#生成器表达式 —— 按需生成元素
gen_exp = (x**2 for x in range(10))
print(f"生成器表达式：{gen_exp}")
print(f"内存占用：{gen_exp.__sizeof__()}字节")

#使用生成器表达式
print("\n生成器表达式的值：")
for value in gen_exp:
    print(value, end=" ")
print()
#大数据处理示例
def process_large_data():
    """处理大量数据的示例"""
    #模拟大数据集
    large_data = range(1000000)
    #使用生成器表达式节省内存
    even_squares = (x**2 for x in large_data)
    #只处理前十个结果
    result = []
    for i,value in enumerate(even_squares):
        if i>= 10:
            break
        result.append(value)
    return result
print(f"\n大数据处理结果：")
result = process_large_data()
print(f"前10个偶数的平方：{result}")

print("**********************************")
#自定义迭代器
class CountDown:
    """倒计时迭代器"""
    def __init__(self, start):
       self.start = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start+1
#使用自定义迭代器
print("倒计时迭代器：")
countdown = CountDown(10)
for num in countdown:
    print(f"倒计时：{num}")
#使用iter()函数
print("\n使用iter()函数：")
data=[1,2,3,4,5]
iterator=iter(data)

try:
    while True:
        value=next(iterator)
        print(f"迭代值：{value}")
except StopIteration:
    print("迭代结束")
#无限迭代器
class InfiniteIterator:
    """无限计数器"""
    def __init__(self,start=0,step=1):
        self.current=start
        self.step=step
    def __iter__(self):
        return self
    def __next__(self):
        value=self.current
        self.current += self.step
        return value
#使用无限迭代器（注意要有退出条件）
print(f"\n无限计数器（前10个值）：")
counter = InfiniteIterator(1,2)
for i,value in enumerate(counter):
    if i >= 10:
        break
    print(f"第{i+1}个值：{value}")
print("**********************************")
#装饰器基础
def timer_decorator(func):
    """计时装饰器"""
    import time
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time=time.time()
        print(f"{func.__name__},执行时间：{end_time-start_time:.5f}")
        return result
    return wrapper
def log_decorator(func):
    """日志装饰器"""
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用参数：{func.__name__}")
        print(f"参数：args={args},kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"返回值：{result}")
        return result
    return wrapper
#使用装饰器
@timer_decorator
@log_decorator
def calculate_sum(n):
    """计算从1到n的和"""
    return sum(range(1,n+1))
#测试装饰器
print("装饰器测试：")
result = calculate_sum(1000)
print(f"最终结果：{result}")