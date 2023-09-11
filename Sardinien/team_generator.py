from random import shuffle

def get_teams():
    member = [
        "Alex",
        "Bene", 
        "An", 
        "Tobi_F",
        "Tobi_M",
        "Flo",
        "Nick",
        "Mick",
        "Cedric",
        "Martin",
        "Steffen",
        "Hendrik",
        "Basti",
        "Felix",
        "Leon",
        "Julius",
    ]

    shuffle(member)

    teams = []
    for i in range(0, len(member), 2):
        teams.append(f"{member[i]} & {member[i+1]}")

    return teams