#数据类型5-字典-函数

# a={"name":"华华","age":18,"money":99.99,"score":[99,100,88]}
#字典支持增删改，查（即取值）
#（1）新增元素 字典名[new_key]=value new_key不存在当前字典
#（2）修改元素 字典名[old_key]=value old_key存在当前字典
#（3）删除元素 字典名.pop(key)删除指定key的元素
#（4）拓展方法：
#（4-1）字典名.clear() 清空元素
#（4-2）del 字典名[key] 删除指定key的元素-方法2
#（4-3）字典名.popitem() 随机删除一组数据

# a["sex"]="female"
# a["age"]=20
# a.pop() #会报错，因为没有最后一个元素的概念，字典是无序的
# a.pop("age")
# a.clear() #返回空字典{}
# del a["name"]
# a.popitem()
# print(a)

#（5）取值拓展
# print(a.keys())  #返回所有keys
# print(a.values())  #返回所有values
# print(a.items())  #返回所有元素
# print(type(a.keys()))  #返回的类型是dict_keys
# print(type(a.items()))  #返回的类型是dict_items

#（6）多个字典合并
# a.update(c) c里面的key如果在a里面，则把c的value值更新到a里面去；
# 如果不存在，则把不存在的key添加到a里面去
a={"name":"华华","age":18,"money":99.99,"score":[99,100,88]}
c={"name":"豆豆","sex":"female"}
a.update(c)
print(a)

#a.setdefault() 未完全理解使用场景
print(a.setdefault("name"))  #key已存在，返回value
a.setdefault("weight") #key不存在，添加key,value是none
print(a)
