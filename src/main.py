import pandas as pd
import queriesTable
import selectsProccesing
#import create_queries_df

#df = create_queries_df.create_queries_df()

queries_table = queriesTable.QueriesTables()

selectsProccesing.queries_counter(queriesTable)

print(queries_table)