from memory_profiler import profile
import random

class User:
    def __init__(self, name):
        self.name = name

class Friendship:
    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2

@profile
def generate_users_and_friendships(n):
    users = [User(f'user{i}') for i in range(n)]
    friendships = [Friendship(user, random.choice(users)) for user in users for _ in range(random.randint(0, n))]
    return users, friendships

@profile
def calculate_average_friends(users, friendships):
    friend_counts = {user: 0 for user in users}
    for friendship in friendships:
        friend_counts[friendship.user1] += 1
        friend_counts[friendship.user2] += 1
    total_friends = sum(friend_counts.values())
    return total_friends / len(users)

users, friendships = generate_users_and_friendships(2000)
print(calculate_average_friends(users, friendships))
