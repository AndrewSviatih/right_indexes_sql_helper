class Column:
    def __init__(self):
        self.moreLessThan = 0
        self.equal = 0

    def __repr__(self):
        return f"{self.moreLessThan} and {self.equal})"

class Table:
    def __init__(self):
        self.columns = {}

    def add_column(self, column_name: str):
        self.columns[column_name] = Column()

    def __repr__(self):
        return f"columns={self.columns})"

class QueriesTables:
    def __init__(self):
        self.tables = {}

    def add_table(self, table_name: str):
        self.tables[table_name] = Table()

    def add_column(self, table_name: str, column_name: str):
        if table_name in self.tables:
            self.tables[table_name].add_column(column_name)
        else:
            raise ValueError(f"Table {table_name} does not exist")

    def __repr__(self):
        return f"QueriesTables(tables={self.tables})"
