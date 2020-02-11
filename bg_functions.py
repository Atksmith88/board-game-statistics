

def category_combine(df, columns=None, final_column=None):
    """Combine multiple one-hot encoded columns into one single column. 
    Columns in the columns list that do not match the final column 
    will be dropped from the df.
    
    df: Dataframe containing the data.
    columns: List of columns to be combined.
    final_column: Column that the rest of the columns will be combined into.
    """
    df[final_column] = df.apply(lambda x: 1 if any(x[col] == 1
                                for col in columns) else 0, axis=1)
    if final_column in columns:
        columns.remove(final_column)
    df.drop(columns=columns, inplace=True)
    