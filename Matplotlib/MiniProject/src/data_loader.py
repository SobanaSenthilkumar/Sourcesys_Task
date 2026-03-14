import pandas as pd

def load_data(path):

    df = pd.read_csv(path)

    print("\nDataset Loaded")
    print(df.head())

    return df