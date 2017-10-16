#from itertools import *
import  itertools
from itertools import permutations,chain

ns=itertools.repeat('A',10)
n1=itertools.count(1)
n2=itertools.takewhile(lambda x:x<10,n1)#这里的lambda函数式子编程
#for  x in itertools.starmap(lambda x,y:x*y,[10,20,30],itertools.count(1)):
#    print(x)

#for m,n in itertools.product('abc',[1,2]): #多个循环器的笛卡尔积，相当于嵌套
  #  print(m,n)

li1=itertools.chain([1,2,3],[4,5,6]) # 把循环集进行链接

n3=itertools.permutations('abc',2) #从'abcd'中挑选两个元素，比如ab, bc, ... 将所有结果排序，返回为新的循环器。
n4=itertools.combinations('abcd',2)#从'abcd'中挑选两个元素，比如ab, bc, ... 将所有结果排序，返回为新的循环器。注意，上面的组合不分顺序，即ab, ba的话，只返回一个ab。
n5=itertools.combinations_with_replacement('abc',2)#与上面类似，但允许两次选出的元素重复。即多了aa, bb, cc
n=itertools.chain.from_iterable(('abc','def'))

pool=tuple([1,2,3,[7,6]])
