#for循环基础
#遍历数字

print("遍历数字")
for i in range(5):
    print(f"数字：{i}")
#遍历列表
print("\n遍历列表")
fruits=["苹果","香蕉","梨"]
for fruit in fruits:
    print(f"水果：{fruit}")
#遍历字符串
print("\n遍历字符串")
for char in "Python":
    print(f"字符：{char}")
#带索引的遍历
print("\n带索引遍历")
for index,fruit in enumerate(fruits):
    print(f"索引：{index}:{fruit}")

#for循环高级用法
print("range(start,stop,step)")
for i in range(2,12,2):
    print(f"偶数：{i}")
#反向遍历
print("\n反向遍历")
for i in range(10,0,-1):
    print(f"倒数：{i}")
#多列表遍历
name=["张三","李四","王五"]
age=[20,18,25]
for name,age in zip(name,age):
    print(f"{name}:{age}岁")
#嵌套循环
print("九九乘法表")
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}")

#while循环基础
count=0
while count<5:
    count+=1
    print(f"计数：{count}")

#break和contine用法
print("\nbreak用法示例——找到第一个偶数")
nums=[1,3,5,8,9,10,15]
for num in nums:
    if num%2==0:
        print(f"找到第一个偶数：{num}")
        break
print("\ncontinue用法示例——跳过偶数")
for num in range(1,11):
    if num%2==0:
        continue
    print(f"跳过偶数:{num}")
#嵌套循环中的break和continue
print("\n嵌套循环示例")
for i in range(3):
    print(f"外层循环：{i}")
    for j in range(5):
        if j==3:
            break
    print(f"内层循环：{j}")
