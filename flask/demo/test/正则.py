import re
#字符集
'''
a = 'pas,as,aes,aqd,aqs,aas'
res = re.findall('a[ae]s', a)
print(res)

a = 'pas,as,aes,aqd,aqs,aas'
res1 = re.findall('a[^ae]s', a)
print(res1)

#概括字符集
#\w [a-zA-Z0-9_] 单词字符 \W 非单词字符（空格，特殊符号）
#\s空白字符  \S 非空白字符
b = 'python1python2$php1'
res2 = re.findall('\W', b)
print(res2)

#数量词 贪婪
c = 'python 1python2$ php 1'
res3 = re.findall('[a-z]{3,6}',c)
print(res3)
#非贪婪
res4 = re.findall('[a-z]{3,6}?',c)
print(res4)
#边界匹配 $
res5 = re.findall('[a-z]n$',c)
print(res5)

#组
a = 'jsjsjsjs'
res6 = re.findall('(js){3}', a)
print(res6)
'''

