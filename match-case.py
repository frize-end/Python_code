def handle_data(data):
    match data:
        case int() if data>0:
            return f"正整数: {data}"
        case int() if data<0:
            return f"负整数: {data}"
        case 0 :
            return "零"
        case str() if len(data)>0:
            return f"非空字符串: {data}"
        case [] :
            return f"空列表"
        case [x] if isinstance(x, int):
            return f"包含一个整数的列表；{x}"
        case [x,y] :
            return f"包含两个元素的列表:{x},{y}"
        case {"name":name,"age":age} :
            return f"包含姓名和年龄的字典：{name},{age}"
        case _ :
            return f"其他类型：{type(data)}"

#测试模式匹配
test_cases = [
    42, -10, 0, "Hello", [], [5], [1, 2],
    {"name": "张三", "age": 25}, (1, 2, 3)
]
print("模式匹配示例：")
for case in test_cases:
    result = handle_data(case)
    print(f"{case}->{result}")

