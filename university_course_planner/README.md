# Course Planner

## Problem

Given `numCourses` courses and a list of prerequisite pairs, determine whether all courses can be completed.

A prerequisite `[a, b]` means course `b` must be completed before course `a`.

---

## Approach

Model the courses as a directed graph.

Use Depth-First Search (DFS) with three states:

- 0 → Unvisited
- 1 → Visiting
- 2 → Visited

If DFS reaches a node that is already in the **Visiting** state, a cycle exists, making it impossible to complete all courses.

Nodes marked as **Visited** are skipped in future searches since they have already been verified to contain no cycles.

---

## Algorithm

1. Build an adjacency list.
2. Initialize a state array.
3. Run DFS from each unvisited course.
4. Return `False` if a cycle is detected.
5. Otherwise return `True`.

---

## Time Complexity

- **O(V + E)**

where:

- `V` = number of courses
- `E` = number of prerequisite pairs

---

## Space Complexity

- **O(V + E)**

for the graph, state array, and recursion stack.