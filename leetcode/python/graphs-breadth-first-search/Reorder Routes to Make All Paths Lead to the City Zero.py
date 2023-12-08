# Link to problem: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero

# Solution: 
# This solution uses a depth first search. To make the graph data easier to 
# navigate, we first convert the list of connections into two dictionaries, one
# of incoming edges and one of outgoing edges. The DFS is performed moving from
# the root to all incoming and outgoing edges. The flip count is increased for 
# each incoming edge. To stop the algorithm for visiting edges mutliple times, 
# each edge is removed from both dictionaries after being used.

# Time complexity: O(n)  
# Space complexity: O(n) 

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        outgoing_edges = {}
        incoming_edges = {}

        for i in range(n):
            outgoing_edges[i] = []
            incoming_edges[i] = []

        for connection in connections:
            outgoing_edges[connection[0]].append(connection[1])
            incoming_edges[connection[1]].append(connection[0])
        
        num_flipped = 0
        to_visit = [0]
        next_layer = []
        while to_visit:
            for node in to_visit:
                next_layer += outgoing_edges[node]
                num_flipped += len(outgoing_edges[node])
                for edge in outgoing_edges[node]:
                    incoming_edges[edge].remove(node)
                
                next_layer += incoming_edges[node]
                for edge in incoming_edges[node]:
                    outgoing_edges[edge].remove(node)

            to_visit = next_layer
            next_layer = []

        return num_flipped