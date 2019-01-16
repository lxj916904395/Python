import math

# 绝对值
def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x

# 返回多个参数
def move(x,y,step,angle=0):
	nx = x+step*math.cos(angle)
	ny = y+step*math.sin(angle)
	return nx,ny


# //阶乘
def power(x,n=2):
	s = 1
	while n>0:
		n=n-1
		s=s*x
	return s	

# a*a+b*b,固定参
def calc(num):
    sum = 0
    for n in num:
        sum = sum + n * n
    return sum

# 可变参
def calchange(*numbers):
	s = 0
	for number in numbers:
		s=s+number*number
	return s

# 关键字参数
def person(name,age,**others):
	if 'name' in others:
		print('name=',others['name'])
	if 'job' in others:
		print('job=',others['job'])
	print('name:',name,',age:',age,',others',others)

# 限定关键字参数为city，job
def person1(name,age,*,city,job):
		print(name,age,city,job)	


# 可变参、命名关键字参数
def person2(name,age,*args,city,job):
		print(name,age,args,city,job)


def product(*num):
    if 0 == len(num):
        raise TypeError('error')
    sum = 1
    for n in num:
        sum=sum*n
    return sum


# 递归,n的阶乘
def fact(n):
	if n == 1:
		return 1
	else:
	 	return n*fact(n-1)	


# 切片，去除收尾空格
def trim(s):
    while s[:1] == " ":
        s = s[1:]
    while s[-1:] == " ":
        s = s[:-1]
    return s

# 迭代，查找List的最大、最小值
def findMinAndMax(list):
	if len(list) == 0:
		return (None,None)
	if len(list) == 1:
		return (list[0],list[0])
	else:
		min = list[0]
		for v in list:
			if v<min:
				min = v
		max = list[0]
		for v in list:
			if v>max:
				max = v	
		return (min,max)
	# if len(L) < 0:
 #        return (None, None)
 #    return (min(L), max(L))


 #列表生成式
def listCreate():
 	L1 = ['Hello', 'World', 18, 'Apple', None]
 	L2 = [s.lower() for s in L1 if isinstance(s,str)]
 	print(L2)
 # 	L3 = ['hello', 'world', 'apple']
	# if L2 == L3:
 #    	print('测试通过!')
	# else:
 #    	print('测试失败!')





# 
def normalize(name):
	f = name[0].upper()
	L = name[1:]
	name = f
	for s in L:
		name=name+s.lower()

	return name;












