#嵌套数据结构
company={
    "名称":"科技公司",
    "部门":{
        "技术部":{
            "员工":["张三","李四","王五"],
            "项目":["项目A","项目B"]
        },
        "销售部":{
            "员工":["赵六","钱七"],
            "目标":100000
        }
    }
}
print(f"公司名称:{company["名称"]}")
print(f"技术部员工：{company["部门"]["技术部"]["员工"]}")
print(f"销售部目标：{company["部门"]["销售部"]["目标"]}")
#遍历嵌套结构
for dept_name,dept_info in company["部门"].items():    #.items() 方法会返回一个可迭代对象，其中每个元素是(键, 值)对。以列表返回可遍历的(键, 值) 元组数组
    print(f"\n{dept_name}")
    for key,value in dept_info.items():
        print(f"{key}:{value}")
#列表的排序和搜索
numbers=[76,9,15,73,65,21]
print(f"原列表：{numbers}")
sorted_ace=sorted(numbers)
sorted_desc=sorted(numbers,reverse=True)
print(f"升序排序:{sorted_ace}")
print(f"降序排序:{sorted_desc}")
"""
语法格式：sorted(iterable, key=None, reverse=False)
*iterable：必需参数，要排序的可迭代对象（如列表、元组、字符串等 。
*key：可选参数，用于指定一个函数，这个函数会作用于可迭代对象的每个元素，排序将基于该函数的返回值进行。例如，对列表中的字符串按长度排序，可写 sorted(list1, key=len)。
*reverse：可选参数，布尔值（True 或 False ），用于指定排序顺序，False 为升序（默认）,True 为降序
"""
numbers.sort()
print(f"原地排序:{numbers}")
#搜索
target=73
if target in numbers:
    index=numbers.index(target)
    print(f"找到{target}了!位置：{index}")
else:
    print("没找到")
#字符串编码与解码
text="你好，python！"
print(f"原字符串：{text}")
#编码
utf_bytes=text.encode('utf-8')
gbk_bytes=text.encode('gbk')
print(f"utf编码：{utf_bytes}")
print(f"gbk编码：{gbk_bytes}")
#解码
utf_decode=utf_bytes.decode('utf-8')
gbk_decode=gbk_bytes.decode('gbk')
print(f"utf-8解码：{utf_decode}")
print(f"gbk解码：{gbk_decode}")
#处理编码错误
try:
    wrong_decode=utf_bytes.decode('ascii')
except UnicodeDecodeError as e:
    print(f"编码错误：{e}")