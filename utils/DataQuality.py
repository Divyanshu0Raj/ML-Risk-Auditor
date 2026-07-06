def get_severity(percentage):
    if percentage == 0:
        return "Excellent"
    elif percentage <= 5:
        return "Low"
    elif percentage <= 20:
        return "Medium"
    elif percentage <= 50:
        return "High"
    elif percentage <= 70:
        return "Critical"
    else:
        return "Extreme"


def get_recommendation(issue_type: str, percentage: float = 0) -> str:
    issue_type = issue_type.lower()

    if issue_type == "missing":

        if percentage == 0:
            return "No action required."

        elif percentage <= 5:
            return "Use simple imputation (Mean / Median / Mode)."

        elif percentage <= 20:
            return "Investigate missing values and use suitable imputation."

        elif percentage <= 50:
            return "Consider advanced imputation or dropping the feature."

        elif percentage <= 80:
            return "Drop this feature unless it has strong business value."

        else:
            return "Strongly recommended to remove this column."

    elif issue_type == "duplicate":

        if percentage == 0:
            return "No duplicate rows found."

        elif percentage <= 5:
            return "Remove duplicate rows."

        else:
            return "Investigate duplicate generation process before removing."

    elif issue_type == "constant":

        return "Remove this column. It contains no useful information."

    elif issue_type == "high_cardinality":

        if percentage <= 50:
            return "Review whether encoding is required."

        elif percentage <= 90:
            return "Consider Target Encoding or Frequency Encoding."

        else:
            return "Likely an identifier. Remove before model training."

    elif issue_type == "identifier":

        return "Exclude this feature from training unless it has business importance."

    elif issue_type == "empty":

        return "Drop this column immediately."

    return "Review this feature manually."


def get_duplicate_report(df, total_rows):

    duplicated_count = df.duplicated().sum()
    duplicated_percentage = (
        (duplicated_count / total_rows) * 100 if total_rows else 0
    )

    return {
        "duplicated_count": duplicated_count,
        "duplicated_percentage": round(duplicated_percentage, 2),
        "severity": get_severity(duplicated_percentage),
        "recommendation": get_recommendation(
            "duplicate",
            duplicated_percentage
        )
    }


def get_missing_report(df, total_rows):

    missing_report = {}

    raw_missing_data = df.isna().sum()

    for col in df.columns:

        missing_count = raw_missing_data[col]

        missing_percentage = (
            (missing_count / total_rows) * 100 if total_rows else 0
        )

        missing_report[col] = {
            "missing_count": missing_count,
            "missing_percentage": round(missing_percentage, 2),
            "severity": get_severity(missing_percentage),
            "recommendation": get_recommendation(
                "missing",
                missing_percentage
            )
        }

    return missing_report


def get_constant_column_report(df):

    constant_columns = {}

    for col in df.columns:

        if df[col].nunique(dropna=False) == 1:

            constant_columns[col] = {
                "severity": "High",
                "recommendation": get_recommendation("constant")
            }

    return constant_columns


def get_high_cardinality_report(df, total_rows):

    high_cardinality_report = {}

    for col in df.columns:

        unique_count = df[col].nunique()

        unique_percentage = (
            (unique_count / total_rows) * 100 if total_rows else 0
        )

        high_cardinality_report[col] = {
            "unique_count": unique_count,
            "unique_percentage": round(unique_percentage, 2),
            "severity": get_severity(unique_percentage),
            "recommendation": get_recommendation(
                "high_cardinality",
                unique_percentage
            )
        }

    return high_cardinality_report


def get_identifier_report(df, total_rows):

    high_cardinality = get_high_cardinality_report(df, total_rows)

    identifiers = {}

    keywords = [
        "id",
        "identifier",
        "email",
        "phone",
        "mobile",
        "passport",
        "uuid"
    ]

    for col in df.columns:

        column_name = col.lower()

        is_high_unique = (
            high_cardinality[col]["unique_percentage"] >= 90
        )

        is_identifier_name = any(
            keyword in column_name
            for keyword in keywords
        )


        if is_high_unique and is_identifier_name :

            identifiers[col] = {
                "unique_percentage":
                    high_cardinality[col]["unique_percentage"],
                "severity": "Extreme",
                "recommendation":
                    get_recommendation("identifier")
            }

    return identifiers


def get_empty_columns(df, total_rows):

    empty_columns = {}

    for col in df.columns:

        if df[col].isna().all():

            empty_columns[col] = {
                "empty_percentage": 100,
                "severity": get_severity(100),
                "recommendation": get_recommendation("empty")
            }

    return empty_columns


def check_data_quality(df):

    total_rows = len(df)

    return {

        "missing":
            get_missing_report(df, total_rows),

        "duplicates":
            get_duplicate_report(df, total_rows),

        "constant_columns":
            get_constant_column_report(df),

        "high_cardinality_columns":
            get_high_cardinality_report(df, total_rows),

        "identifiers":
            get_identifier_report(df, total_rows),

        "empty_columns":
            get_empty_columns(df, total_rows)
    }