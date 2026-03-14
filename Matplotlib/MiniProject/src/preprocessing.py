def preprocess_data(df):

    # Convert column names to lowercase
    df.columns = df.columns.str.lower()

    # Calculate total marks
    df["total"] = df["math"] + df["science"] + df["english"]

    # Calculate average
    df["average"] = df["total"] / 3

    print("\nPreprocessing Completed")

    return df