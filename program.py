import random

def main():
	start, end = 1, 10
	init()
	answer = random.randint(start, end)

	correct = False
	while not correct:
		guess = ask_number(start, end)
		if is_valid(guess, start, end):
			correct = check_guess(guess, answer)
		else:
			print("Enter the valid number.")


def init():
	print("**************************************************")
	print("**************************************************")
	print("                 GUESS NUMBER")
	print("**************************************************")
	print("**************************************************")
	print()


def ask_number(start, end):
	guess = input("Guess the number from {} to {}: ".format(start, end))
	try:
		guess = int(guess)
	except ValueError:
		print("Enter the decimal number.")
		guess = ask_number(start, end)
	return guess


def is_valid(guess, start, end):
	return start <= guess <= end


def check_guess(guess, answer):
	if guess < answer:
		print("Your guess is too low!")
		return False
	elif guess > answer:
		print("Your guess is too high!")
		return False
	else:
		print("Correct!!!!")
		return True


if __name__ == '__main__':
	main()
