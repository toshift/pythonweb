# coding:utf-8

"""
入力された値のbitを数える
# in : 10 2
# out: 5
http://www.nminoru.jp/~nminoru/programming/bitcount.html
"""
retult = 0
n,m = input().split(" ")
for i in range(int(n)+1):
    bits = bin((i & 0x55555555)+((i >> 1) & 0x55555555))
    bits = bin((int(bits,2) & 0x33333333) + (int(bits,2) >> 2 & 0x33333333))
    bits = bin((int(bits,2) & 0x0f0f0f0f) + (int(bits,2) >> 4 & 0x0f0f0f0f))
    bits = bin((int(bits,2) & 0x00ff00ff) + (int(bits,2) >> 8 & 0x00ff00ff))
    bits = bin((int(bits,2) & 0x0000ffff) + (int(bits,2) >> 16 & 0x0000ffff))
    if int(m) == int(bits,2):
        retult += 1
print(retult)
