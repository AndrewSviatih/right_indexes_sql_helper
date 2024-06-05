import pandas as pd 

def create_queries_df() -> pd.DataFrame:
    columns = ['table', 'column', '> or <', '=']
    df = pd.DataFrame(columns=columns)

    return df