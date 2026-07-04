# Pair Finder Problem

## Problem
Given a list of integers `nums` and an integer `target`, find two numbers in the list such that they add up to the target.

Return the indices of the two numbers.

You may assume:
- Exactly one solution exists
- You cannot use the same element twice

---

## Example

Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]

---

## Idea (Solution Approach)

We use a dictionary (hash map) to store numbers we have already seen.

For each number:
1. Compute what number we need (complement = target - num)
2. Check if we already saw that number
3. If yes → return indices
4. If no → store current number with its index

---

## Complexity

Time: O(n)  
Space: O(n)

---

## How to run

```bash
python two_sum.py