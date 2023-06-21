class Solution(object):
    def carFleet(self, target, position, speed):
        stack = []
        PosSpeed = [(position, speed)
                    for position, speed in zip(position, speed)]
        PosSpeed.sort(reverse=True)  # Sorting by position and reversing

        for position, speed in PosSpeed:
            stack.append(float(target - position) / speed)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
