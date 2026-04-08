def add_player(players, scores, new_player, new_score):
    players.append(new_player)
    scores.append(new_score)

def remove_player(players, scores, player_to_remove):
    found = False
    for i in range(len(players)):
        if players[i] == player_to_remove:
            players[:] = players[:i] + players[i+1:]
            scores[:] = scores[:i] + scores[i+1:]
            found = True
            break
    return found


def get_top_players(players, scores, count):
    temp_players = players[:]
    temp_scores = scores[:]
    top_players = []

    times = min(count, len(temp_scores))

    for _ in range(times):
        max_index = 0
        max_score = temp_scores[0]
        for i in range(1, len(temp_scores)):
            if temp_scores[i] > max_score:
                max_score = temp_scores[i]
                max_index = i

        top_players.append(temp_players[max_index])
        temp_players = temp_players[:max_index] + temp_players[max_index+1:]
        temp_scores = temp_scores[:max_index] + temp_scores[max_index+1:]

    return top_players


def manage_leaderboard(initial_players, initial_scores, new_player_data, player_to_remove, top_count):
    players = initial_players[:]
    scores = initial_scores[:]
    add_player(players, scores, new_player_data[0], new_player_data[1])
    remove_player(players, scores, player_to_remove)

   
    top_players = get_top_players(players, scores, top_count)

    return players, top_players



players = ["ACE", "BAM", "CID", "DAZ", "EGG"]
scores = [8800, 7500, 9200, 8100, 7900]
new_player = ["FIN", 9300]
remove_name = "BAM"
count = 3

final_players, top_list = manage_leaderboard(players, scores, new_player, remove_name, count)

print(f"Test Case 1 Results:")
print(f"Final Players: {final_players}")
print(f"Top List: {top_list}")    
