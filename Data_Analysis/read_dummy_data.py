import pandas as pd
import os

DUMP_FILE = os.path.join("dummy_data.pkl")

dataframes = pd.read_pickle(DUMP_FILE)

print(dataframes['users'])
print(dataframes['view_counts'])