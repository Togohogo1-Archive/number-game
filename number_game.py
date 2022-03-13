from random import choice

file_wlr = open("Win_Lose_Ratio.txt", "r")
file_add = open("Win_Lose_Ratio.txt", "a")

wlr = file_wlr.read()

# Calculates the win rates
def win_rate(wlr):
    try:
        print(f"Win Rate: {(wlr.count('1')/len(wlr))*100:.1f}%\n")
    except ZeroDivisionError:
        print("Win Rate: N/A\n")


# Check if the numbers in [1, 15]
def range_check(guess):
    for i in guess:
        if i not in range(1, 16):
            return False

    return True


# Check if the number of guesses are correct
def num_check(guess):
    count = 0

    for i in set(guess):
        if i in picked:
            count += 1

    return count


in_range = True  # Boolean flag for range_check()
num_of_guesses = True  # Boolean flag for num_check() if # of guesses in [1, 7]
fin_num_of_guesses = True  # Boolean flag for num_check() if final guess

picked = []
numbers = [i for i in range(1, 16)]

# Program choosing the numbers
for _ in range(3):
    picked.append(numbers.pop(numbers.index(choice(numbers))))

# Sorted it to print the numbers in order (getting wrong on final guess)
picked.sort()

# print(f"Numbers: {picked[0]}, {picked[1]}, {picked[2]}")
win_rate(wlr)

for i in range(8):
    temp_choice = []

    while True:  # If answer is invalid, keep on asking until answer is valid
        try:
            temp_choice = list(map(int, input(f"#{i+1}: ").split(", ")))

            # Check out of range
            if not range_check(temp_choice):
                in_range = False
            else:
                in_range = True

            if i < 7:  # Guess number 1 to 7
                if len(temp_choice) > 4:
                    num_of_guesses = False
                else:
                    num_of_guesses = True

            if i == 7:  # Final guess
                if len(temp_choice) != 3:
                    fin_num_of_guesses = False
                else:
                    fin_num_of_guesses = True

            if i < 7:
                if in_range and not num_of_guesses:
                    print("Input 1 to 4 integers.\n")
                elif not in_range and num_of_guesses:
                    print("Input integers between 1 to 15 inclusive.\n")
                elif not in_range and not num_of_guesses:
                    print("Input 1 to 4 integers between 1 to 15 inclusive.\n")
                else:
                    break
            elif i == 7:
                if in_range and not fin_num_of_guesses:
                    print("This is the final guess. Input exactly 3 integers.\n")
                elif not in_range and fin_num_of_guesses:
                    print("This is the final guess. Input integers between 1 to 15 inclusive.\n")
                elif not in_range and not fin_num_of_guesses:
                    print("This is the final guess. Input exactly 3 integers between 1 to 15 inclusive.\n")
                else:
                    break

        except ValueError:
            print("Invalid input. Try again.\n")

    #  This win condition holds true no matter the guess number
    if num_check(temp_choice) == 3 and len(set(temp_choice)) == 3:
        print("You Won! Congratulations!")
        file_add.write("1")
        break

    if i < 7:
        if num_check(temp_choice) == 1:  # Being vary of singular and plural
            print("Your guess contains 1 correct integer.\n")
        else:  # else not needed, but kept for consistency
            print(f"Your guess contains {num_check(temp_choice)} correct integers.\n")
    elif i == 7:
        print(f"You lost. The numbers were {picked[0]}, {picked[1]}, and {picked[2]}.")
        file_add.write("0")

file_add.close()
file_wlr.close()
