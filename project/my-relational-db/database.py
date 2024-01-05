

class Database:
    def __init__(self, tables):
        self.tables = tables
    
    def __repr__(self):
        return f"<Database> tables: \n{[table.name for table in self.tables]}"
    

class Table:
    def __init__(self, name:str, column_names=[], data=None):
        self.name = name
        self.column_names = column_names
        self.num_rows = 0
        self.id_col_idx = 0
        self.last_primary_id = 0 # what value does last row have
        if data is None:
            self.data = []
        else:
            self.data = data


    def insert(self, data_dict):
        new_row = [None] * len(self.column_names)

        if self.column_names[0] not in data_dict:
            self.last_primary_id += 1
            new_row[0] = self.last_primary_id

        for col_name, val in data_dict.items():
            col_idx = self.column_names.index(col_name)
            if col_name not in self.column_names:
                print(f"{col_name} does not match any column name")
                raise Exception
            
            new_row[col_idx] = val
            
        self.num_rows += 1
        self.data.append(new_row)


    def select(self, col_names):
        if col_names == "*":
            return [self.column_names] + self.data
        
        indecies = [i for i, col_name in enumerate(self.column_names) if col_name in col_names]
        result_data = [col_names] + [[row[idx] for idx in indecies] for row in self.data]
        return result_data

    def eq(self):
        pass

    def alter(self):
        pass

    def delete(self):
        pass

    def __repr__(self):
        return f"<Table> {self.name}; \ncolumns: {self.column_names}; \n{self.num_rows} rows"
