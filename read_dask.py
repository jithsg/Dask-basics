import dask
import dask.dataframe as dd

df = dd.read_csv('Twitter_Data.csv', assume_missing=True)

df = df.repartition(npartitions=2)
df.to_parquet('Twitter_Data.parquet')
print(df.npartitions)
