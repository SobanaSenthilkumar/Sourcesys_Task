import pandas as pd


def filtering_data(df):

    print("\nFiltering High Sales Orders")

    high_sales = df[df["sales"] > 500]

    print(high_sales.head())

    return high_sales


def sorting_data(df):

    print("\nSorting by Sales")

    sorted_sales = df.sort_values(by="sales", ascending=False)

    print(sorted_sales.head())

    return sorted_sales


def analysis_summary(df):

    print("\nSales Summary")

    total_sales = df["sales"].sum()
    avg_sales = df["sales"].mean()
    total_profit = df["profit"].sum()

    print("Total Sales:", total_sales)
    print("Average Sales:", avg_sales)
    print("Total Profit:", total_profit)


def grouping_analysis(df):

    print("\nSales by Region")

    sales_region = df.groupby("region")["sales"].sum()

    print(sales_region)

    print("\nProfit by Category")

    profit_category = df.groupby("category")["profit"].sum()

    print(profit_category)

    print("\nMonthly Sales")

    monthly_sales = df.groupby("order_month")["sales"].sum()

    print(monthly_sales)