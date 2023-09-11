from random import shuffle
import pyttsx3
from team_generator import get_teams_2

def isMatch(plist, match):
    return match[0][0] in plist and match[0][1] in plist and match[1][0] in plist and match[1][1] in plist
def isInMatch(plist, match):
    return match[0][0] in plist or match[0][1] in plist or match[1][0] in plist or match[1][1] in plist


def occursMax1(match, array):
    count = 0
    plist = [match[0][0], match[0][1], match[1][0], match[1][1]]
    for a in array:
        if isInMatch(plist, a):
            count+=1

    return count <1

def occursAtLeast1(match, array):
    count = 0
    plist = get_teams_2()[0]
    for a in array:
        if isInMatch(plist, a):
            count+=1

    return count >= 1

def main():
    while True:
        player, all_teams = get_teams_2()
        shuffle(all_teams)

        teams1, teams2  = all_teams.copy()[:33], all_teams.copy()[33:66]

        blanks = [t for t in all_teams if "_" in t]
        no_blanks = [t for t in all_teams if "_" not in t]

        teams1 = blanks + no_blanks[:22]
        teams2 = no_blanks[22:]


        matches = []
        p_list = []
        try:
            while len(teams1) > 0:
                team1 = teams1.pop(0)
                if "_" in team1:
                    try:
                        team2 = [t for t in teams2 if team1[0] not in t and team1[1] not in t and t[0] not in p_list and t[1] not in p_list][0]
                        teams2.remove(team2)

                    except:
                        print("here")
                        team2 = [t for t in teams1 if team1[0] not in t and team1[1] not in t and t[0] not in p_list and t[1] not in p_list][0]
                        teams1.remove(team2)

                        new_team = teams2.pop()
                        teams1.append(new_team)

                    p_list.append(team2[0])
                    p_list.append(team2[1])

                else:
                    team2 = [t for t in teams2 if team1[0] not in t and team1[1] not in t ][0]
                    teams2.remove(team2)


                matches.append((team1, team2))

                if len(p_list) == 10:
                    p_list.clear()
            break 
        except:
            continue

    day_match_array = []
    hand = []
    for i in range (5):
        day_match_array.append([])
    
    for i in range(len(matches)):
        index = i % 5
        match = matches.pop()
        found = False
        for j in range(5):
            day_matches = day_match_array[(index + j) % 5 ]
            if occursMax1(match, day_matches) or occursAtLeast1(match, day_matches):
                day_matches.append(match)
                found = True
                break
        if not found:
            hand.append(match)

    for i, array in enumerate(day_match_array):
        print(f"Day {i}")
        for match in array:
            print(match)
        print("-------")

    for i in hand:
        print(i)

    # GREEDY
    # try:
    #     for solo_p in player:
    #         day_matches = []
    #         players_list = player.copy()
    #         while len(players_list) > 0: 
    #             match = [m for m in matches if isMatch(players_list, m)][0]
                
    #             players_list.remove(match[0][0])
    #             players_list.remove(match[0][1])
    #             players_list.remove(match[1][0])
    #             players_list.remove(match[1][1])

    #             matches.remove(match)

    #             day_matches.append(match)
    #         day_match_array.append(day_matches)
    # except:
    #     for i, array in enumerate(day_match_array):
    #         print(f"Day {i}")
    #         for match in array:
    #             print(match)
    #         print("-------")
    
if __name__ == "__main__":
    # while True:
    #     try:
    #         main()
    #     except:
    #         continue

    main()
    

