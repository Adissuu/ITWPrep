class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        total_distance = 0
        distance = 0
        while mainTank > 0:
            distance = min(mainTank, 5) * 10
            total_distance += distance

            mainTank -= 5

            if (additionalTank >= 1) and (distance == 50):
                transferred_fuel = min(1, additionalTank)
                mainTank += transferred_fuel
                additionalTank -= transferred_fuel
        return total_distance
