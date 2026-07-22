#列表的创建
fruits=["apple","banana","watermelon"]
print(f"fruits list:{fruits}")
#列表基本操作增删改查
fruits.append("pear")
print(f"增加元素后的列表：{fruits}")
fruits.remove("apple")
print(f"删除元素后的列表：{fruits}")
fruits.insert(1,"orange")
print(f"插入元素后的列表：{fruits}")
print(f"查看第一个元素：{fruits[0]}")
print(f"查看最后一个元素：{fruits[-1]}")
fruits.pop(1)
print(f"删除第二个元素：{fruits}")
#列表的分片
num=[0,1,2,3,4,5,6,7,8,9,10]
num1=num
print(f"前五个数字：{num[:5]}")
print(f"后六个数字：{num[5:]}")
print(f"偶数位数字：{num[::2]}")
num1.pop(0)
print(f"奇数位数字{num1[::2]}")
print(f"反转列表：{num[::-1]}")
#列表的遍历
print("\n遍历列表：")
for i,num in enumerate(num):
    print(f"索引{i},元素：{num}")
#列表推导式
sqlite=[x**2 for x in range(1,11)]
print(f"生成平方数：{sqlite}")
even_numbers=[x for x in range(1,12) if x%2==0]
print(f"筛选偶数:{even_numbers}")
words=["hello","world","python"]
capitalized=[word.capitalize() for word in words]
print(f"首字母大写：{capitalized}")
