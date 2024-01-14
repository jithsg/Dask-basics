from __future__ import annotations
import time

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from dask.distributed import Client

def multiple_by_two(x: int) -> int:
    time.sleep(1)
    return x * 2

futures= []
# start = time.time()
# with ProcessPoolExecutor(max_workers=10) as executor:
#     for x in range(10):
#         future = executor.submit(multiple_by_two, x)
        
#         futures.append(future)
#         print(future.running())
#     outputs = [future.result() for future in futures]
# end = time.time()

# print(f"Time taken: {end - start}")

# if __name__ == "__main__":
#     client = Client()
#     features=[]
#     start = time.time()
    
#     for x in range(10):
#         future = client.submit(multiple_by_two, x)
#         features.append(future)
#     outputs = [future.result() for future in features]
#     end = time.time()
#     print(f"Time taken: {end - start}")


# if __name__ == "__main__":
#     client = Client()
#     start= time.time()
#     inputs=list(range(10))

#     futures = client.map(multiple_by_two, inputs)
#     outputs = client.gather(futures)
#     end = time.time()
#     print(f"Time taken: {end - start}")
    
#     del futures


if __name__ == "__main__":
    client = Client(processes=False)
    start= time.time()
    inputs=list(range(10))
    remote_inputs = client.scatter(inputs)

    futures = client.map(multiple_by_two, remote_inputs)
    outputs = client.gather(futures)
    end = time.time()
    print(f"Time taken: {end - start}")
    
    del futures
    del remote_inputs
