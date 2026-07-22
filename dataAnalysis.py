#深拷贝和浅拷贝
import copy
original = [[1, 2, 3], [4, 5, 6]]
print(f"原始数据: {original}")

#浅拷贝
shallow_copy=copy.copy(original)
shallow_copy[0][0]=999
print(f"浅拷贝修改后的原始数据:{original}")
print(f"浅拷贝数据：{shallow_copy}")

#重置数据
original=[[1, 2, 3], [4, 5, 6]]

#深拷贝
deep_copy=copy.deepcopy(original)
deep_copy[0][0]=999
print(f"深拷贝修改后的原始数据:{original}")
print(f"深拷贝数据：{deep_copy}")
"""
区别：
浅拷贝的主要特点是它不拷贝对象内部的子对象，所以原始对象和拷贝对象会共享某些内容。
深拷贝则会拷贝所有内容，包括对象内部的子对象，因此原始对象和拷贝对象是完全独立的。
"""

#数据统计分析
numbers=[78,54,66,69,74,84,92,97,66]
#基本统计
print(f"数据：:{numbers}")
print(f"长度：{len(numbers)}")
print(f"最大值：{max(numbers)}")
print(f"最小值：{min(numbers)}")
print(f"总和：{sum(numbers)}")
print(f"平均值：{sum(numbers)/len(numbers):.2f}")
#排序后的统计
sorted_numbers=sorted(numbers)
print(f"排序后的数据：:{sorted_numbers}")
print(f"中位数：{sorted_numbers[len(sorted_numbers)//2]}")
#计数统计
from collections import Counter
counter=Counter(numbers)
print(f"计数统计：{counter}")
print(f"最常见的三个：{counter.most_common(3)}")
#第一次提交额外操作