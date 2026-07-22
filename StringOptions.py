#字符串基本操作
text="Python Solution"
print(f"原始字符串：{text}")
print(f"改为大写：{text.upper()};改为小写：{text.lower()}")
print(f"总长度：{len(text)}")
print(f"替换：{text.replace("Python","Java")}")

#字符串分片
text1="Python is the best language!"
print(f"前七个字符：{text1[:7]},除了前七个以外的字符：{text1[7:]}")
print(f"中间部分：{text1[7:9]}")
print(f"隔一个字符：{text1[::2]}")
print(f"反转字符{text1[::-1]}")

#字符串判断
text2="Python2025"
print(f"是否为数字：{text2.isdigit()};是否为字母：{text2.isalpha()};是否为字母数字：{text2.isalnum()}")
print(f"是否为小写；{text2.islower()};是否为大写：{text2.isupper()}")

#字符串格式方法
name="张三"
age=18
score=96.5
print(f"姓名：{name},年龄：{age}，成绩：{score}")   #f-String方法
print("姓名：{}，年龄：{}，成绩：{:.1f}".format(name,age,score))  #format方法
print("姓名：%s,年龄：%d,成绩：%.1f"%(name,age,score))   #%格式化方法