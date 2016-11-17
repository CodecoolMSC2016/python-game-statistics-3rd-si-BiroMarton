from reports import get_most_played_game
from reports import sum_sold
from reports import get_selling_avg
from reports import count_longest_title
from reports import get_date_avg
from reports import get_game
# For some reason the program didn't work when i imprted the reprts file, so I had to imprort the functions one by one.

print(get_most_played_game("game_stat.txt"))
print(sum_sold("game_stat.txt"))
print(get_selling_avg("game_stat.txt"))
print(count_longest_title("game_stat.txt"))
print(get_date_avg("game_stat.txt"))
print(get_game("game_stat.txt", "Diablo II"))


