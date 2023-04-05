'''
source https://algorithmsandme.com/category/algorithms/greedy-algorithm/
'''

from operator import itemgetter

def min_Lateness(assignments):
    
    sortedAssignments = sorted(assignments, key=itemgetter(2))

    maxLateness = 0
    startTime = 0
    schedule = []

    for assignment in sortedAssignments:
        finishTime = startTime + assignment[1]

        if(finishTime > assignment[2]):
            maxLateness = max(maxLateness, (finishTime - assignment[2]))
        startTime = finishTime
        schedule.append(assignment[0])
    
    return maxLateness, schedule


assignments = [("A", 2, 2), ("B", 3, 4), ("C", 1, 6), ("D", 1, 6)] #(S.no, timetaken, deadline)
print(min_Lateness(assignments))