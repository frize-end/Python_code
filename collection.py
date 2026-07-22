#集合的创建和操作
set1={1,2,3,4,5}
set2={5,6,7,8,9}
print(f"原集合一：{set1},原集合二：{set2}")
#集合运算
print(f"两集合的交集：{set1 & set2}")
print(f"两集合的差集：{set2 - set1}")
print(f"两集合的并集：{set1 | set2}")
print(f"对称差集：{set1 ^ set2}")
#集合方法
set1.add(91)
print(f"增加一个元素后的集合一：{set1}")
set1.discard(1)
print(f"删除一个元素后的集合一：{set1}")
set1.remove(3)
print(f"再次删除一个元素的集合一：{set1}")
#字符串方法
text=" hello python world "
print(f"原字符串：{text}")
print(f"去除空格：{text.strip()}") #strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
"""
用法
1. 移除指定字符。可以通过传递参数来移除字符串头尾的特定字符。
2. 移除多个字符。如果参数chars不为None有值，那就去掉在chars中出现的所有字符。
"""
print(f"分割字符串：{text.strip().split()}")
text2=" hello,python,world! "
print(f"字符串二：{text2}")
print(f"分割字符串二：{text2.strip().split(',')}")
print(f"连接字符串：{'-'.join(['a','b','z'])}")
print(f"查找字符串：{text.find("python")}")
print(f"替换字符串：{text.replace("python","Java")}")
print(f"字符串居中：{text.strip().center(30,"*")}")
#firststar