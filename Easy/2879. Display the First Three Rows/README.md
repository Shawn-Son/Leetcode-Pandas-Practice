# 2879. Display the First Three Rows

## Problem Description

You are given a DataFrame named `employees`.  
Write a solution to **display only the first three rows** of this DataFrame.

---

## Example

**Input DataFrame:**

| employee_id | name      | department            | salary |
|-------------|-----------|-----------------------|--------|
| 3           | Bob       | Operations            | 48675  |
| 90          | Alice     | Sales                 | 11096  |
| 9           | Tatiana   | Engineering           | 33805  |
| 60          | Annabelle | InformationTechnology | 37678  |
| 49          | Jonathan  | HumanResources        | 23793  |
| 43          | Khaled    | Administration        | 40454  |

**Output DataFrame:**

| employee_id | name    | department  | salary |
|-------------|---------|-------------|--------|
| 3           | Bob     | Operations  | 48675  |
| 90          | Alice   | Sales       | 11096  |
| 9           | Tatiana | Engineering | 33805  |

---

## Function Signature

```python
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame: