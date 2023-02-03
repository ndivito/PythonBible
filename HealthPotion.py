import random

health = 50
difficulty = 5
health_lower_bound = 25/difficulty
health_upper_bound = 50/difficulty
potion_health = random.randint(health_lower_bound,health_upper_bound)

health = health + potion_health

print(health)

