import pandas as pd

def compressed_mean(orders: pd.DataFrame) -> pd.DataFrame:
    total_item=sum(orders['item_count']*orders['order_occurrences'])
    total_orders=sum(orders['order_occurrences'])
    average=round(total_item/total_orders,2)
    return pd.DataFrame({'average_items_per_order':[average]})