def data_validation(data):
    result={}
    #检验数据是否为空
    result['is_empty']=len(data)==0
    #检验是否为数字或字符串
    result['all_numbers']=all(isinstance(x,(int,float)) for x in data)
    result['all_strings']=all(isinstance(x,str) for x in data)
    #如果是数字
    if result['all_numbers']:
        result['is_positive']=all(x>0 for x in data)
        result['in_range_100']=all(0<=x<=100 for x in data)
    #如果是字符串
    if result['all_strings']:
        result['all_non_empty']=all(len(x.strip()) for x in data)
        result['all_alpha']=all(x.isalpha() for x in data)
    return result
#测试数据
test_data1=[1,2,3,4]
test_data2=["hello","python","world"]
test_data3=[]
print(f"测试数字列表：{data_validation(test_data1)}")
print(f"测试字母列表：{data_validation(test_data2)}")
print(f"测试空列表：{data_validation(test_data3)}")

#数据过滤和映射
data=[1,2,3,4,5,6,7,8,9,10]
#filter过滤
even_numbers=list(filter(lambda x:x%2==0,data))
print(f"偶数：{even_numbers}")
#map映射
square_numbers=list(map(lambda x: x**2,data))
print(f"平方数：{square_numbers}")
#使用列表推导式
even_square_numbers=[x**2 for x in data if x%2==0]
print(f"偶数位的平方数：{even_square_numbers}")
#字符串处理
words=["hello","python","world","kalilinux"]
long_words_upper=[word.upper() for word in words if len(word)>5]
print(f"过滤长度大于五的单词并大写{long_words_upper}")

#数据分组
from collections import defaultdict
students=[
    {"name":"张三","age":17,"class":"A班","score":98},
    {"name":"李四","age":18,"class":"B班","score":86},
    {"name":"王五","age":18,"class":"A班","score":88},
    {"name":"赵六","age":17,"class":"B班","score":94}
]
class_groups=defaultdict(list)
for student in students:
    class_groups[student["class"]].append(student)

for class_name,student_in_class in class_groups.items():
    print(f"\n班级：{class_name}")
    for student in student_in_class:
        print(f"姓名:{student['name']}:{student['score']}分")
#计算平均分
avg_score=sum(s['score'] for s in students)/len(students)
print(f"\n平均分：{avg_score:.1f}")
"""
用collections.defaultdict初始化一个特殊字典，键为班级名称，值默认是空列表，
方便直接对不存在的键执行 append 操作（避免普通字典因键不存在报错），用来存储每个班级对应的学生数据列表
"""