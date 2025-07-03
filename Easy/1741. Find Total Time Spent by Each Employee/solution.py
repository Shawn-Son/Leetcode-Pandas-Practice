import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['time']=employees['out_time']-employees['in_time']
    result=employees.groupby(['emp_id','event_day'])['time'].sum().reset_index().rename(columns={'event_day':'day','time':'total_time'})
    return result[['day','emp_id','total_time']]