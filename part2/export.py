from reports import get_most_played_game
from reports import sum_sold
from reports import get_selling_avg
from reports import count_longest_title
from reports import get_date_avg
from reports import get_game
# For some reason the program didn't work when i imprted the reprts file, so I had to imprort the functions one by one.

def export_results(result):
    file =open("export.txt", "a")
    file.write(str(result) + "\n")

export_results(str(get_most_played_game("game_stat.txt")))
export_results(str(sum_sold("game_stat.txt")))
export_results(str(get_selling_avg("game_stat.txt")))
export_results(str(count_longest_title("game_stat.txt")))
export_results(str(get_date_avg("game_stat.txt")))
export_results(str(get_game("game_stat.txt", "Diablo II")))
# Export functions
