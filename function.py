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

#递归函数
def factorial(n):
    """计算阶乘"""
    if n<=1:
        return 1
    return  n * factorial(n-1)
def fibonacci(n):
    """计算斐波那契数列第n项"""
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
def fibonacci_memo(n,memo={}):
    """带记忆化的斐波那契数列"""
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    memo[n]=fibonacci_memo(n-1,memo)+fibonacci_memo(n-2,memo)
    return memo[n]
#测试递归函数
print(f"5的阶乘：{factorial(5)}")
print(f"斐波那契数列前10项：")
for i in range(10):
    print(f"F({i})={fibonacci_memo(i)}")

#装饰器函数
def retry(max_attempts=3):
    """重试装饰器"""
    def decorator(func):
        def wrapper(*args,**kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    if attempt == max_attempts-1:
                        raise e
                    print(f"第{attempt+1}次尝试失败：{e}")
            return None
        return wrapper
    return decorator
def validata_types(**types):
    """类型验证装饰器"""
    def decorator(func):
        def wrapper(*args,**kwargs):
            #验证位置参数
            import inspect
            sig = inspect.signature(func)
            bound_args=sig.bind(*args,**kwargs)
            bound_args.apply_defaults()

            for param_name,excepted_type in types.items():
                if param_name in bound_args.arguments:
                    value=bound_args.arguments[param_name]
                    if not isinstance(value,excepted_type):
                        raise TypeError(f"参数{param_name}应该是{excepted_type.__name__}类型")
            return func(*args,**kwargs)
        return wrapper
    return decorator

#使用装饰器
@retry(max_attempts=3)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise Exception("随机失败")
    return "成功"
@validata_types(name=str,age=int)
def create_person(name,age):
    return f"创建了{name},年龄{age}"
#测试装饰器
try:
    result = unreliable_function()
    print(f"结果:{result}")
except Exception as e:
    print(f"最终失败:{e}")
try:
    person = create_person("张三", 25)
    print(person)
    # person = create_person("李四", "25")  # 会报错
except TypeError as e:
    print(f"类型错误: {e}")

#生成器函数
def read_file_lins(filename):
    """逐行读取文件的生成器"""
    try:
        with open(filename,"r",encoding="utf-8") as file:
            for line_num,line in enumerate(file,start=1):
                yield line_num,line.strip()
    except FileNotFoundError:
        print(f"文件{filename}不存在")

def prime_generator(limit):
    """生成质数的生成器"""
    def is_prime(num):
        def is_prime(n):
            if n<2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
    for num in range(2,limit+1):
        if is_prime(num):
            yield num
def batch_generator(data,batch_size):
        """批量处理数据的生成器"""
        for i in range(0,len(data),batch_size):
            yield data[i:i + batch_size]
#使用生成器
print("前20个质数：")
primes=list(prime_generator(20))
print(primes[:20])

print("\n批量处理数据：")
data=list(range(1,21))
for batch in batch_generator(data,5):
    print(f"批次:{batch}")

#函数注解
def calculate_sum(length:float,width:float)->float:
    """计算矩形面积
    Args:
        length：长度
        width：宽度
    Returns:
        面积"""
    return length*width
def process_data(data:List[int],multiplier:int = 2)->List[int]:
    """处理数据"""
    return [x*multiplier for x in data]
from typing import Union,Optional,List
    
def advenced_function(
        name:str,
        age:int,
        scores:Optional[List[float]]=None,
        metadata:Dict[str,Union[str,int]]=None
)