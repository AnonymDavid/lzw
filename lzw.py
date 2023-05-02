from dataclasses import dataclass
from typing import List

@dataclass
class FIELD():
    m : int
    n : int
    char : str
    series : str

def getDict(dict:List[str]) -> List[FIELD]:
    dictionary = []
    help_list = []
    dictionary.append(FIELD(0, 0, '', ''))
    for i in range(len(dict)):
        if dict[i] not in help_list:
            dictionary.append(FIELD(i+1, 0, dict[i], dict[i]))
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
        
    dictionary.append(FIELD(mu+1, nm, '', ''))

    return dictionary

def encode(text:str) -> tuple[List[tuple[int, str]], List[int]]:
    encoded:List[FIELD] = encodeFull(text)
    dictionary = []
    code = []
    i = 1
    while encoded[i].n == 0:
        dictionary.append((encoded[i].m, encoded[i].char))
        i += 1
    while i < len(encoded):
        code.append(encoded[i].n)
        i += 1
    
    return dictionary, code
