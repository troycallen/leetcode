
class Solution:
    def minOperations(self, n: int) -> int:
        from collections import deque
        
        # upper‐bound on reachable values: allow up to 2*n
        max_val = 2 * n
        
        # precompute powers of two up to max_val
        powers = []
        p = 1
        while p <= max_val:
            powers.append(p)
            p <<= 1
        
        # standard BFS from n down to 0
        dq = deque([(n, 0)])      # (current_value, steps_so_far)
        visited = {n}
        
        while dq:
            x, steps = dq.popleft()
            if x == 0:
                return steps
            
            for pw in powers:
                # subtract pw
                nx = x - pw
                if 0 <= nx <= max_val and nx not in visited:
                    visited.add(nx)
                    dq.append((nx, steps + 1))
                
                # add pw
                nx = x + pw
                if 0 <= nx <= max_val and nx not in visited:
                    visited.add(nx)
                    dq.append((nx, steps + 1))
        
        return -1  # unreachable (theoretically shouldn't happen)