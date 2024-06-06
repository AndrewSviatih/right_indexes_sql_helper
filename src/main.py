import pandas as pd
import queriesTable
import selectsProccesing
#import create_queries_df

#df = create_queries_df.create_queries_df()

# Create an instance of QueriesTables
queries_cnt = queriesTable.QueriesTables()

# Run the queries_counter function
queries_cnt = selectsProccesing.queries_counter(queries_cnt)

# Print the result
print(queries_cnt)