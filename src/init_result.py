import pandas as pd # type: ignore

def init_result(df):

    columns = ['WHERE']
    index = ['table']

    df = pd.DataFrame(index=index, columns=columns)

