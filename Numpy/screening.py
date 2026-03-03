import numpy as np
from data import generate_data
from utils import calculate_revenue, normalize_data, rank_orders, statistics
def main():

    print(" E-Commerce Management Using NumPy\n")


    data = generate_data(orders=1000)
    print("Dataset Shape:", data.shape)

    revenue = calculate_revenue(data)

    
    normalized_revenue = normalize_data(revenue)

    print("\nMemory Usage (MB):", normalized_revenue.nbytes / 1024 / 1024)

    top_orders = rank_orders(revenue)

    print("\n Top Order Indexes:", top_orders)
    print("Top Revenues:", revenue[top_orders])

   
    statistics(revenue)

    print("\n E-Commerce Analysis Completed Successfully")


if __name__ == "__main__":
    main()