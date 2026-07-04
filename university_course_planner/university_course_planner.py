from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list
        graph = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # 0 = unvisited
        # 1 = visiting
        # 2 = visited
        state = [0] * numCourses

        def dfs(course: int) -> bool:
            if state[course] == 1:
                return False  # Cycle found

            if state[course] == 2:
                return True  # Already checked

            state[course] = 1

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            state[course] = 2
            return True

        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return False

        return True

if __name__ == "__main__":
    solution = Solution()

    print(solution.canFinish(2, [[1, 0]]))          # True
    print(solution.canFinish(2, [[1, 0], [0, 1]]))  # False