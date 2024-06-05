import os
import glob
import queriesTable
import pandas as pd

def queries_counter(queries_cnt: queriesTable.QueriesTables):

    directory = '../put_queries_here/'
    text_files = glob.glob(os.path.join(directory, '*.txt *.sql *.log'))

    for file_path in text_files:
        with open(file_path, 'r') as file:
            content = file.read()
            queries = content.split(';')

            for query in queries:
                FROM_index = query.upper().find('FROM')
                if FROM_index != -1:
                    from_clause = query[FROM_index + 5:] #skip FROM + space
                    table_name = from_clause.split()[0].strip()  # Get the table name after FROM
                    if table_name not in queries_cnt.tables:
                        queries_cnt.add_table(table_name)

                WHERE_index = query.upper().find('WHERE')
                
                if WHERE_index != -1:
                    where_clause = query[WHERE_index + 5:]
                    for keyword in ['>', '<', '=']:
                        keyword_index = where_clause.upper().find(keyword)
                        if keyword_index != -1:
                            if where_clause[:keyword_index] not in queries_cnt.tables:
                                queries_cnt.add_column(table_name, where_clause[:keyword_index])
                            if keyword in ['>', '<']:
                                queries_cnt.tables[table_name].columns[where_clause[:keyword_index]].moreLessThan += 1
                            else:
                                queries_cnt.tables[table_name].columns[where_clause[:keyword_index]].equal += 1
                            break



