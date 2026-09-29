# ISSUE 31
#
# Problem:
# Write a program that accepts player names and their scores from multiple matches and calculates each player's total score and ranking. Players on the same total share the same rank, and the next rank skips accordingly — two players tied at rank 1 are followed by rank 3, not rank 2.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def player_rankings(players):
    rows = []
    for player in players:
        # TODO: Check that every match score contributes to the total.
        total = sum(player["scores"][1:])
        rows.append({"name": player["name"], "total": total})
    # TODO: Check whether highest totals come first.
    rows.sort(key=lambda row: row["total"])
    for place, row in enumerate(rows, 1):
        # TODO: Check how the place number maps to the player's rank.
        # TODO: Check what rank a player should get when an earlier player has the same total.
        row["rank"] = place
    return rows

def check_solution():
    players = [{"name":"Ari","scores":[10,20,30]},{"name":"Bo","scores":[25,35]},{"name":"Cy","scores":[40,5]}]
    result = player_rankings(players)
    assert result == [{"name":"Ari","total":60,"rank":1},{"name":"Bo","total":60,"rank":1},{"name":"Cy","total":45,"rank":3}]
    assert player_rankings([]) == []

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
