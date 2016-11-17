from reports import count_games
from reports import decide
from reports import get_latest
from reports import count_by_genre
from reports import get_line_number_by_title
# For some reason the program didn't work when i imprted the reprts file, so I had to imprort the functions one by one.

def export_results(result):
    file =open("export.txt", "a")
    file.write(str(result) + "\n")

export_results(str(count_games("game_stat.txt")))
export_results(str(decide("game_stat.txt", 2004)))
export_results(str(get_latest("game_stat.txt")))
export_results(str(count_by_genre("game_stat.txt", "RPG")))
export_results(str(get_line_number_by_title("game_stat.txt", "Diablo II")))
# Export functions