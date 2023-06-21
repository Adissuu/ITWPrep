# Car Fleet

## There are n cars going to the same destination along a one-lane road. The destination is target miles away. You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour). Return the number of car fleets that will arrive at the destination.

```
class Solution(object):
    def carFleet(self, target, position, speed):
        stack = []
        PosSpeed = [(position, speed) for position, speed in zip(position,speed)]
        PosSpeed.sort(reverse=True) # Sorting by position and reversing

        for position, speed in PosSpeed:
            stack.append(float(target - position) / speed)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
```

### This was a tough problem, as we need to correctly picture it and since the wording is weird at times. To achieve this solution, we had to convert both list into one, sorting it by reverse position, and iterate through it. With each iteration, we append the time it will take for that car to achieve the end. If it is smaller or equal to the car in front of it, pop from the stack, because it becomes a fleet. Return the lenght of the stack. 