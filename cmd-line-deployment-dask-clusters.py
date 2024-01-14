import dask.array as da
from dask.distributed import Client

def main() -> None:
    client = Client("tcp://10.34.19.118:8786")
    x = da.random.random((10000, 10000), chunks=(1000, 1000))   

    print(da.exp(x).sum().compute())


if __name__ == "__main__":
    main()