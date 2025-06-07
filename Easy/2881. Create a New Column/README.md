# 2881. Create a New Column

## Problem Description

You are given a DataFrame called `employees`.  
Write a solution to **create a new column named `bonus`** that contains double the values from the `salary` column.

---

## Example

**Input DataFrame:**

| name    | salary |
|---------|--------|
| Piper   | 4548   |
| Grace   | 28150  |
| Georgia | 1103   |
| Willow  | 6593   |
| Finn    | 74576  |
| Thomas  | 24433  |

**Output DataFrame:**

| name    | salary | bonus  |
|---------|--------|--------|
| Piper   | 4548   | 9096   |
| Grace   | 28150  | 56300  |
| Georgia | 1103   | 2206   |
| Willow  | 6593   | 13186  |
| Finn    | 74576  | 149152 |
| Thomas  | 24433  | 48866  |

---

## Function Signature

```python
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame: