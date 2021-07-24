# Inputs:
# - How many people are you expecting?
# - On average, how many drinks does each guest drink? Add one to each guest to ensure there is enough
# - Liquor of Choice (Choose up to 3)
# - Do you already have cups?
# - Do you already have mixers?

# Outputs:
# - Amount of bottles
# - Amount of Mixers
# - Amount of cups
# - Cases of Beer

# How to Calculate
# 1. Multiply amount of guests by drinks per person, use rowdiness level as a multiplier (increase or decrease)
# 3. Check if beers are to be considered in count

# Assumptions:
# 750ml bottles of liquor
# 16 drinks per bottle
# 1 liter of mixer per 3 guests
# 1 liter of soda costs $2

mixer_cost_per_liter = 2
guest_count = int(input("How many guests are you expecting? "))
drinks_per_person = int(input("On average, how many drinks does each guest drink? "))
bottle_price = int(input("On average, how much do you pay per bottle? "))

def main():
	drinks_count = total_drinks(guest_count, drinks_per_person)
	bottles_count = total_bottles(drinks_count)
	liters_of_mixers = total_mixers(guest_count)
	calculate_cost(bottles_count, liters_of_mixers, bottle_price)
 
# calculate total drinks needed
def total_drinks(guest_count, drinks_per_person):
	drinks_count = (guest_count * drinks_per_person) * 1.1
	return drinks_count


# calculate amount of bottles needed for that amount of drinks
def total_bottles(drinks_count):
	#assuming 16 drinks per bottle
	bottles_count = drinks_count / 16
	return bottles_count


def total_mixers(guest_count):
	#1 liter for every 3 guests
	liters_of_mixers = guest_count / 3
	return liters_of_mixers

def calculate_cost(bottles_count, liters_of_mixers, bottle_price):
	total_cost = (bottles_count * bottle_price) + (liters_of_mixers * mixer_cost_per_liter)
	print("\nFor {} guests, you will need approximately {:.1f} 750ml bottles and {} 1L mixers. \nThe total cost would be approximately ${:.2f} USD".format(guest_count, bottles_count, round(liters_of_mixers), total_cost))


if __name__ == "__main__":
    main()

