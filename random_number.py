import random

# Generate a random number
random_number = random.randint(1, 100)

# Write the random number to a file
with open('random_number.txt', 'w') as file:
    file.write(str(random_number))