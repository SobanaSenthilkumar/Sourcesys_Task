import numpy as np
def calculate_revenue(data):
    
    price = data[:, 1]
    quantity = data[:, 2]
    discount = data[:, 3]

    total_price = price * quantity
    final_price = total_price - (total_price * discount / 100)

    return final_price


def normalize_data(values):
   
    return (values - np.min(values)) / (np.max(values) - np.min(values))


def rank_orders(revenue, top_n=5):
    
    return np.argsort(revenue)[-top_n:][::-1]


def statistics(revenue):
    
    print("\n Revenue Statistics")
    print("Total Revenue:", np.sum(revenue))
    print("Average Revenue:", np.mean(revenue))
    print("Maximum Revenue:", np.max(revenue))
    print("Minimum Revenue:", np.min(revenue))
    print("Standard Deviation:", np.std(revenue))