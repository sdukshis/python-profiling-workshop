import random
import time

def roll_dice():
    return random.randint(1, 6)

def draw_card():
    return random.choice(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])

def calculate_score(dice, card):
    if card in ['J', 'Q', 'K']:
        card = 10
    elif card == 'A':
        card = 11
    else:
        card = int(card)

    return dice + card

def play_game():
    dice = roll_dice()
    card = draw_card()
    score = calculate_score(dice, card)
    return score

def simulate_games(n):
    scores = []
    for _ in range(n):
        score = play_game()
        scores.append(score)
    return scores

if __name__ == "__main__":
    start_time = time.perf_counter()
    scores = simulate_games(1000000)
    end_time = time.perf_counter()
    print(f"Simulation took {end_time - start_time} seconds")
