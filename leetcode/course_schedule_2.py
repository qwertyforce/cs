#https://leetcode.com/problems/course-schedule-ii/
# Topological sort (Kahn's algorithm)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        in_degree = [0]*numCourses
        for _to, _from in prerequisites:
            adj_list[_from].append(_to)
            in_degree[_to]+=1
        queue=[idx for idx,val in enumerate(in_degree) if val==0]
        ans=[]
        while(queue):
            node = queue.pop()
            ans.append(node)
            for _to in adj_list[node]:
                in_degree[_to]-=1
                if in_degree[_to] == 0:
                    queue.insert(0, _to)

        if len(ans)!=numCourses:
            return []
        else:
            return ans