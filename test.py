import lzw
from lzw import FIELD
from typing import List

output:List[FIELD] = lzw.encodeFull("abaababa")

for line in output:
    print(f'{line.m}\t{line.n}\t{line.char}\t{line.series}')

print("--------------------")

print(lzw.encode("abaababa"))