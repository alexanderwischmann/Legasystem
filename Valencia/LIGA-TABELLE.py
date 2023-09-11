import re 
import json

def fetchData():
    lines = []
    with open("plan.txt") as file:
        lines = file.readlines()
    members = []
    with open("members.csv") as file:
        members = [name.replace('\n', '') for name in file.readlines()]
    PLAYER_DICT = {}
    for player in members:
        PLAYER_DICT[player] = {
            "Spiele": 0,
            "Punkte": 0,
            "Siege": 0,
            "Nied": 0,
            "Ties":0,
            "Treffer": 0,
            "Diff": 0,
            "Tre / Sp": 0
        }
 
    for line in lines:
        names = re.findall("\'[a-zA-Z_]{1,12}\'", line)
        stats = re.findall("[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", line)
        stats = [s.replace(' ', '') for s in stats]

        if len(names) == 0 or len(stats) == 0:
            continue

        names  = [n[1:-1] for n in names]
        match  = (int(stats[0]), int(stats[1]))
        hits = [float(p) for p in stats[2:]]
        for i, name in enumerate(names):
            if name == "_":
                continue
            isTie = match[0] < 10 and match[1] < 10
            isWin = match[int(i/2)] > match[(int(i/2 + 1)%2)]  and not isTie
            points = 3 if isWin else (1 if isTie else 0)

            newHits = hits[i] 
            
            PLAYER_DICT[name]["Spiele"] = PLAYER_DICT[name]["Spiele"] + 1
            PLAYER_DICT[name]["Punkte"] = PLAYER_DICT[name]["Punkte"] + points
            if isTie:
                PLAYER_DICT[name]["Ties"] = PLAYER_DICT[name]["Ties"] + 1
            elif isWin:
                PLAYER_DICT[name]["Siege"] = PLAYER_DICT[name]["Siege"] + 1
            else:
                PLAYER_DICT[name]["Nied"] = PLAYER_DICT[name]["Nied"] + 1
            PLAYER_DICT[name]["Treffer"] = PLAYER_DICT[name]["Treffer"] + newHits
            PLAYER_DICT[name]["Diff"] = PLAYER_DICT[name]["Diff"] + match[int(i/2)] - match[(int(i/2 + 1)%2)] 
            PLAYER_DICT[name]["Tre / Sp"] =  PLAYER_DICT[name]["Treffer"] / PLAYER_DICT[name]["Spiele"] 

            # print(PLAYER_DICT[name])
    keys=PLAYER_DICT[next(iter(PLAYER_DICT.keys()))].keys()

    best_player_per_key={}
    second_best_player_per_key={}
    for key in keys:
        best_value=-1000000
        best_player=None
        second_best_player=None
        second_best_value=-1000000
        for player, obj in PLAYER_DICT.items():
            if obj[key] > best_value:
                second_best_player=best_player
                second_best_value=best_value
                best_player =player
                best_value=obj[key]
            elif obj[key]> second_best_value:
                second_best_player=player
                second_best_value=obj[key]


        best_player_per_key[key] =best_player
        second_best_player_per_key[key]=second_best_player

    for key, player in best_player_per_key.items():
        if not "highest_scores" in PLAYER_DICT[player].keys():
            PLAYER_DICT[player]["highest_scores"] =[]
        PLAYER_DICT[player]["highest_scores"].append(key)

    print(json.dumps(PLAYER_DICT, indent=5))
    for key, player in second_best_player_per_key.items():
        if player is None:
            continue
        if not "2nd_highest_scores" in PLAYER_DICT[player].keys():
            PLAYER_DICT[player]["2nd_highest_scores"] =[]
        PLAYER_DICT[player]["2nd_highest_scores"].append(key)
    
    return PLAYER_DICT

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printTabelle(player_dict):
    
    
    sortedList = [(key, {**value, "Platz": i+1}) for i,(key , value) in enumerate(sorted(player_dict.items(), key=lambda p: (p[1]["Punkte"], p[1]["Treffer"]), reverse=True))]

    keys=["Spiele", "Punkte","Siege", "Nied","Ties", "Treffer", "Diff", "Tre / Sp"]
    print(bcolors.UNDERLINE+"\tSpieler\t\t"+"\t".join(keys)+bcolors.ENDC+"\n")
    for i, (player, value) in enumerate(sortedList):
        line = f"{i+1}.\t"
        line += f"{bcolors.OKCYAN}{bcolors.BOLD}{player}{bcolors.ENDC}\t"
        for key in keys:
            is_best=key in player_dict[player].get("highest_scores",[])
            is_2nd_best=key in player_dict[player].get("2nd_highest_scores",[])
            start_char =bcolors.OKGREEN+bcolors.BOLD if is_best else bcolors.WARNING if is_2nd_best else ""
            end_char =bcolors.ENDC if is_best or is_2nd_best else ''
            line+=f"\t{start_char}{value[key]:.3g}{end_char}"
            # line +=f"{is_best}"
        print(f"{line}\n")

def animateTabelle():
    return

def main():
    PLAYER_DICT = fetchData()
    printTabelle(PLAYER_DICT)
    
        


if __name__ == "__main__":
    main()