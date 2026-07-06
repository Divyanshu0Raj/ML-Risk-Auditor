import pandas as pd

def get_dataset_summary(df):

    rows=df.shape[0]
    cols=df.shape[1]
    missing_data=df.isnull().sum()
    duplicate_data=df.duplicated().sum()
    numeric_cols=df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols=df.select_dtypes(include=['object']).columns.tolist()
    boolean_cols=df.select_dtypes(include=['bool']).columns.tolist()
    date_cols = df.select_dtypes(include=["datetime"]).columns.tolist()
    total_missing=missing_data.sum().sum()
    total_duplicated=duplicate_data.sum().sum()


    summary={
        "rows":rows,
        "cols":cols,
        "missing_data":missing_data,
        "duplicate_data":duplicate_data,
        "numeric_cols":numeric_cols,
        "categorical_cols":categorical_cols,
        "boolean_cols":boolean_cols,
        "date_cols":date_cols,
        "total_missing":total_missing,
        "total_duplicated":total_duplicated
    }

    return summary