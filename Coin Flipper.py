import random,time, datetime
#heads are 0
#tails are 1
i = 0
number_of_heads = 0
number_of_tails = 0
number_of_flips = input("How many times do you want to flip the coin?")
flips_coin_n = int(number_of_flips)
def flip_coin():

    return random.randint(0,1)

while i < flips_coin_n:
    flip_coin()
    if flip_coin() == 0:
            number_of_heads = number_of_heads + 1
    else:
            number_of_tails = number_of_tails + 1
    i = i + 1
coins_flipped = number_of_heads + number_of_tails
chance_heads = number_of_heads / coins_flipped
chance_tails = number_of_tails / coins_flipped

print("This is the number of heads " + str(number_of_heads))
print("This is the number of tails " + str(number_of_tails))
print("This is the probability that a flipped coin will result in heads: " + str(chance_heads))
print("This is the probability that a flipped coin will result in tails: " + str(chance_tails))
