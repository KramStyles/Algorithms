def solution(n, m, k) -> bool:
    # Create a set for each players to store the players they have not played against
    players = []
    for i in range(n):
        players.append(set())

    # Iterate through the games
    for game in k:
        # Split the players into two teams
        team1 = game[: n // 2]
        team2 = game[n // 2 :]

        # add the opposing team players to each players set
        for player in team1:
            players[player - 1].update(team2)

        for player in team2:
            players[player - 1].update(team1)

    # check that each player has played against all other players
    for i in range(n):
        if len(players[i]) != n - 1:
            return False

    return True


solution(4, 2, [[1, 2, 3, 4], [4, 3, 1, 2]])
solution(4, 2, [[1, 2, 3, 4], [1, 3, 2, 4]])
