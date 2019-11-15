"""
@lc id=207 lang=python3.7.4 tag=graph,cycle

[207] Course Schedule I

There are a total of `n` courses you have to take, labeled from 0..n-1

Some courses may have prerequisites. For example, to take course 0, you have
to first take course 1, which is expressed as a pair: `[0, 1]`.

Given the total number of courses and a list of prerequisite pairs,
return if it is possible to finish all `n` courses.

Constraints:
    - Assume there are no duplicate edges in the input prerequisites.
    - Note that input prerequisites is a graph represented by an edge list, and not adj matrix.

Example 1:
    Input: n=2, prereqs=[[1,0]]
    Output: true
    Explanation: 2 courses to take, 0 and 1. To take course 1, you should have finished course 0.
                 Since there are no prerequisites for course 0, you can take 0, 1, so it is possible.

Example 2:
    Input: n=2, prereqs=[[1,0], [0, 1]]
    Output: false
    Explanation: 2 courses to take, 0 and 1. To take course 1, you should have finished course 0.
                 To take course 0, you need to have finished course 1, so it is impossible.

Complexity:
    Time: O(V + E) for each V, we spend constant amount of time per vertice's edge.
    Space: O(V * E) for adj list, worst in a complete graph. Recursion, stack, visited each O(V).
"""


from typing import List


class Solution:
    """
    Leetcode submission beats 99.7% python3 submissions: 89ms over 42 test cases.
    """

    @staticmethod
    def can_finish(self, courses_cnt: int, prereqs: List[List[int]]) -> bool:
        if courses_cnt <= 1 or len(prereqs) <= 1:
            return True

        # Transform edge list to adjacency list representation.
        adj_list = [list() for _ in range(courses_cnt)]
        for [v, u] in prereqs:
            adj_list[u].append(v)

        # `visited` keeps track of already visited vertices.
        visited = [False] * courses_cnt
        # `stack` keeps track of visiting vertices during a specific DFS,
        # and gets reset once the cycle is not found from that vertex.
        stack = [False] * courses_cnt

        def has_cycle(cur):
            """ DFS to see if we return to same node, meaning cycle. """
            visited[cur], stack[cur] = True, True
            for adj in adj_list[cur]:
                if not visited[adj]:
                    if has_cycle(adj):
                        return True
                elif stack[adj]:
                    return True
            stack[cur] = False
            return False

        # Check for a cycle from each course.
        for course_id in range(len(adj_list)):
            if not visited[course_id] and has_cycle(course_id):
                return False  # cycle means cannot complete all courses

        # No cycle, so can complete all courses.
        return True
