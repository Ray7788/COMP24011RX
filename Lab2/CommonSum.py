from constraint import Problem , AllDifferentConstraint, ExactSumConstraint

def CommonSum(n):
    problem = Problem()
    problem.addVariables (range(0 , n * n ) , range(1 , n * n +1))
    problem.addConstraint(AllDifferentConstraint() , range(0 , n * n ))

    for row in range ( n ):
        problem.addConstraint(ExactSumConstraint(CommonSum(n)) ,
        [ row * n + i for i in range ( n )])

    for col in range ( n ):
        problem.addConstraint(ExactSumConstraint(CommonSum(n)) ,
        [ col * n + i for i in range ( n )])

    # restrict diagonal top-left to bot-right
    problem.addConstraint(ExactSumConstraint(CommonSum(n)), [i for i in range(0, n**2, n+1)])

    # restrict diagonal bot-left to top-right
    problem.addConstraint(ExactSumConstraint(CommonSum(n)), [i for i in range(n**2-n, 0, -(n-1))])

    solns = problem.getSolutions()
    return print (solns)
    # print (solns)

CommonSum(1)