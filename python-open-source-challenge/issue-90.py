# ISSUE 90
#
# Problem:
# Write a program that accepts sports player records containing scores from multiple matches and calculates each player's total, average and highest score.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def player_score_report(players):
    report = {}
    for player in players:
        scores = player["scores"]
        # TODO: Check whether every match score contributes to the total.
        total = sum(scores[1:])
        average = total / len(scores) if scores else 0
        # TODO: Check how the highest match score is chosen.
        highest = min(scores) if scores else None
        report[player["name"]] = {"total":total,"average":average,"highest":highest}
    # TODO: Check that each player receives a report.
    return report

def check_solution():
    players = [{"name":"A","scores":[5,10,15]},{"name":"B","scores":[20,10]}]
    assert player_score_report(players) == {"A":{"total":30,"average":10,"highest":15},"B":{"total":30,"average":15,"highest":20}}
    assert player_score_report([]) == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
