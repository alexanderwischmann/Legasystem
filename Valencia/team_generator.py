from random import shuffle

def get_teams_2():
    with open('members.csv', 'r') as f:
        members = [name.replace('\n', '') for name in f.readlines()]
    members.append("_")

    # print("The original list : " + str(members))

    teams = []
    n = len(members)
    for i in range(n):
        for j in range(i+1, n):
            teams.append((members[i], members[j]))

    return members, teams
    # print("All possible pairs : " + str(res))