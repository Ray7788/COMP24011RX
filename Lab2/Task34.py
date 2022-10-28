from constraint import Problem, AllDifferentConstraint, ExactSumConstraint


def CommonSum(n):
    return int((1 + n * n) * n / 2)


def msqList(n, pairList):
    common_sum = CommonSum(n)

    problem = Problem ()
    problem.addVariables(range(0, n * n), range(1, n * n + 1))
    problem.addConstraint(AllDifferentConstraint(), range(0, n * n))

    for v, i in pairList:
        problem.addConstraint(ExactSumConstraint(i), [v])

    for row in range (n):
        problem.addConstraint(ExactSumConstraint(CommonSum(n)), [row * n + i for i in range(n)])

    for col in range (n):
        problem.addConstraint(ExactSumConstraint(CommonSum(n)), [i * n + col for i in range(n)])

    problem.addConstraint(ExactSumConstraint(CommonSum(n)), [i * n + i for i in range(n)])
    problem.addConstraint(ExactSumConstraint(CommonSum(n)), [i * n + n - 1 - i for i in range(n)])

    return problem.getSolutions()


def pmsList(n, pairList):
    common_sum = CommonSum(n)

    problem = Problem ()
    problem.addVariables(range(0, n * n), range(1, n * n + 1))
    problem.addConstraint(AllDifferentConstraint(), range(0, n * n))

    for v, i in pairList:
        problem.addConstraint(ExactSumConstraint(i), [v])

    for row in range (n):
        problem.addConstraint(ExactSumConstraint(CommonSum(n)), [row * n + i for i in range(n)])

    for col in range (n):
        problem.addConstraint(ExactSumConstraint(CommonSum(n)), [i * n + col for i in range(n)])

    problem.addConstraint(ExactSumConstraint(CommonSum(n)), [i * n + i for i in range(n)])
    problem.addConstraint(ExactSumConstraint(CommonSum(n)), [i * n + n - 1 - i for i in range(n)])

    diagonal_one = [i * n + i + 1 for i in range(n)]
    diagonal_one[n - 1] = (n - 1) * n
    diagonal_two = [i * n + i + n for i in range(n)]
    diagonal_two[n - 1] = (n - 1) 
    problem.addConstraint(ExactSumConstraint(common_sum), diagonal_one)
    problem.addConstraint(ExactSumConstraint(common_sum), diagonal_two)

    return problem.getSolutions()


if __name__ == '__main__':
    print("debug run...")
    sol = pmsList(5,[[0,20],[1,8],[2,21],[3,14],[4,2],[5,11],[6,4],[7,17],[8,10],[9,23]])
    print(sol)
