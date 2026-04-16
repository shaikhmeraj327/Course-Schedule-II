from collections import deque
from typing import List


def find_course_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses

    for course, prerequisite in prerequisites:
        if not (0 <= course < num_courses and 0 <= prerequisite < num_courses):
            return []
        graph[prerequisite].append(course)
        indegree[course] += 1

    queue = deque(i for i in range(num_courses) if indegree[i] == 0)
    order: List[int] = []

    while queue:
        current = queue.popleft()
        order.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == num_courses else []


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    return find_course_order(numCourses, prerequisites)


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return find_course_order(numCourses, prerequisites)
