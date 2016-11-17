from reports import count_games
from reports import decide
from reports import get_latest
from reports import count_by_genre
from reports import get_line_number_by_title
# For some reason the program didn't work when i imprted the reprts file, so I had to imprort the functions one by one.

print(count_games("game_stat.txt"))
print(decide("game_stat.txt", 2004))
print(get_latest("game_stat.txt"))
print(count_by_genre("game_stat.txt", "RPG"))
print(get_line_number_by_title("game_stat.txt", "Terraria"))
# Printing functions
