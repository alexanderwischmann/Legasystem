from random import shuffle

def get_teams_2():
    with open('members.csv', 'r') as f:
        members = [name.replace('\n', '') for name in f.readlines()]
    members.append("_")

    # print("The original list : " + str(members))

    res = []
    n = len(members)
    for i in range(n):
        for j in range(i+1, n):
            res.append((members[i], members[j]))

    return members, res
    # print("All possible pairs : " + str(res))