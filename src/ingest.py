import pandas as pd

def ingest(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(df)
    return df