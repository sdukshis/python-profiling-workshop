from game_of_chance import play_game

def test_play_game(benchmark):
    score = benchmark(play_game)
