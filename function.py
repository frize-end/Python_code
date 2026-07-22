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