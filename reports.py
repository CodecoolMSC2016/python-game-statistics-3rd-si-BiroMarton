def count_games(file_name):
    with open (file_name) as f:
        return len(f.readlines())

def decide(file_name, year):
    games = []
    list = open(file_name).read().split("\n")
    for game in list:
       games.append(game.split("\t"))
    for i in games:
        if i[2] == str(year):
            return True

def get_latest(file_name):
    games = []
    years = []
    list = open(file_name).read().split("\n")
    for game in list:
       games.append(game.split("\t"))
    for i in games:
        years.append(int(i[2]))
    max = 0
    num = 0
    id = 0
    for latest in years:
        if (latest > max):
            max = latest
            id = num
        num += 1
    y = years[id]
    for t in games:
        if t[2] == str(y):
            return t[0]


def count_by_genre(file_name, genre):
    games = []
    count = 0
    list = open(file_name).read().split("\n")
    for game in list:
       games.append(game.split("\t"))
    for i in games:
       if (i[3]) == genre:
           count += 1
    return count

def get_line_number_by_title(file_name, title):
    games = []
    line = 0
    list = open(file_name).read().split("\n")
    for game in list:
       games.append(game.split("\t"))
    for name in games:
        line += 1
        if (name[0]) == title:
                return line
    raise ValueError

# Report functions