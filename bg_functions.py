

def category_combine(df, columns=None, final_column=None):
    """Combine multiple one-hot encoded columns into one single column. 
    Columns in the columns list that do not match the final column 
    will be dropped from the df.
    
    df: Dataframe containing the data.
    columns: List of columns to be combined.
    final_column: Column that the rest of the columns will be combined into.
    """
    for col in columns:
        if col != final_column:
            for i, row in df.iterrows():
                if df.at[i, col] == 1:
                    df.at[i, final_column] = 1
            df.drop(columns=col, inplace=True)