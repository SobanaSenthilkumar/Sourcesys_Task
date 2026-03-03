
import numpy as np

def generate_data(orders=1000):
    
    np.random.seed(42)

    order_ids = np.arange(1, orders + 1)
    price = np.random.randint(100, 5000, orders)
    quantity = np.random.randint(1, 6, orders)
    discount = np.random.randint(0, 31, orders)

    data = np.column_stack((order_ids, price, quantity, discount))

    return data