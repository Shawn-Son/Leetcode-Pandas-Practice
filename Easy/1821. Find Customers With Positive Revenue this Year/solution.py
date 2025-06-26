import pandas as pd

def find_customers(customers: pd.DataFrame) -> pd.DataFrame:
    pos=customers[(customers.year==2021) & (customers.revenue>0)]
    return pos[['customer_id']]