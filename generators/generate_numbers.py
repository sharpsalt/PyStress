import random
from typing import List,Set

class gen_numbers:

    @staticmethod
    def random_int(l:int,r:int,rng=None)->int:
        if rng is None:
            rng=random.Random()
        return rng.randint(l,r)

    @staticmethod
    def random_real(l:float,r:float,rng=None)->float:
        if rng is None:
            rng=random.Random()
        return rng.uniform(l,r)

    @staticmethod
    def random_range(l,r,count:int,rng=None)->List:
        if rng is None:
            rng=random.Random()
        if isinstance(l,float) or isinstance(r,float):
            return [rng.uniform(l,r) for _ in range(count)]
        return [rng.randint(l,r) for _ in range(count)]

    @staticmethod
    def random_exclude(l:int,r:int,exclude:Set[int],rng=None)->int:
        if rng is None:
            rng=random.Random()
        while True:
            val=rng.randint(l,r)
            if val not in exclude:
                return val

    @staticmethod
    def random_range_exclude(l:int,r:int,count:int,exclude:Set[int],rng=None)->List[int]:
        if rng is None:
            rng=random.Random()
        v=[]
        while len(v)<count:
            val=rng.randint(l,r)
            if val not in exclude:
                v.append(val)
        return v

    @staticmethod
    def random_weighted(values:List,weights:List[float],rng=None):
        if rng is None:
            rng=random.Random()
        return rng.choices(values,weights,k=1)[0]

    @staticmethod
    def random_real_exclude(l:float,r:float,excl_l:float,excl_r:float,rng=None)->float:
        if rng is None:
            rng=random.Random()
        while True:
            val=rng.uniform(l,r)
            if not(excl_l<=val<=excl_r):
                return val


if __name__ == "__main__":
    print(gen_numbers.random_int(1,10))
    print(gen_numbers.random_real(1.0,10.0))
    print(gen_numbers.random_range(1,100,5))
    print(gen_numbers.random_exclude(1,10,{3,5,7}))
    print(gen_numbers.random_range_exclude(1,10,5,{2,4,6}))
    print(gen_numbers.random_weighted(['a','b','c'],[0.1,0.3,0.6]))
    print(gen_numbers.random_real_exclude(1.0,10.0,4.0,6.0))