# Higher Lower Game
from tools import clear
from game_data import data
import art
import random

score = 0
end_game = False
compare_a = random.choice(data)
compare_b = random.choice([x for x in data if x != compare_a])


def show_logo():
    clear()
    print(art.logo)


show_logo()

print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")
print(art.vs)
print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")
answer = input("Who has more followers? Type 'A' or 'B': ").lower()

if answer == 'a':
    if compare_a['follower_count'] < compare_b['follower_count']:
        end_game = True
    else:
        compare_b = random.choice([x for x in data if x != compare_a])
        score += 1
elif answer == 'b':
    if compare_b['follower_count'] < compare_a['follower_count']:
        end_game = True
    else:
        compare_a = compare_b
        compare_b = random.choice([x for x in data if x != compare_a])
        score += 1

while end_game is False:
    show_logo()
    print(f"You're right! Current score: {score}")
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")
    print(art.vs)
    print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if answer == 'a':
        if compare_a['follower_count'] < compare_b['follower_count']:
            end_game = True
        else:
            compare_b = random.choice([x for x in data if x != compare_a])
            score += 1
    elif answer == 'b':
        if compare_b['follower_count'] < compare_a['follower_count']:
            end_game = True
        else:
            compare_a = compare_b
            compare_b = random.choice([x for x in data if x != compare_a])
            score += 1

show_logo()
print(f"Sorry, that's wrong. Final score: {score}")
