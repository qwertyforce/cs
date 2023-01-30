#https://leetcode.com/problems/course-schedule/
# Topological sort (Kahn's algorithm)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        in_degree=[0]*numCourses
        for _to, _from in prerequisites:
            adj_list[_from].append(_to)
            in_degree[_to] +=1

        queue=[idx for idx,val in enumerate(in_degree) if val==0]

        while(queue):
            at = queue.pop()
            for to in adj_list[at]:
                in_degree[to]-=1
                if in_degree[to] == 0:
                    queue.insert(0,to)
    
        return sum(in_degree) == 0