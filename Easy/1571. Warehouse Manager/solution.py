import pandas as pd

def warehouse_manager(warehouse: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    products['products_volume']=products['Width']*products['Length']*products['Height']
    wp=warehouse.merge(products,on='product_id')
    wp['total_volume']=wp['products_volume']*wp['units']
    result=wp.groupby('name')['total_volume'].sum().reset_index().rename(columns={'name':'warehouse_name','total_volume':'volume'})
    return result[['warehouse_name','volume']]