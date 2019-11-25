#5.字符串的切片

#根据索引取值，只能取单个值
#切片可以根据自己的要求任意取值，子字符串
#切片格式：[m:n:k]
# m 索引开始的地方 n 索引结束的地方 k 步长
#规则：取左不取右，取到n-1结束
a = "hello lemon"
res = a[1:11:2] #k=2,结果el eo, 注意空格也是一个字符
res = a[0:5] #k=1，结果hello （k如果不输入，则默认为1）
res = a[-5:-1] #反序取值到-1，取不到最后一个字母，a[-5:0]也不对。待研究？
res = a[:] #从头取到尾
res = a[1:] #从start取到尾
res = a[:11] #从头取到end-1
print(res)
print(a[1:10:2]) #取n之前的偶数位，el eo

#使用场景补充：取单个字符，用索引；取子字符串，用切片。