#coding: utf-8
import MeCab
mc = MeCab()
text = "ラーメンはおいしい。"
print(mc.parse(text))