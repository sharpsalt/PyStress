import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from Hashings.secure_random import get_secure_random
from typing import List, Tuple

class gen_graphs:
    
    @staticmethod
    def tree(n: int,zero_based=False,rng=None)->List[Tuple[int,int]]:
        if rng is None:
            rng=get_secure_random()
        nodes=list(range(1,n+1))
        rng.shuffle(nodes)
        edges=[]
        for i in range(1,n):
            u=nodes[i]
            v=nodes[rng.randint(0,i-1)]
            edges.append((u,v) if not zero_based else (u-1,v-1))
            # edges.append((u, v))

        rng.shuffle(edges)
        return edges

    @staticmethod
    def simple_graph(n: int,m: int,zero_based=False,rng=None)->List[Tuple[int,int]]:
        if rng is None:
            rng=get_secure_random()

        edges=gen_graphs.tree(n, rng)
        edge_set=set(tuple(sorted(e)) for e in edges)
        while len(edge_set)<m:
            u=rng.randint(1,n)
            v=rng.randint(1,n)
            if u!=v:
                # print(u,v)
                edge_set.add(tuple(sorted((u,v) if not zero_based else (u-1,v-1))))
        return list(edge_set)

    @staticmethod
    def weighted_graph(n: int, m: int, min_w:int, max_w:int, zero_based=False,rng=None):
        if rng is None:
            rng=get_secure_random()

        edges=gen_graphs.simple_graph(n, m, zero_based, rng)
        return [(u,v,(rng.randint(min_w, max_w) if not zero_based else (rng.randint(min_w, max_w)))) for u,v in edges]

    @staticmethod
    def directed_graph(n: int,m: int,zero_based=False,rng=None)->List[Tuple[int,int]]:
        if rng is None:
            rng=get_secure_random()
        edge_set=set()
        while len(edge_set)<m:
            u=rng.randint(1,n)
            v=rng.randint(1,n)
            if u!=v:
                edge_set.add((u, v) if not zero_based else (u-1,v-1))
        return list(edge_set)

    @staticmethod
    def dag(n: int,m: int,zero_based=False,rng=None)->List[Tuple[int, int]]:
        if rng is None:
            rng=get_secure_random()

        nodes=list(range(1,n+1))
        rng.shuffle(nodes)
        edge_set=set()
        while len(edge_set)<m:
            u=rng.randint(0,n-2)
            v=rng.randint(u+1,n-1)
            edge_set.add((nodes[u], nodes[v]) if not zero_based else (nodes[u]-1,nodes[v]-1))

        return list(edge_set)

    @staticmethod
    def bipartite(n1: int,n2: int,m: int,zero_based=False,rng=None)->List[Tuple[int,int]]:
        if rng is None:
            rng=get_secure_random()
        edge_set=set()
        while len(edge_set)<m:
            u=rng.randint(1,n1)
            v=rng.randint(1,n2)+n1
            edge_set.add((u,v) if not zero_based else (u-1,v-1))
        return list(edge_set)

    @staticmethod
    def star(n:int,center:int=1,zero_based=False,rng=None)->List[Tuple[int,int]]:
        if rng is None:
            rng=get_secure_random()
        edges=[]
        for i in range(1,n+1):
            if i!=center:
                edges.append((center,i) if not zero_based else (center-1,i-1))
        rng.shuffle(edges)
        return edges

    @staticmethod
    def cycle(n:int,zero_based=False,rng=None)->List[Tuple[int,int]]:
        if rng is None:
            rng=get_secure_random()
        nodes=list(range(1,n+1))
        rng.shuffle(nodes)
        if zero_based:
            return [(nodes[i]-1,nodes[(i+1)%n]-1) for i in range(n)]
        return [(nodes[i],nodes[(i+1)%n]) for i in range(n)]
    
    @staticmethod
    def complete(n:int,zero_based=False)->List[Tuple[int,int]]:
        if zero_based:
            return [(i,j) for i in range(n) for j in range(i+1,n)]
        return [(i,j) for i in range(1,n+1) for j in range(i+1,n+1)]

    @staticmethod
    def regular(n:int,d:int,zero_based=False,rng=None)->List[Tuple[int,int]]:
        if rng is None:
            rng=get_secure_random()
        if (n*d)%2!=0 or d>=n:
            return []
        nodes=[]
        for i in range(1,n+1):
            nodes.extend([i]*d)
        rng.shuffle(nodes)
        edges=[]
        for i in range(0,len(nodes),2):
            if nodes[i]==nodes[i+1]:
                return []
            u,v=nodes[i],nodes[i+1]
            edges.append((u,v) if not zero_based else (u-1,v-1))
        return edges

    @staticmethod
    def tree_with_diameter(n:int,diameter:int,zero_based=False,rng=None)->List[Tuple[int,int]]:
        if rng is None:
            rng=get_secure_random()
        diameter=min(diameter,n-1)
        path=list(range(1,diameter+2))
        rng.shuffle(path)
        edges=[]
        for i in range(diameter):
            a,b=path[i],path[i+1]
            edges.append((a,b) if not zero_based else (a-1,b-1))
        next_node=diameter+2
        while len(edges)<n-1:
            attach=rng.randint(0,diameter)
            a,b=path[attach],next_node
            edges.append((a,b) if not zero_based else (a-1,b-1))
            next_node+=1
        rng.shuffle(edges)
        return edges
    
    @staticmethod
    def chain_tree(n:int,zero_based=False)->List[Tuple[int,int]]:
        if zero_based:
            return [(i-2,i-1) for i in range(2,n+1)]
        return [(i-1,i) for i in range(2,n+1)]
    

if __name__ == "__main__":
    print(gen_graphs.tree(5,zero_based=True))
    print(gen_graphs.simple_graph(6,8))
    print(gen_graphs.weighted_graph(5,6,1,10))
    print(gen_graphs.dag(6,7))
    print(gen_graphs.star(5,center=3))
