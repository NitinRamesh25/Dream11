# NOTE only works for t20, as batsmen take more risk when batting first
# Bias exception 
#   - wkt keeper (pick whichever seems best. If equal, then use both)
#   - blacklisted players need not be included when picking teams (rarely perform)
#   - all rounders that dont bowl (alternatively pick more bowlers)

# BLACKLIST
# CSK - K Jadav

# Allrounders that did not bowl (might not give many points)
# MI - polard, h pandya

# 2 bow from secondBatting 2 bow from firstBatting
# 2 all from secondBatting 1 all from firstBatting
# 2 bat from secondBatting 1 bat from firstBatting
# 1 wkt keeper from either team

# TODO 
# - point/credit system (max limit 100)
#   Scenario where points are not sufficient. 
#   Pick the bowler and batsmen from fristbatting team, and try managing with allrounder. 
#   If not possible, first compromise on batsman and try once again. 
#   If not at all possible, then compromise on bowler and keep original batsmen and try picking all rounders.
#
# - considering set of batsmen, allrounder and bowlers, the combination of sets might repeat
#   swap second and first batting team
# - what if more than 1 wkt keeper play from a team as a batsman
#
# - captian and vc pick for each team
#   c and vc should be two batsmen of second batting team
#   2 teams at the end can have c as wkt keeper
#   pick c and vs for 6 teams for the actualy secondbatting team and 5 teams with the actual firstbatting team   

# 3 x 4 should be max, a total of 12 combinations
# Any list in second batting team must have 3 max
# If you want two bowlers per dreamteam from first batting team, then club them in tuples of 2
# and take only one tuple from the list for combinations

import itertools

# CSK vs MI
# firstBatting = {'bat':['rohit','s yadav','s tiwari'], 'all':['h pandya','k pandya','pollard'], 'bow':['pattinson','r chahar','boult', 'bumrah']}
# secondBatting = {'bat':['vijay','watson','du plesis','raydu'], 'all':['jadeja','s curran'], 'bow':['d chahar','chawla','nigidi']}

# KingsXI vs DC
# firstBatting = {'bat':['dhawan','iyer','p shaw','hetmyer'], 'all':['a patel','m stoinis'], 'bow':[('rabada','ashwin'),('nortje','m sharma')]}
# secondBatting = {'bat':['m agarwal','k nair','s khan'], 'all':['maxwell','gowtham'], 'bow':['shami','jordan','cottrell']} # bishoni removed

firstBatting = {'bat':['','',''], 'all':['',''], 'bow':['','','']}
secondBatting = {'bat':['','',''], 'all':['',''], 'bow':['','','']} 


def allCombinations(players, pickCount):
    return list(itertools.combinations(players, pickCount))


def permuteTwoLists(list1, list2):
    unique = itertools.product(list1, list2)
    return list(unique)


def printTeam(team, teamNumber):
    print('\nStart of team {0}\n'.format(teamNumber))
    for element in team:
        print(element)
    print('\nEnd of team\n')


if __name__=='__main__':

    batsmen_combinations = permuteTwoLists(allCombinations(secondBatting['bat'], 2), firstBatting['bat'])

    # print('{0} {1}'.format(len(batsmen_combinations), batsmen_combinations))

    allrounder_combinations = permuteTwoLists(allCombinations(secondBatting['all'], 2), firstBatting['all'])

    # print('{0} {1}'.format(len(allrounder_combinations), allrounder_combinations))

    bowler_combinations = permuteTwoLists(allCombinations(secondBatting['bow'], 2), firstBatting['bow'])

    # print('{0} {1}'.format(len(bowler_combinations), bowler_combinations))

    totalTeams = max(len(batsmen_combinations), len(allrounder_combinations), len(bowler_combinations))

    print('total teams = {0}'.format(totalTeams))

    for i in range(totalTeams):
        team = []

        team.append(batsmen_combinations[i % len(batsmen_combinations)])
        team.append(allrounder_combinations[i % len(allrounder_combinations)])
        team.append(bowler_combinations[i % len(bowler_combinations)])

        printTeam(team, i+1)
    