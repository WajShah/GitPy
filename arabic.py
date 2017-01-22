# -*- coding: utf-8 -*-

text = "چرا کار نمیکنی؟" # also using u"...." results the same
print(text,"Case 1")

text = "چرا کار نمیکنی؟".encode("utf-8")
print(text,"Case 2")

import sys

text = "چرا کار نمیکنی؟".encode("utf-8")
print("Case 3")
sys.stdout.buffer.write(text)
