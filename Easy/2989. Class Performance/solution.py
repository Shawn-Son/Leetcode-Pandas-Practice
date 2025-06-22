import pandas as pd

def class_performance(scores: pd.DataFrame) -> pd.DataFrame:
    total_score=scores['assignment1']+scores['assignment2']+scores['assignment3']
    diff=total_score.max()-total_score.min()
    return pd.DataFrame({'difference_in_score':[diff]})