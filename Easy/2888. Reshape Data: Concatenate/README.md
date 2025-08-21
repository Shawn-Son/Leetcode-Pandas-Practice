# 2888. Reshape Data: Concatenate

## Problem
Given two DataFrames `df1` and `df2`, concatenate them **vertically** (row-wise) into a single DataFrame.

---

## Example

### Input
**df1**

| student_id | name    | age |
|------------|---------|-----|
| 1          | Mason   | 8   |
| 2          | Ava     | 6   |
| 3          | Taylor  | 15  |
| 4          | Georgia | 17  |

**df2**

| student_id | name | age |
|------------|------|-----|
| 5          | Leo  | 7   |
| 6          | Alex | 7   |

### Output

| student_id | name    | age |
|------------|---------|-----|
| 1          | Mason   | 8   |
| 2          | Ava     | 6   |
| 3          | Taylor  | 15  |
| 4          | Georgia | 17  |
| 5          | Leo     | 7   |
| 6          | Alex    | 7   |

---