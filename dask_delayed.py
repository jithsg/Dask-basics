from __future__ import annotations
import dask, time, random 


from dask import delayed

import numpy as np

@delayed
def increment(x: int | float) -> int | float:
    return x + 1

@delayed
def double(x: int | float) -> int | float:
    return x + 2


@delayed
def add(x: int | float, y: int | float) -> int | float:
    return x + y


data = [1, 2, 3, 4, 5] 

output = []


for x in data:
    a = increment(x) 
    b =double(x) 
    c = add(a, b) 
    output.append(c) 
print(output)   
total= dask.delayed(sum)(output) 
print(total.compute())
    
