class Solution(object):
    def average(self, salary):
        # return average of list, excluding min and max
        min = salary[0]
        max = salary[0]
        tot = 0.0
        for i in salary:
            tot += i
            if i < min:
                min = i
            if i > max:
                max = i
        tot -= (min + max)
        return tot / (len(salary) - 2)

    def average2(self, salary):
        salary.sort()
        tot = sum(salary[1:-1])
        return tot / (len(salary) - 2)


if 1:
    salary = [48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]
    print(Solution().average2(salary))
    salary = [1000,2000,3000]
    print(Solution().average2(salary))