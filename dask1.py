import numpy as np
import pandas as pd 
import dask

import dask.dataframe as dd

from dask.distributed import Client

def main() -> None:
    # data_dict = {
    #     'a': np.arange(5000),
    #     'b': np.random.randn(5000),
    #     'c': np.random.choice(['a', 'b', 'c'], 5000)

    # }
    
    # df = pd.DataFrame(data_dict)
    # # print(df.head(10))

    
    # ddf = dd.from_pandas(df, npartitions=10)
    # sum_df = ddf.groupby('c').mean()
    # # sum_df = sum_df.visualize()
    
    @dask.delayed
    def increment(x: int) -> int:
        return x + 1

    @dask.delayed
    def add(x: int, y: int) -> int:
        return x + y
    
    a= increment(1)
    b = increment(2)
    c = add(a, b)
    c.visualize()
    print(c.compute())

if __name__ == "__main__":
    client= Client()
    main()