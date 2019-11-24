#python之for循环-1

#for 遍历in后面数据类型里面的每个元素，依次挨个访问。
#for循环，循环的次数，是由in后面的元素个数所决定。
s="lemon"
t=("lemon",1,0.88)
l=["hello",0.99,[1,2,3]]
d={"name":"huahua","age":18,"sex":"female"}
for item in s:
    print("item是：",item)

#字典的遍历
# for item in d:
#     print("item是：",item)
#遍历字典时只会遍历到key，如果需要value可以遍历字典values的集合。
# for item in d.values():
#     print("item是：",item)
#或者，根据遍历到的key取值。
# for item in d:
#     print("item是：",d[item])


# 小题目：完成1-100的和
# sum=0
# for item in [1,2,3...100]:
#     sum+=item
# 需要range()函数与for循环结合使用