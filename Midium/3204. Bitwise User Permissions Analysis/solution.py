import pandas as pd
import numpy as np

def analyze_permissions(user_permissions: pd.DataFrame) -> pd.DataFrame:
    common_perms=np.bitwise_and.reduce(user_permissions['permissions'])
    any_perms=np.bitwise_or.reduce(user_permissions['permissions'])
    return pd.DataFrame({'common_perms':[common_perms],'any_perms':[any_perms]})