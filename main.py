import random
from art import logo, vs
from game_data import data
from clear import clear

# NTS: bug - sometimes chooses the same for a and b

print(logo)
correct_choice = True
current_score = 0
attempts = 0
while correct_choice == True:
    if attempts == 0:
        a = random.choice(data)
        b = random.choice(data)
        while b == a:
            b = random.choice(data)
    else:
        b = random.choice(data)
        while b == a:
            b = random.choice(data)
    print(f"Compare A: {a['name']}, a {a['description']} from {a['country']}.")
    print(f"psst, {a['follower_count']}.")
    print(vs)
    print(f"Compare B: {b['name']}, a {b['description']} from {b['country']}.")
    print(f"psst, {b['follower_count']}.")

    if a['follower_count'] > b['follower_count']:
        a = a
        most_followers = 'a'
    else:
        a = b
        most_followers = 'b'

    user_choice = input("Who has more followers? Type 'A' or 'B': ")
    user_choice.lower()
    if user_choice == most_followers:
        correct_choice = True
        current_score += 1
        attempts += 1
        clear()
        print(logo)
        print(f"You're right! Current score: {current_score}.")
    else:
        correct_choice = False
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {current_score}.")
