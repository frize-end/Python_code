#数据结构的转换
"""
列表：顺序存储结构，占更多存储空间（默认存了指针），元素不必相同，用"[]“表示。
元组：元组和列表在结构上没有什么区别，唯一的差异在于元组是只读的，不能修改。元组用“()”表示。
字典：字典定义了键和值之间一对一的关系,但它们是以无序的方式储存的。定义 Dictionary 使用一对大(花)括号”{}"。（其中前三个也可称之为Python的数组类型）
集合：用的比较少，无序不重复元素集。
"""
#列表转换
list_data=[1,2,3,4,5]
tuple_data=tuple(list_data)
set_data=set(list_data)
print(f"列表：{list_data}")
print(f"元组：{tuple_data}")
print(f"集合：{set_data}\n")

#字符串转换
string_data="hello"
list_from_string=list(string_data)
tuple_from_string=tuple(string_data)
set_from_string=set(string_data)
print(f"字符串：{string_data}")
print(f"转列表：{list_from_string}")
print(f"转元组：{tuple_from_string}")
print(f"转集合：{set_from_string}\n")

#字典转换
dict_data={"a":1,"b":2,"c":3}
dict_keys=list(dict_data.keys())
dict_values=list(dict_data.values())
dict_items=list(dict_data.items())
print(f"字典：{dict_data}")
print(f"键列表：{dict_keys}")
print(f"值列表；{dict_values}")
print(f"项列表：{dict_items}\n")

#字符串格式化高级用法
name="张三"
age=20
score=94.5

#f-string高级格式化
print(f"姓名:{name:>10}")#右对齐，宽度10
print(f"年龄:{age:0>5}")#用0填充，宽度5
print(f"成绩：{score:8.2f}")#宽度8，保留两位小数
print(f"百分比：{score/100:.2%}")#百分比格式

#数字格式化
number=12345678
print(f"千分位分割：{number:,}")
print(f"科学计数法：{number:.2e}")

#日期格式化
from datetime import datetime
now=datetime.now()
print(f"当前时间:{now:%Y-%m-%d %H:%M:%S}")