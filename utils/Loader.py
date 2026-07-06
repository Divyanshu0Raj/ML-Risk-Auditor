import pandas as pd


def load_dataset(uploaded_file):

    file_name = uploaded_file.name
    extension = file_name.split(".")[-1].lower()

    if extension == "csv":
        return pd.read_csv(uploaded_file)

    elif extension == "tsv":
        return pd.read_csv(uploaded_file, sep="\t")

    elif extension == "json":
        return pd.read_json(uploaded_file)

    elif extension == "parquet":
        return pd.read_parquet(uploaded_file)

    elif extension in ["xlsx", "xls"]:
        return pd.read_excel(uploaded_file)

    else:
        raise ValueError(f"Unsupported file type: {extension}")