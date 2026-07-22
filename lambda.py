comp=lambda a,b : "a比b小" if a<b else "a大于等于b"
print(comp(2,5))  #lambda只能实现简单的逻辑，如果逻辑复杂且内容量大，则不建议使用

#内置函数
#查看所有的内置函数
import builtins
print(dir(builtins))
#内置函数1:abs返回绝对值
print(abs(-10))
#sum求和
print(sum(range(10)))
print(sum({12,4,5}))      #sum需要内置可迭代对象
#内置函数2 min(),max()求最小值和最大值
print(max(4,1,8))
print(min(4,1,8))

