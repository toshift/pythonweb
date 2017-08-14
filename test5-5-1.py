# coding: utf-8

num = 10
sum = num + 7
print sum

num1 = 10
num2 = 8
sum = num1 + num2
print sum

msg = "Hello"
newmsg = msg + "World!"
try:
    errmsg = msg + 10
    print "TypeError"
except:
    pass

print newmsg


num1 = 10
num2 = 8
num3 = 15
print str(num1), "+", str(num2), "+", str(num3), "=",
print num1 + num2 + num3

msg = "Hello"
newmsg = msg + "World!"
print newmsg