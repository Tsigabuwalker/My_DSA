class Solution:
    def canCompleteCircuit(self, gas, cost):
        totalGas = 0
        totalCost = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            totalGas += gas[i]
            totalCost += cost[i]
            tank += gas[i] - cost[i]

            if tank < 0:
                start = i + 1
                tank = 0

        return start if totalGas >= totalCost else -1
