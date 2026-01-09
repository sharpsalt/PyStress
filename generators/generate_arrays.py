import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from Hashings.secure_random import get_secure_random

class gen_arrays:
    
    @staticmethod
    def random(len_: int,l: int,r: int,rng=None,unique: bool=False,sorted_: bool=False):
        if rng is None:
            rng=get_secure_random()
        if unique:
            if len_>r-l+1:
                raise ValueError("Cannot generate unique values: not enough numbers in range")
            v=set()
            while len(v)<len_:
                v.add(rng.randint(l,r))
            v=list(v)
        else:
            v=[rng.randint(l,r) for _ in range(len_)]
        if sorted_:
            v.sort()
        return v

    @staticmethod
    def permutation(n: int,rng=None):
        if rng is None:
            rng=get_secure_random()
        v=list(range(1,n+1))
        rng.shuffle(v)
        return v

    @staticmethod
    def matrix(rows: int,cols: int,l: int,r: int,rng=None,unique_rows: bool=False,sorted_rows: bool=False):
        if rng is None:
            rng=get_secure_random()
        return [gen_arrays.random(cols,l,r,rng,unique=unique_rows,sorted_=sorted_rows) for _ in range(rows)]

    @staticmethod
    def pairs(len_: int,l1: int,r1: int,l2: int,r2: int,rng=None,ordered: bool=False):
        if rng is None:
            rng=get_secure_random()
        v=[]
        for _ in range(len_):
            a=rng.randint(l1,r1)
            b=rng.randint(l2,r2)
            if ordered and a>b:
                a,b=b,a
            v.append((a,b))
        return v

    @staticmethod
    def subset(l: int,r: int,k: int,rng=None,sorted_: bool=False):
        if rng is None:
            rng=get_secure_random()
        if k>r-l+1:
            raise ValueError("Subset size larger than range")
        v=set()
        while len(v)<k:
            v.add(rng.randint(l,r))
        v=list(v)
        if sorted_:
            v.sort()
        else:
            rng.shuffle(v)
        return v

    @staticmethod
    def partition(sum_: int,k: int,min_val: int,max_val: int,rng=None):
        if rng is None:
            rng=get_secure_random()
        if sum_<min_val*k or sum_>max_val*k:
            raise ValueError("Sum out of possible range")
        parts=[min_val]*k
        remaining=sum_-min_val*k
        for i in range(k):
            # print(remaining)
            if remaining<=0:
                break
            add_max=min(remaining,max_val-min_val)
            delta=rng.randint(0,add_max)
            parts[i]+=delta
            remaining-=delta
        # print(parts)
        rng.shuffle(parts)
        return parts

    @staticmethod
    def arithmetic_progression(len_: int,start: int,step: int):
        return [start + i*step for i in range(len_)]

    @staticmethod
    def geometric_progression(len_: int,start: int,ratio: int):
        v=[]
        val=start
        for _ in range(len_):
            v.append(val)
            val*=ratio
        return v

    @staticmethod
    def constant_array(len_: int,value: int):
        return [value]*len_

    @staticmethod
    def bit_array(len_: int,prob_one: float=0.5,rng=None):
        if rng is None:
            rng=get_secure_random()
        return [1 if rng.random()<prob_one else 0 for _ in range(len_)]

    @staticmethod
    def shuffled(v,rng=None):
        if rng is None:
            rng=get_secure_random()
        v=v[:]
        rng.shuffle(v)
        return v

    @staticmethod
    def strictly_increasing(len_: int,start: int,step_min: int,step_max: int,rng=None):
        if rng is None:
            rng=get_secure_random()
        v=[start]
        cur=start
        for _ in range(1,len_):
            cur+=rng.randint(step_min,step_max)
            v.append(cur)
        return v

    @staticmethod
    def strictly_decreasing(len_: int,start: int,step_min: int,step_max: int,rng=None):
        if rng is None:
            rng=get_secure_random()
        v=[start]
        cur=start
        for _ in range(1,len_):
            cur-=rng.randint(step_min,step_max)
            v.append(cur)
        return v

    @staticmethod
    def random_with_sum(len_: int,sum_: int,min_val: int,max_val: int,rng=None):
        if rng is None:
            rng=get_secure_random()
        if sum_<min_val*len_ or sum_>max_val*len_:
            raise ValueError("Sum out of possible range")
        v=[min_val]*len_
        remaining=sum_-min_val*len_
        for i in range(len_):
            if remaining<=0:
                break
            add_max=min(remaining,max_val-min_val)
            # print(add_max)
            delta=rng.randint(0,add_max)
            v[i]+=delta
            remaining-=delta
        rng.shuffle(v)
        return v

if __name__ == "__main__":
    print(gen_arrays.matrix(5,5,10,20))
    print(gen_arrays.random(5,10,20,unique=True,sorted_=True))
    print(gen_arrays.permutation(5))
    print(gen_arrays.strictly_decreasing(5,20,1,3))
    print(gen_arrays.random_with_sum(5,500,10,200))