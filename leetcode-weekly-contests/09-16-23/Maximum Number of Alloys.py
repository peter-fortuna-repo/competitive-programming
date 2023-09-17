# You are the owner of a company that creates alloys using various types of 
# metals. There are n different types of metals available, and you have access
# to k machines that can be used to create alloys. Each machine requires a 
# specific amount of each metal type to create an alloy.

# For the ith machine to create an alloy, it needs composition[i][j] units of 
# metal of type j. Initially, you have stock[i] units of metal type i, and 
# purchasing one unit of metal type i costs cost[i] coins. Given integers n, k, 
# budget, a 1-indexed 2D array composition, and 1-indexed arrays stock and 
# cost, your goal is to maximize the number of alloys the company can create 
# while staying within the budget of budget coins.
# All alloys must be created with the same machine.

# Return the maximum number of alloys that the company can create.

# Solution 1: Brute force 
# Move through each machine and compute the maximum number of alloys it can 
# create. This algorithm creates alloys one at a time and decrements resources.
# This approach is simple but inefficient, as budget can go up to 10**8.

# Time complexity: O(n * budget)
# Space complexity: O(n)

def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
    max_num_alloys = 0
    for machine in composition:
        num_alloys = self.getMaxProduction(machine, budget, stock.copy(), cost)
        max_num_alloys = max(max_num_alloys, num_alloys)
    return max_num_alloys
        
def getMaxProduction(self, machine, budget, stock, cost):
        production = 0
        while True:
            for i, metal_needed in enumerate(machine):
                stock[i] -= metal_needed
                if stock[i] < 0:
                    budget += cost[i] * stock[i]
                    stock[i] = 0
            if budget < 0:
                return production
            production += 1


# Solution 2: Hashmap
# We can bring the runtime down to O(nk) with a hashmap. A hashmap is created
# for each machine that identifies the bottlenecks in its alloy making process.
# We track how many alloys can be produced before running out of each metal. We
# are then able to calculate the cost at each bottleneck, which increases as 
# more metals are neaded. We produce as many metals as we can before running 
# out of money or hitting another bottleneck, and then return the total amount 
# produced.

# Time complexity: O(nk)
# Space complexity: O(k)

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        max_production = 0
        for machine in composition:
            hashmap_costs = self.getHashmapCosts(machine, stock)
            production = self.getProduction(hashmap_costs, machine, budget, stock, cost)
            max_production = max(max_production, production)
        return max_production
    
    def getHashmapCosts(self, machine, stock):
        hashmap_costs = {}
        for i, metal in enumerate(machine):
            num_can_produce = stock[i] // metal
            if num_can_produce not in hashmap_costs.keys():
                hashmap_costs[num_can_produce] = []
            hashmap_costs[num_can_produce].append(i)
        return hashmap_costs

    def getProduction(self, hashmap_costs, machine, budget, stock, cost):
        bottlenecks = list(hashmap_costs.keys())
        bottlenecks.sort()
        production = bottlenecks[0]
        total_cost_per_alloy = 0
        for i, bottleneck in enumerate(bottlenecks):
            metals = hashmap_costs[bottleneck]
            total_cost_per_alloy += sum([cost[metal]*machine[metal] for metal in metals])
            budget -= total_cost_per_alloy 
            budget += sum([cost[metal] * (stock[metal]%machine[metal]) for metal in metals])
            production += 1
            if budget < 0:
                return production - 1
            if i+1 < len(bottlenecks):
                num_possible_at_cost = bottlenecks[i+1] - bottlenecks[i] - 1
                num_produced_at_cost = min(num_possible_at_cost, budget // total_cost_per_alloy)
                budget -= num_produced_at_cost * total_cost_per_alloy
                production += num_produced_at_cost
                
        if budget > 0:
            production += budget // total_cost_per_alloy
        return production