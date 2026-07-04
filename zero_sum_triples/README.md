# Three Sum

## Problem

Given an integer array `nums`, return all unique triplets `[a, b, c]` such that:

```
a + b + c = 0
```

The solution must not contain duplicate triplets.

---

## Approach

1. Sort the array.
2. Fix one number.
3. Use two pointers (`left` and `right`) to search for the other two numbers.
4. Skip duplicate values to avoid repeated triplets.

---

## Complexity

- Time: **O(n²)**
- Space: **O(1)** (excluding the output list)

---

## Example

Input:

```python
nums = [-1, 0, 1, 2, -1, -4]
```

Output:

```python
[[-1, -1, 2], [-1, 0, 1]]
```

---

## Key Takeaways

- Sorting enables the two-pointer technique.
- Move `left` when the sum is too small.
- Move `right` when the sum is too large.
- Skip duplicates to avoid repeated answers.

---

## Patterns Learned

- Sorting
- Two Pointers
- Duplicate Handling