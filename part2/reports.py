
# Report functions
def get_most_played_game(file_name):
    games = []
    sold = []
    list = open(file_name).read().split("\n")
    for game in list:
       games.append(game.split("\t"))
    for i in games:
        sold.append(float(i[1]))
    max = 0
    num = 0
    id = 0
    for most in sold:
        if (most > max):
            max = most
            id = num
        num += 1
    s = sold[id]
    for p in games:
        if float(p[1]) == float(s):
            return p[0]

def sum_sold(file_name):
    games = []
    sold = []
    list = open(file_name).read().split("\n")
    for game in list:
       games.append(game.split("\t"))
    for i in games:
        sold.append(float(i[1]))
    return sum(sold)


def get_selling_avg(file_name):
    games = []
    sold = []
    num = 0
    list = open(file_name).read().split("\n")
    for game in list:
       games.append(game.split("\t"))
    num = len(games)
    for i in games:
        sold.append(float(i[1]))
    return (sum(sold) / num)

def count_longest_title(file_name):
    games = []
    title = []
    list = open(file_name).read().split("\n")
    for game in list:
        games.append(game.split("\t"))
    for t in games:
        title.append(str(t[0]))
    longest = 0
    for l in title:
        l.strip(" ")
        if len(l) > longest:
            longest = len(l)
    return longest

def get_date_avg(file_name):
    games = []
    date = []
    num = 0
    list = open(file_name).read().split("\n")
    for game in list:
       games.append(game.split("\t"))
    num = len(games)
    for i in games:
        date.append(float(i[2]))
    return round(sum(date) / num)
def get_game(file_name, title):
    games = []
    list = open(file_name).read().split("\n")
    for game in list:
       games.append(game.split("\t"))
    for t in games:
        if t[0] == title:
            return t
