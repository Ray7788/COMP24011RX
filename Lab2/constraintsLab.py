#!/usr/bin/env python3
from constraint import Problem , AllDifferentConstraint , ExactSumConstraint


# Task 1    
def Travellers(List):
    problem = Problem()
    people = [ "claude" , "olga", "pablo" , "scott" ]
    times = [ "2:30" , "3:30" , "4:30" , "5:30" ]
    destinations = [ "peru" , "romania" , "taiwan" , "yemen" ]

    t_variables = list ( map( lambda x : "t_" +x , people ))
    d_variables = list ( map( lambda x : "d_" +x , people ))

    problem . addVariables ( t_variables , times )
    problem . addVariables ( d_variables , destinations )
    problem . addConstraint( AllDifferentConstraint() , t_variables )
    problem . addConstraint( AllDifferentConstraint() , d_variables )

    # Olga is leaving 2 hours before the traveller from Yemen .
    for person in people :
        problem.addConstraint(
            (lambda x , y , z : ( y != "yemen") or
                (( x == "4:30" ) and ( z == "2:30" )) or
                (( x == "5:30" ) and ( z == "3:30" ))) ,
            ["t_" + person , "d_" + person , "t_olga"])

    # Claude is either the person leaving at 2:30 pm or the traveller leaving at 3:30 pm.
    problem.addConstraint(
        (lambda x : ( x != "2:30") and
            ( x != "3:30")) ,
        ["t_claude"])

    # The person leaving at 2:30 pm is flying from Peru.
    for person in people :
        problem.addConstraint(
            (lambda x, y: ( y != "peru") or (( y == "peru") and ( x == "2:30" ))),
            ["t_" + person , "d_" + person])

    # The person flying from Yemen is leaving earlier than the person flying from Taiwan
    for person in people :
        for person2 in people :
            problem.addConstraint(
                lambda x, y, z, m:( (m != "taiwan") or 
                (y != "yemen") or
                (( x == "2:30") and (( z == "3:30") or ( z == "4:30") or ( z == "5:30"))) or 
                (( x == "3:30") and (( z == "4:30") or ( z == "5:30")))or 
                (( x == "4:30") and ( z == "5:30"))),
                ["t_" + person , "d_" + person, "t_" + person2, "d_" + person2]
            )

    # Pablo is not flying from Yemen and is leaving at neither 2:30 nor 3:30;
    for person in people :
        problem.addConstraint(
            (lambda z , m: (( m != "yemen") and 
            ( z != "3:30" ) and ( z != "2:30" ))) ,
            ["t_pablo", "d_pablo"])

    # whoever is flying from Yemen is likewise leaving at neither 2:30 nor 3:30
    for person in people :
        problem.addConstraint(
            (lambda x, y: ( y != "yemen") or 
            (( x != "2:30") and ( x != "3:30") and 
            ( y == "yemen"))),
            ["t_" + person, "d_" + person  ])

    solns = problem.getSolutions()
    print (solns)


# Task 2
def CommonSum(n):
    return int((1 + n * n) * n / 2)


# Task 3
def msqList(n, pairList):
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

    # restrict diagonal top-left to bottom-right
    problem.addConstraint(ExactSumConstraint(CommonSum(n)), [i for i in range(0, n**2, n+1)])

    # restrict diagonal bottom-left to top-right
    problem.addConstraint(ExactSumConstraint(CommonSum(n)), [i for i in range(n**2-n, 0, -(n-1))])

    solns = problem.getSolutions()
    return print (solns)


# Task 4
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

    # restrict diagonal top-left to bottom-right
    problem.addConstraint(ExactSumConstraint(CommonSum(n)), [i for i in range(0, n**2, n+1)])

    # restrict diagonal bottom-left to top-right
    problem.addConstraint(ExactSumConstraint(CommonSum(n)), [i for i in range(n**2-n, 0, -(n-1))])

    common_Sum = CommonSum(n)

    diagonal1 = [i * n + i + 1 for i in range(n)]
    diagonal1[n - 1] = n * (n - 1) 
    diagonal2 = [i * n + i + n for i in range(n)]
    diagonal2[n - 1] = (n - 1)

    # each member of dd is a list of those variables lying along some broken diagonal.
    dd = [diagonal1, diagonal2]
    problem.addConstraint(ExactSumConstraint(common_Sum), dd[0])
    problem.addConstraint(ExactSumConstraint(common_Sum), dd[1])
    
    solns = problem.getSolutions()
    return print (solns)


# Debug
if __name__ == '__main__':
    print("debug run...")

