# coding: utf-8

str1 = "ABC"
str2 = "ABC"

print str1 == str2
print str1 is str2
print str1 is not str2

str1 = "ABC"
str2 = str1
print str1 == str2
print str1 is str2


num1 = 10
num2 = 10

print "num1 == num2", num1 == num2
print "num1 is num2", num1 is num2

name1 = "Hello, Yamashita.How are you doing?"
name2 = "Hello, Yamashita.How are you doing?"

print "name1 == name2", name1 == name2
print "name2 is name2", name1 is name2

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print "list1 == list2", list1 == list2
print "list1 is list2", list1 is list2

list1 = [1, 2, 3]
list2 = list1

print "list1 == list2", list1 == list2
print "list1 is list2", list1 is list2