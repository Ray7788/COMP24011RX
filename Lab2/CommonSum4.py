from constraint import Problem , AllDifferentConstraint, ExactSumConstraint

def CommonSum(n):
    return int((1 + n * n) * n / 2)

def pmsList(n, pairList):
    problem = Problem()
    problem.addVariables (range(0 , n * n ) , range(1 , n * n +1))
    problem.addConstraint(AllDifferentConstraint() , range(0 , n * n ))

    for v, i in pairList:
        problem.addConstraint(ExactSumConstraint(i), [v])
    
    for row in range ( n ):
        problem.addConstraint(ExactSumConstraint(CommonSum(n)) ,
        [ row * n + i for i in range ( n )])

    for col in range ( n ):
        problem.addConstraint(ExactSumConstraint(CommonSum(n)) ,
        [ col + n * i for i in range ( n )])

    # restrict diagonal top-left to bot-right
    problem.addConstraint(ExactSumConstraint(CommonSum(n)), [i for i in range(0, n**2, n+1)])

    # restrict diagonal bot-left to top-right
    problem.addConstraint(ExactSumConstraint(CommonSum(n)), [i for i in range(n**2-n, 0, -(n-1))])

    common_sum = CommonSum(n)

    diagonal_one = [i * n + i + 1 for i in range(n)]
    diagonal_one[n - 1] = (n - 1) * n
    diagonal_two = [i * n + i + n for i in range(n)]
    diagonal_two[n - 1] = (n - 1)

    problem.addConstraint(ExactSumConstraint(common_sum), diagonal_one)
    problem.addConstraint(ExactSumConstraint(common_sum), diagonal_two)
    
    solns = problem.getSolutions()
    return print (solns)

pmsList(4,[[0,13],[1,12],[2,7]])