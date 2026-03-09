from src.data_loader import load_dataset
from src.preprocessing import clean_data, preprocess_data
from src.analysis import filtering_data, sorting_data, analysis_summary, grouping_analysis


def main():

    print("\nRetail Sales Analysis Project\n")

    # Load dataset
    df = load_dataset(r"C:\Users\VICKY\OneDrive\Desktop\Sourcesys\MiniProject-Retail_Sales_Analysis_Project\superstore.csv")

    # Data cleaning
    df = clean_data(df)

    # Data preprocessing
    df = preprocess_data(df)

    # Filtering
    filtering_data(df)

    # Sorting
    sorting_data(df)

    # Analysis
    analysis_summary(df)

    # Grouping
    grouping_analysis(df)

    print("\nProject Completed Successfully")


if __name__ == "__main__":
    main()