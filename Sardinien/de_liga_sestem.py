from random import shuffle
import pyttsx3
from team_generator import get_teams

teams = get_teams()

N = len(teams)
TOTAL_MATCHES = (N * (N-1)) / 2
MATCHES_PER_DAY = 2

def main():
    matches_orig = []
    for i in range(N):
        team_a = teams[i]

        for j in range(i+1, N):
            team_b = teams[j]

            matches_orig.append([team_a, team_b])

    for i in range(1000):
        matches = matches_orig.copy()
        shuffle(matches)
        day, matches, output = create_plan(matches)

        if day == 4 and matches == 5:
            engine = pyttsx3.init()
            engine.say("Dehe Ligga System sahagt")
            engine.runAndWait()

            team_text = "TEAMS:\n \n "
            for t in teams:
                team_text += "  " + t + "\n"
            team_text += "Und de Plan: Na schauen wa doch wa nach"
            engine.say(team_text)
            engine.runAndWait()
            print(team_text)

            print("\nPLAN:\n")
            print(output)

            return
        else:
            continue
            #print("Versuch ", i, "Day ", day, "Matches ", matches)





def create_plan(matches):
    text_output = ""
    day_count = 1
    while matches:

        text_output += "Day " + str(day_count) + "\n\n"

        match_count = 1
        for i in range(MATCHES_PER_DAY):
            temp_teams = teams.copy()
            shuffle(temp_teams)
            while temp_teams:
                temp_team = temp_teams[0]

                temp_match = next((match for match in matches if (temp_team in match) and (match[0] in temp_teams) and (match[1] in temp_teams)), ["FILL", "FILL"])
                try:
                    matches.remove(temp_match)
                    temp_teams.remove(temp_match[0])
                    temp_teams.remove(temp_match[1])
                except:
                    return (day_count, match_count, text_output)

                text_output += "     " + str(match_count) +  ".  " + temp_match[0] + " - " + temp_match[1] + "\n"
                match_count += 1    

            text_output += "\n"
        
        day_count += 1

    
if __name__ == "__main__":
    main()

