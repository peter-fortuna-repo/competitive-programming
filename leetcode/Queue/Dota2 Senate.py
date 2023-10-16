# Link to problem: https://leetcode.com/problems/dota2-senate

 

# Solution:
# The most efficient strategy is to block the next person to vote. We 
# can simulate this strategy iteratively by tracking which senators make it to
# the next round in a queue, and repeat this until only senators from one party
# are left. Each round elemenates half the senators, resulting in an O(nlog(n))
# runtime.

# Time complexity: O(nlog(n)) 
# Space complexity: O(n)

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        num_radiants_to_ban = 0
        num_dires_to_ban = 0

        voting_round = [senator for senator in senate]
        next_round = []

        while voting_round.count("D") > 0 and voting_round.count("R") > 0:
            for senator in voting_round:
                if senator == "R":
                    if num_radiants_to_ban > 0:
                        num_radiants_to_ban -= 1
                    else:
                        num_dires_to_ban += 1
                        next_round.append("R")
                else:
                    if num_dires_to_ban > 0:
                        num_dires_to_ban -= 1
                    else:
                        num_radiants_to_ban += 1
                        next_round.append("D")

            voting_round, next_round = next_round, []
        if voting_round.count("R") > 0:
            return "Radiant"
        return "Dire"