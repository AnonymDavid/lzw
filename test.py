import lzw
from lzw import FIELD
from typing import List

text = 'abcabcbacbacbacbacbacbcabbcabcabcababacbacbcababcbacb'

output:List[FIELD] = lzw.encodeFull(text)

for line in output:
    print(f'{line.m}\t{line.n}\t{line.char}\t{line.series}')

print("--------------------")

encoded = lzw.encode(text)
print(encoded)

print("--------------------")

decoded = lzw.decode(encoded)
print(decoded)

print("--------------------")

print(text == decoded)