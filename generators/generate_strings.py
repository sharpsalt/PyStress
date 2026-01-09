import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from Hashings.secure_random import get_secure_random
from enum import Enum
from typing import List

class CaseType(Enum):
    Lower=0
    Upper=1
    Mixed=2

class gen_strings:

    @staticmethod
    def random_char(case_type:CaseType,rng=None,l='a',r='z')->str:
        if rng is None:
            rng=get_secure_random()
        if case_type==CaseType.Upper:
            base='A'
        else:
            base='a'
        ch=chr(ord(base)+rng.randint(ord(l)-ord(base),ord(r)-ord(base)))
        if case_type==CaseType.Mixed and rng.randint(0,1):
            ch=ch.upper() if ch.islower() else ch.lower()
        return ch

    @staticmethod
    def random(len_:int,case_type:CaseType,rng=None,l='a',r='z')->str:
        if rng is None:
            rng=get_secure_random()
        return ''.join(gen_strings.random_char(case_type,rng,l,r) for _ in range(len_))

    @staticmethod
    def palindrome(len_:int,case_type:CaseType,rng=None,l='a',r='z')->str:
        if rng is None:
            rng=get_secure_random()
        s=['']*len_
        i,j=0,len_-1
        while i<=j:
            ch=gen_strings.random_char(case_type,rng,l,r)
            s[i]=s[j]=ch
            i+=1
            j-=1
        return ''.join(s)

    @staticmethod
    def random_alphanum(len_:int,letters:bool,digits:bool,case_type:CaseType,rng=None)->str:
        if rng is None:
            rng=get_secure_random()
        assert letters or digits
        s=[]
        for _ in range(len_):
            if letters and digits:
                if rng.randint(0,1):
                    s.append(gen_strings.random_char(case_type,rng))
                else:
                    s.append(chr(ord('0')+rng.randint(0,9)))
            elif letters:
                s.append(gen_strings.random_char(case_type,rng))
            else:
                s.append(chr(ord('0')+rng.randint(0,9)))
        return ''.join(s)

    @staticmethod
    def random_custom(len_:int,alphabet:str,rng=None)->str:
        if rng is None:
            rng=get_secure_random()
        assert alphabet
        return ''.join(alphabet[rng.randint(0,len(alphabet)-1)] for _ in range(len_))

    @staticmethod
    def random_strings(count:int,len_:int,case_type:CaseType,rng=None)->List[str]:
        if rng is None:
            rng=get_secure_random()
        return [gen_strings.random(len_,case_type,rng) for _ in range(count)]

    @staticmethod
    def palindromes(count:int,len_:int,case_type:CaseType,rng=None)->List[str]:
        if rng is None:
            rng=get_secure_random()
        return [gen_strings.palindrome(len_,case_type,rng) for _ in range(count)]

if __name__ == "__main__":
    print(gen_strings.random(10,CaseType.Mixed))
    print(gen_strings.palindrome(11,CaseType.Lower))
    print(gen_strings.random_alphanum(15,True,True,CaseType.Upper))
    print(gen_strings.random_custom(12,"abc123"))
    print(gen_strings.random_strings(5,8,CaseType.Lower))
    print(gen_strings.palindromes(3,7,CaseType.Mixed))