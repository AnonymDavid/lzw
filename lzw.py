from dataclasses import dataclass
from typing import List

@dataclass
class FIELD():
    m : int
    n : int
    char : str
    series : str

@dataclass
class ENCODED():
    dictionary : List[str]
    code : List[int]

def getDict(dict:List[str]) -> List[FIELD]:
    dictionary = []
    help_list = []
    dictionary.append(FIELD(0, 0, '', ''))
    c = 1
    for i in range(len(dict)):
        if dict[i] not in help_list:
            dictionary.append(FIELD(c, 0, dict[i], dict[i]))
            c += 1
            help_list.append(dict[i])
    
    return dictionary

def findFirstChar(dict:List[FIELD], ch:str) -> int:
    i = 0
    while i < len(dict) and dict[i].char != ch:
        i += 1
    return i

def encodeFull(text:str) -> List[FIELD]:
    dictionary:List[FIELD] = getDict(text)
    
    nm = 0
    mu = dictionary[-1].m
    for c in text:
        i = 0
        while i < len(dictionary) and (dictionary[i].n != nm or dictionary[i].char != c):
            i += 1
        
        if i < len(dictionary):
            nm = dictionary[i].m
        else:
            dictionary.append(FIELD(mu+1, nm, c, f'{dictionary[nm].series}{c}'))
            nm = findFirstChar(dictionary, c)
            mu += 1

    dictionary.append(FIELD(mu+1, nm, dictionary[nm].char, dictionary[nm].series))

    return dictionary

def encodeTable(table:List[FIELD]) -> ENCODED:
    dictionary = []
    code = []
    i = 1
    while table[i].n == 0:
        dictionary.append(table[i].char)
        i += 1

    while i < len(table):
        code.append(table[i].n)
        i += 1
    
    return ENCODED(dictionary, code)

def encode(text:str) -> ENCODED:
    encoded:List[FIELD] = encodeFull(text)
    
    return encodeTable(encoded)

def decodeFull(encoded:ENCODED) -> List[FIELD]:
    dictionary:List[FIELD] = getDict(encoded.dictionary)

    mu = dictionary[-1].m + 1
    n = encoded.code[0]
    dictionary.append(FIELD(mu, n, '', dictionary[n].char))

    for i in range(1, len(encoded.code)):
        n = encoded.code[i]
        mu += 1
        j = n
        while dictionary[j].n != 0:
            j = dictionary[j].n
        
        dictionary.append(FIELD(mu, n, '', ''))
        dictionary[mu-1].char = dictionary[j].char
        dictionary[mu-1].series = f'{dictionary[mu-1].series}{dictionary[j].char}'
        dictionary[mu].series = dictionary[n].series
    
    dictionary[mu].char = dictionary[dictionary[mu].n].series[-1]

    return dictionary

def decodeTable(table:List[FIELD]) -> str:
    text = ""
    for x in table:
        text += x.series[:-1]
    
    text += table[-1].series[-1]
    
    return text

def decode(encoded:ENCODED) -> str:
    dictionary = decodeFull(encoded)

    return decodeTable(dictionary)
