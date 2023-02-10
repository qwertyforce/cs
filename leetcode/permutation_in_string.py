class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter(s1)
        window_map = defaultdict(int)
        need = len(s1_map)
        l=0
        
        for i in range(0, len(s2)):
            if i>=len(s1):
                window_map[s2[l]]-=1
                if s2[l] in s1_map:
                    if s1_map[s2[l]] == window_map[s2[l]]:
                        need-=1
                    if s1_map[s2[l]] == window_map[s2[l]]+1:
                        need+=1
                l+=1

            window_map[s2[i]]+=1
            if s2[i] in s1_map:
                if s1_map[s2[i]] == window_map[s2[i]]:
                    need-=1
                if s1_map[s2[i]] == window_map[s2[i]]-1:
                    need+=1

            if need==0:
                return True
            
        return False
