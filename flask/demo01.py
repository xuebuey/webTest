'''
account = 'lixue'
password = '666'

print("please enter username")
username = input()
print("please enter password")
passwords = input()

if account == username and password == passwords:
    print("login")
else:
    print("again")

# snippet 片段 代码快补充
# pass pass 空语句/占位语句
a = [1,2,3,4,5,6,7,8,9,0]
for x in range(len(a),0,-3):
    print(x, end='happy')
'''
a = [1,2,3,4,5,6,7,8,9,0]
b = a[0:len(a):2]
print(b)