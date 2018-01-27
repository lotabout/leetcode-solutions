#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class SolutionTLE:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        graph = {}
        for a, b in prerequisites:
            if a in graph:
                graph[a].add(b)
            else:
                graph[a] = set([b])

        for course in graph:
            if self.contains_loop(graph, course):
                return False
        return True

    def contains_loop(self, graph, node, visited = set()):
        if node in visited:
            return True

        if node not in graph:
            return False

        visited.add(node)
        for prerequisite in graph[node]:
            if self.contains_loop(graph, prerequisite, visited):
                visited.remove(node)
                return True
        visited.remove(node)
        return False

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        graph = {}
        backref = {}
        for a, b in prerequisites:
            if a in graph:
                graph[a].add(b)
            else:
                graph[a] = set([b])

            if b in backref:
                backref[b].add(a)
            else:
                backref[b] = set([a])
        # print("backref: ", backref)

        available_courses = set(range(numCourses)) - graph.keys()

        while len(available_courses) > 0:
            new_available_courses = set()

            for course in available_courses:
                # print("eliminate course: ", course)
                # print("before: ", graph)
                for n in backref.get(course, set()):
                    if n in graph:
                        graph[n].remove(course)
                        if len(graph[n]) == 0:
                            new_available_courses.add(n)
                # print("after: ", graph)

            available_courses = new_available_courses

        for course in graph:
            if len(graph[course]) > 0:
                return False
        return True

solution = Solution()

assert solution.canFinish(2, [[1, 0]])
assert not solution.canFinish(2, [[1, 0], [0, 1]])
assert not solution.canFinish(3, [[1,0],[1,2],[0,1]])
assert solution.canFinish(3, [[0,1],[0,2],[1,2]])
