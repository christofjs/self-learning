class Solution(object):
    def nearestValidPoint(self, x, y, points):
        # point is valid if xi == x or yi == y
        # return valid point with shortest Manhattan distance to real point
        min = [float('inf'), float('inf')]
        for i in range(len(points)):
            xi = points[i][0]
            yi = points[i][1]
            if x == xi or y == yi:
                dist = abs(x-xi) + abs(y-yi)
                if dist < min[1]:
                    min[0] = i
                    min[1] = dist
        if min[0] == float('inf'):
            return -1
        else:
            return min[0]

if 1:
    print(Solution().nearestValidPoint(3,4,[[1,2],[3,1],[2,4],[2,3],[4,4]]))