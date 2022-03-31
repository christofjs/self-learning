class Solution:
    def areAlmostEqual(self, s1, s2):
        # return True if a single char swap will make the strings equal
        if s1 == s2:
            return True
        n = -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if n == -1:
                    n = i
                else:
                    if self.swapped(n,i,s1) == s2:
                        return True
                    else: return False
        return False

    def swapped(self, n, i, s1):
        swaps1 = ""
        for j in range(len(s1)):
            if j == n:
                swaps1 += s1[i]
            elif j == i:
                swaps1 += s1[n]
            else:
                swaps1 += s1[j]
        return swaps1

    def areAlmostEqual2(self, s1, s2):
        # return True if a single char swap will make the strings equal
        # 5/6 runtime, a little less memory using zip function
        differents = [[i,j] for i,j in zip(s1,s2) if i != j]
        return not differents or len(differents) == 2 and differents[0][::-1] == differents[1]

if 0:
    print(Solution().areAlmostEqual2("bank", "kanb"))
    print(Solution().areAlmostEqual2("attack", "defend"))
    print(Solution().areAlmostEqual2("kelb", "kelb"))