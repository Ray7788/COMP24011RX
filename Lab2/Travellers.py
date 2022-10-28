#!/usr/bin/env python3
from constraint import Problem , AllDifferentConstraint , ExactSumConstraint

# Task 1    

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
# for person in people :
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

# # The four travellers are Pablo, the traveller flying from Yemen, the person leaving at 2:30 pm and the person leaving at 3:30 pm.
# for person in people :
#     problem.addConstraint(
#         (lambda x, y, z, m: (
#             ( y != "yemen") or ( x != "2:30") or ( x != "3:30"))and 
#         (( z != "2:30") or ( z != "3:30") and ( m != "yemen"))),
#         ["t_" + person, "d_" + person, "t_pablo", "d_pablo" ])

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