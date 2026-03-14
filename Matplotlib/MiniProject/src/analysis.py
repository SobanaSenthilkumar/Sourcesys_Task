import numpy as np

def perform_analysis(df):

    print("\nStatistical Analysis")

    math_avg = np.mean(df["math"])
    sci_avg = np.mean(df["science"])
    eng_avg = np.mean(df["english"])

    print("Average Math:", math_avg)
    print("Average Science:", sci_avg)
    print("Average English:", eng_avg)

    top_student = df.loc[df["total"].idxmax()]

    print("\nTop Student:")
    print(top_student)