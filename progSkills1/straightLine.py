class Solution:
    def checkStraightLine(self, coordinates):
        if len(coordinates) == 2:
            return True
        # y = m1/m2 * x + b
        # m2*y = m1*x + m2*b
        # avoid decimal issues with online checker
        m1 = (coordinates[1][1] - coordinates[0][1])
        m2 = (coordinates[1][0] - coordinates[0][0])
        m2b = m2*coordinates[0][1] - m1*coordinates[0][0]
        for i in range(2, len(coordinates)):
            if m2*coordinates[i][1] != m1*coordinates[i][0] + m2b:
                return False
        return True

if 0:
    print(Solution().checkStraightLine([[2,1],[4,2],[6,3]]))